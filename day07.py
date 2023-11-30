#!/usr/bin/env python
from collections import defaultdict
import string

step_times = {k: v for v, k in enumerate(string.ascii_uppercase, 61)}


def do_part_1(lines: list[str]) -> str:
    conditions = defaultdict(set)
    dependencies = defaultdict(set)
    for line in lines:
        conditions[line[36]].add(line[5])
        dependencies[line[5]].add(line[36])
    for d in dependencies:
        if d not in conditions:
            conditions[d] = set()
    final_order = []
    while conditions:
        next_step = sorted((k for k, v in conditions.items() if not v))[0]
        final_order.append(next_step)
        for d in dependencies[next_step]:
            conditions[d].discard(next_step)
        del conditions[next_step]

    return "".join(final_order)


def do_part_2(lines) -> int:
    conditions = defaultdict(set)
    dependencies = defaultdict(set)
    for line in lines:
        conditions[line[36]].add(line[5])
        dependencies[line[5]].add(line[36])
    for d in dependencies:
        if d not in conditions:
            conditions[d] = set()

    clock = 0
    num_workers = 5
    workers = [0 for _ in range(num_workers)]
    under_construction: dict[str, int] = {}

    while conditions or under_construction:
        for k in list(under_construction):
            if under_construction[k] == 0:
                for d in dependencies[k]:
                    conditions[d].discard(k)
                del under_construction[k]

        next_steps = sorted((k for k, v in conditions.items() if not v))
        if next_steps:
            for step in next_steps:
                for i, w in enumerate(workers):
                    if w == 0:
                        workers[i] = step_times[step]
                        under_construction[step] = step_times[step]
                        del conditions[step]
                        break

        clock += 1
        workers = [x - 1 if x > 0 else 0 for x in workers]
        under_construction = {k: v - 1 for k, v in under_construction.items()}

    return clock - 1


def main():
    lines = read_input()

    part_1 = do_part_1(lines)
    print(f"{part_1=}")

    part_2 = do_part_2(lines)
    print(f"{part_2=}")


def read_input() -> list[str]:
    #     return """Step C must be finished before step A can begin.
    # Step C must be finished before step F can begin.
    # Step A must be finished before step B can begin.
    # Step A must be finished before step D can begin.
    # Step B must be finished before step E can begin.
    # Step D must be finished before step E can begin.
    # Step F must be finished before step E can begin.""".split(
    #         "\n"
    #     )
    with open("day07.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
