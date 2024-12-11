import time
from collections import deque
from typing import Deque, FrozenSet, List, Set

from utils import read_data


def find_combinations(containers: List[int], target: int) -> Set[FrozenSet[int]]:
    successes: Set[FrozenSet[int]] = set()
    stack: Deque[FrozenSet[int]] = deque([frozenset({x}) for x in range(len(containers))])
    while stack:
        combination = stack.pop()
        value = sum(containers[i] for i in combination)
        for i in (x for x in range(len(containers)) if x not in combination):
            if value + containers[i] > target:
                continue
            if value + containers[i] == target:
                successes.add(combination | {i})
                continue
            stack.append(combination | {i})
    return successes


def main():
    containers = [int(x) for x in read_data().splitlines()]
    exactly_150_ways = find_combinations(containers, 150)
    print(f"Part one: {len(exactly_150_ways)}")
    min_containers = min(len(x) for x in exactly_150_ways)
    print(f"Part two: {len([x for x in exactly_150_ways if len(x) == min_containers])}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
