import time
from collections import defaultdict
from itertools import permutations

from utils import read_data


def main():
    distances = defaultdict(dict)
    for line in read_data().splitlines():
        origin, _, destination, _, distance = line.split(" ")
        distances[origin][destination] = int(distance)
        distances[destination][origin] = int(distance)

    min_distance = 9999999999
    max_distance = 0
    for route in permutations(distances.keys()):
        distance = 0
        for start, finish in zip(route[:-1], route[1:]):
            distance += distances[start][finish]
        min_distance = min(min_distance, distance)
        max_distance = max(max_distance, distance)
    print(f"Part one: {min_distance}")
    print(f"Part two: {max_distance}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
