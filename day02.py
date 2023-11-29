#!/usr/bin/env python
from collections import Counter
import itertools


def make_counters(boxes: list[str]) -> list[Counter[str]]:
    return [Counter(box) for box in boxes]


def do_part1(boxes: list[str]) -> int:
    counters = make_counters(boxes)
    num_pairs = len([c for c in counters if 2 in c.values()])
    num_triples = len([c for c in counters if 3 in c.values()])
    return num_pairs * num_triples


def boxes_are_similar(box1: str, box2: str) -> bool:
    return len([1 for (b1, b2) in zip(box1, box2) if b1 != b2]) == 1


def find_similar_boxes(boxes: list[str]) -> tuple[str, str]:
    for box1, box2 in itertools.combinations(boxes, 2):
        if boxes_are_similar(box1, box2):
            return box1, box2

    raise ValueError("No similar boxes found")


def do_part_2(boxes: list[str]) -> str:
    box1, box2 = find_similar_boxes(boxes)
    return "".join(b1 for (b1, b2) in zip(box1, box2) if b1 == b2)


def main():
    boxes = [line.rstrip("\n") for line in read_input()]
    counters = make_counters(boxes)

    part_1 = do_part1(counters)
    print(f"{part_1=}")

    part_2 = do_part_2(boxes)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day02.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
