#!/usr/bin/env python
from collections import Counter, defaultdict


def manhattan_distance(pair1, pair2):
    return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])


def do_part_1(pairs: list[tuple[int, int]]) -> int:
    max_x = max(x for x, y in pairs)
    max_y = max(y for x, y in pairs)

    print(max_x, max_y)

    areas: defaultdict[tuple[int, int], int] = defaultdict(int)
    infinite_areas = set()

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            closest_points = set()
            min_distance = max_x + max_y
            for pair in pairs:
                distance = manhattan_distance((x, y), pair)
                if distance == min_distance:
                    closest_points.add(pair)
                elif distance < min_distance:
                    closest_points = set([pair])
                    min_distance = distance

            if len(closest_points) == 1:
                closest_point = closest_points.pop()
                areas[closest_point] += 1
                if x == 0 or y == 0 or x == max_x or y == max_y:
                    infinite_areas.add(closest_point)

    largest_area = max(
        area for pair, area in areas.items() if pair not in infinite_areas
    )
    return largest_area


def do_part_2(pairs: list[tuple[int, int]]) -> int:
    max_x = max(x for x, y in pairs)
    max_y = max(y for x, y in pairs)

    safe_region_size = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            total_distance = sum(manhattan_distance((x, y), pair) for pair in pairs)
            if total_distance < 10000:
                safe_region_size += 1
    return safe_region_size


def main():
    lines = read_input()
    pairs = [(int(x), int(y)) for x, y in (line.split(",") for line in lines)]

    part_1 = do_part_1(pairs)
    print(f"{part_1=}")

    part_2 = do_part_2(pairs)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day06.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
