import time
from collections import defaultdict
from itertools import permutations
from typing import Dict, List

from utils import read_data


def calc_value(people: Dict[str, Dict[str, int]], order: List[str]) -> int:
    happiness = 0
    for i, person in enumerate(order):
        left = order[(i - 1) % len(order)]
        right = order[(i + 1) % len(order)]
        happiness = happiness + people[person][left] + people[person][right]
    return happiness


def main():
    people = defaultdict(dict)
    for line in read_data().splitlines():
        host, _, sign, amount, _, _, _, _, _, _, neighbor = line.split()
        people[host][neighbor[:-1]] = int(amount) * (1 if sign == "gain" else -1)
    print(f"Part one: {max(calc_value(people, x) for x in permutations(people.keys()))}")
    other_people = list(people.keys())
    people["Clint"] = {x: 0 for x in other_people}
    for person in other_people:
        people[person]["Clint"] = 0
    print(f"Part two: {max(calc_value(people, x) for x in permutations(people.keys()))}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
