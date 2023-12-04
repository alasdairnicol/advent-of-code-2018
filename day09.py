#!/usr/bin/env python
from collections import deque


def find_max_score(num_players: int, last_marble: int) -> int:
    marbles = deque([0])
    scores = [0] * num_players
    player = 1

    for number in range(1, last_marble + 1):
        if number % 23 == 0:
            marbles.rotate(7)
            scores[player - 1] += number + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(number)

        player = player % num_players + 1

    return max(scores)


def main():
    input_string = read_input()
    words = input_string.split()
    num_players = int(words[0])
    last_marble = int(words[-2])

    part_1 = find_max_score(num_players, last_marble)
    print(f"{part_1=}")

    part_2 = find_max_score(num_players, last_marble * 100)
    print(f"{part_2=}")


def read_input() -> str:
    with open("day09.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
