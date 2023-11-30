#!/usr/bin/env python
from collections import Counter, defaultdict


def do_part_1(minutes_slept_by_guard: defaultdict) -> int:
    total_minutes_slept = Counter(
        {
            guard_id: sum(minutes_slept.values())
            for guard_id, minutes_slept in minutes_slept_by_guard.items()
        }
    )
    sleepiest_guard_id = total_minutes_slept.most_common(1)[0][0]
    sleepiest_minute = minutes_slept_by_guard[sleepiest_guard_id].most_common(1)[0][0]

    return sleepiest_guard_id * sleepiest_minute


def do_part_2(minutes_slept_by_guard: defaultdict) -> int:
    sleepiest_minute_by_guard = {
        guard_id: minutes_slept.most_common(1)[0]
        for guard_id, minutes_slept in minutes_slept_by_guard.items()
    }
    guard_id, (minute, _) = max(sleepiest_minute_by_guard.items(), key=lambda x: x[0])
    return guard_id * minute


def process_lines(lines: list[str]) -> defaultdict:
    minutes_slept_by_guard: defaultdict = defaultdict(lambda: Counter())

    for line in lines:
        current_minute = int(line[15:17])
        if "begins shift" in line:
            current_guard = int(line.split()[3][1:])
            hours = int(line[12:14])
            if hours == 0:
                start_minute = current_minute
            else:
                start_minute = 0
        elif "falls asleep" in line:
            start_minute = current_minute
        elif "wakes up" in line:
            minutes_slept_by_guard[current_guard].update(
                {minute: 1 for minute in range(start_minute, current_minute)}
            )
        else:
            raise ValueError(f"Invalid Line: {line}")

    return minutes_slept_by_guard


def main():
    lines = sorted(line.strip() for line in read_input())

    minutes_slept_by_guard = process_lines(lines)

    part_1 = do_part_1(minutes_slept_by_guard)
    print(f"{part_1=}")

    part_2 = do_part_2(minutes_slept_by_guard)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day04.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
