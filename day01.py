#!/usr/bin/env python
import itertools


def parse_frequency_changes(frequency_strings: list[str]) -> list[int]:
    return [int(num) for num in frequency_strings]


def find_repeated_frequencies(frequency_changes: list[int]) -> int:
    seen_frequences = set()
    current_frequency = 0
    for frequency_change in itertools.cycle(frequency_changes):
        current_frequency += frequency_change
        if current_frequency in seen_frequences:
            return current_frequency
        seen_frequences.add(current_frequency)
    raise ValueError("No repeated frequencies found")



def main():
    frequency_changes = parse_frequency_changes(read_input())

    part_1 = sum(frequency_changes)
    print(f"{part_1=}")

    part_2 = find_repeated_frequencies(frequency_changes)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day01.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
