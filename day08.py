#!/usr/bin/env python
from collections.abc import Iterator
from typing import Callable


def main():
    input_string = read_input()
    numbers = [int(x) for x in input_string.split()]

    part_1 = calc_node_score(iter(numbers), score_part_1)
    print(f"{part_1=}")

    part_2 = calc_node_score(iter(numbers), score_part_2)
    print(f"{part_2=}")


def score_part_1(children: list[int], metadata: list[int]) -> int:
    return sum(children) + sum(metadata)


def score_part_2(children: list[int], metadata: list[int]) -> int:
    if children:
        value = sum(children[x - 1] if x <= len(children) else 0 for x in metadata)
    else:
        value = sum(metadata)
    return value


def calc_node_score(
    stream: Iterator[int], score_fn: Callable[[list[int], list[int]], int]
) -> int:
    num_children = next(stream)
    metadata_len = next(stream)
    children = [calc_node_score(stream, score_fn) for _ in range(num_children)]
    metadata = [next(stream) for _ in range(metadata_len)]
    return score_fn(children, metadata)


def read_input() -> str:
    with open("day08.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
