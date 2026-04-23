#!/usr/bin/env python3
"""Validate and analyze revision task DAGs for clo-revise."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

BLOCK_ORDER = {"?": -1, "A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
REQUIRED_FIELDS = {
    "reviewer_source",
    "quote",
    "category",
    "description",
    "status",
    "owner",
    "depends_on",
    "decision_flag",
    "affected_sections",
    "affected_outputs",
}


def load_tasks(path: Path) -> Dict[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict) and "tasks" in data and isinstance(data["tasks"], dict):
        tasks = data["tasks"]
    elif isinstance(data, dict):
        tasks = data
    else:
        raise ValueError("Task graph must be a JSON object or an object with a 'tasks' key.")

    normalized = {}
    for task_id, task in tasks.items():
        if not isinstance(task, dict):
            raise ValueError(f"Task '{task_id}' must map to an object.")
        normalized[str(task_id)] = task
    return normalized


def validate_schema(tasks: Dict[str, dict]) -> List[str]:
    errors = []
    for task_id, task in tasks.items():
        missing = sorted(REQUIRED_FIELDS - set(task))
        if missing:
            errors.append(f"{task_id}: missing required fields: {', '.join(missing)}")
        depends = task.get("depends_on", [])
        if not isinstance(depends, list):
            errors.append(f"{task_id}: depends_on must be a list")
        for dep in depends if isinstance(depends, list) else []:
            if dep not in tasks:
                errors.append(f"{task_id}: unknown dependency '{dep}'")
        for field in ("affected_sections", "affected_outputs"):
            value = task.get(field, [])
            if not isinstance(value, list):
                errors.append(f"{task_id}: {field} must be a list")
        block = task.get("block", "?")
        if block not in BLOCK_ORDER:
            errors.append(f"{task_id}: invalid block '{block}'")
    return errors


def build_graph(tasks: Dict[str, dict]) -> Tuple[Dict[str, List[str]], Dict[str, int]]:
    outgoing = defaultdict(list)
    indegree = {task_id: 0 for task_id in tasks}
    for task_id, task in tasks.items():
        for dep in task.get("depends_on", []):
            outgoing[dep].append(task_id)
            indegree[task_id] += 1
    return outgoing, indegree


def topo_sort(tasks: Dict[str, dict], outgoing: Dict[str, List[str]], indegree: Dict[str, int]):
    queue = deque(sorted([task_id for task_id, degree in indegree.items() if degree == 0]))
    ordered = []
    indegree_work = dict(indegree)
    batches = []
    while queue:
        batch = list(queue)
        batches.append(batch)
        next_queue = deque()
        while queue:
            node = queue.popleft()
            ordered.append(node)
            for downstream in sorted(outgoing[node]):
                indegree_work[downstream] -= 1
                if indegree_work[downstream] == 0:
                    next_queue.append(downstream)
        queue = next_queue
    if len(ordered) != len(tasks):
        return None, None
    return ordered, batches


def find_cycle(tasks: Dict[str, dict]) -> List[str]:
    state = {task_id: 0 for task_id in tasks}
    stack = []

    def dfs(node: str):
        state[node] = 1
        stack.append(node)
        for dep in tasks[node].get("depends_on", []):
            if state[dep] == 0:
                cycle = dfs(dep)
                if cycle:
                    return cycle
            elif state[dep] == 1:
                start = stack.index(dep)
                return stack[start:] + [dep]
        stack.pop()
        state[node] = 2
        return []

    for task_id in tasks:
        if state[task_id] == 0:
            cycle = dfs(task_id)
            if cycle:
                return cycle
    return []


def block_violations(tasks: Dict[str, dict]) -> List[str]:
    violations = []
    for task_id, task in tasks.items():
        task_block = task.get("block", "?")
        if task_block == "?":
            continue
        for dep in task.get("depends_on", []):
            dep_block = tasks[dep].get("block", "?")
            if dep_block == "?":
                continue
            if BLOCK_ORDER[dep_block] > BLOCK_ORDER[task_block]:
                violations.append(
                    f"{task_id}: depends on {dep} but block order is invalid ({task_block} before {dep_block})"
                )
    return violations


def longest_paths(tasks: Dict[str, dict], ordered: Iterable[str], outgoing: Dict[str, List[str]]):
    depth = {task_id: 1 for task_id in tasks}
    parent = {task_id: None for task_id in tasks}
    for node in ordered:
        for downstream in outgoing[node]:
            candidate = depth[node] + 1
            if candidate > depth[downstream]:
                depth[downstream] = candidate
                parent[downstream] = node
    end = max(depth, key=depth.get)
    path = []
    cursor = end
    while cursor is not None:
        path.append(cursor)
        cursor = parent[cursor]
    path.reverse()
    return path


def descendant_counts(tasks: Dict[str, dict], outgoing: Dict[str, List[str]], ordered: Iterable[str]):
    descendants = {task_id: set() for task_id in tasks}
    for node in reversed(list(ordered)):
        for downstream in outgoing[node]:
            descendants[node].add(downstream)
            descendants[node].update(descendants[downstream])
    return {task_id: len(values) for task_id, values in descendants.items()}


def optional_networkx_summary(tasks: Dict[str, dict], outgoing: Dict[str, List[str]]):
    try:
        import networkx as nx  # type: ignore
    except Exception:
        return None

    graph = nx.DiGraph()
    for task_id in tasks:
        graph.add_node(task_id)
    for upstream, downstreams in outgoing.items():
        for downstream in downstreams:
            graph.add_edge(upstream, downstream)

    critical_path = nx.algorithms.dag.dag_longest_path(graph)
    bottlenecks = sorted(
        ((node, len(nx.descendants(graph, node))) for node in graph.nodes),
        key=lambda item: (-item[1], item[0]),
    )[:5]
    return {"critical_path": critical_path, "bottlenecks": bottlenecks}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and analyze revision task DAGs.")
    parser.add_argument("task_graph", help="Path to revision_task_graph JSON file.")
    parser.add_argument("--validate-only", action="store_true", help="Run structural validation only.")
    args = parser.parse_args()

    try:
        tasks = load_tasks(Path(args.task_graph))
    except Exception as exc:
        print(f"FAILED: could not load task graph: {exc}", file=sys.stderr)
        return 1

    errors = validate_schema(tasks)
    errors.extend(block_violations(tasks))
    if errors:
        print("FAILED: schema or sequencing errors detected:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    outgoing, indegree = build_graph(tasks)
    ordered, batches = topo_sort(tasks, outgoing, indegree)
    if ordered is None:
        cycle = find_cycle(tasks)
        cycle_text = " -> ".join(cycle) if cycle else "unknown cycle"
        print(f"FAILED: cycle detected: {cycle_text}", file=sys.stderr)
        return 1

    edge_count = sum(len(task.get("depends_on", [])) for task in tasks.values())
    if args.validate_only:
        print(f"PASSED: {len(tasks)} tasks, {edge_count} dependencies, acyclic.")
        return 0

    critical_path = longest_paths(tasks, ordered, outgoing)
    bottlenecks = sorted(descendant_counts(tasks, outgoing, ordered).items(), key=lambda item: (-item[1], item[0]))[:5]
    print(f"PASSED: {len(tasks)} tasks, {edge_count} dependencies, acyclic.")
    print(f"Parallel batches: {len(batches)}")
    for idx, batch in enumerate(batches, start=1):
        print(f"  Batch {idx}: {', '.join(batch)}")
    print(f"Critical path: {' -> '.join(critical_path)}")
    if bottlenecks:
        print("Top bottlenecks:")
        for task_id, count in bottlenecks:
            print(f"  {task_id}: blocks {count} downstream task(s)")
    nx_summary = optional_networkx_summary(tasks, outgoing)
    if nx_summary:
        print("NetworkX summary:")
        print(f"  Longest path: {' -> '.join(nx_summary['critical_path'])}")
        for task_id, count in nx_summary["bottlenecks"]:
            print(f"  {task_id}: {count} downstream descendant(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
