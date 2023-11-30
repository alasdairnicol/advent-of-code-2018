#!/usr/bin/env python
from collections import deque
import string


def do_part_1(polymer: str) -> int:
    return react_polymer(polymer)


def do_part_2(polymer: str) -> int:
    return min(
        react_polymer(polymer.replace(letter, "").replace(letter.upper(), ""))
        for letter in string.ascii_lowercase
    )


def react_polymer(polymer: str) -> int:
    left: deque = deque()
    right = deque(polymer)

    while right:
        if not left:
            left.extend(right.popleft())
        elif left[-1] != right[0] and left[-1].upper() == right[0].upper():
            left.pop()
            right.popleft()
        else:
            left.extend(right.popleft())
    return len(left)


def main():
    polymer = read_input()

    part_1 = do_part_1(polymer)
    print(f"{part_1=}")

    part_2 = do_part_2(polymer)
    print(f"{part_2=}")


def read_input() -> str:
    with open("day05.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
