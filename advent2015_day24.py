import time
from itertools import combinations
from math import prod
from typing import List

from utils import read_data


# This doesn't do any verification to make sure it's possible to split the remaining packages
# equally, but it turns out that doesn't matter for my input
def smallest_passenger_group(packages: List[int], num_groups: int = 3) -> int:
    target = sum(packages) // num_groups
    for i in range(2, len(packages)):
        valid_combinations = [prod(x) for x in combinations(packages, i) if sum(x) == target]
        if valid_combinations:
            return min(valid_combinations)


def main():
    weights = [int(x) for x in read_data().splitlines()]
    print(f"Part one: {smallest_passenger_group(weights)}")
    print(f"Part two: {smallest_passenger_group(weights, num_groups=4)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
