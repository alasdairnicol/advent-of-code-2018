#!/usr/bin/env python
from collections import Counter


def parse_claims(line):
    _, _, pos, dimensions = line.replace(":", "").split()
    x_str, y_str = pos.split(",")
    x, y = int(x_str), int(y_str)
    dim_x_str, dim_y_str = dimensions.split("x")
    dim_x, dim_y = int(dim_x_str), int(dim_y_str)
    return {(x + i, y + j) for i in range(dim_x) for j in range(dim_y)}


def do_part_1(claims):
    counter = Counter()
    for claim in claims:
        counter.update(claim)
    return len([k for k, v in counter.items() if v > 1])


def do_part_2(claims):
    fabric = {}
    claim_intact = set()
    for i, claim in enumerate(claims, 1):
        claim_intact.add(i)
        for point in claim:
            if point in fabric:
                claim_intact.discard(i)
                claim_intact.discard(fabric[point])
            else:
                fabric[point] = i
    return claim_intact.pop()


def main():
    lines = read_input()
    claims = [parse_claims(line) for line in lines]

    part_1 = do_part_1(claims)
    print(f"{part_1=}")

    part_2 = do_part_2(claims)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day03.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
