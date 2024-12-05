import itertools
from typing import List

from utils import read_data
import time
import re

LINE = re.compile(r'(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)')

OPS = {
    "v1": {
        "turn on": lambda x: 1,
        "turn off": lambda x: 0,
        "toggle": lambda x: 1 if x == 0 else 0
    },
    "v2": {
        'turn on': lambda x: x + 1,
        'turn off': lambda x: max(0, x - 1),
        'toggle': lambda x: x + 2
    }
}

def apply_instructions(instructions: List[str], version: str = "v1") -> int:
    grid: List[List[int]] = [[0] * 1000 for _ in range(1000)]
    for instruction in instructions:
        type, *corners = LINE.match(instruction).groups()
        x1, y1, x2, y2 = (int(x) for x in corners)
        xrange = range(min(x1, x2), max(x1, x2) + 1)
        yrange = range(min(y1, y2), max(y1, y2) + 1)
        for y in yrange:
            for x in xrange:
                grid[y][x] = OPS[version][type](grid[y][x])
    return sum(itertools.chain.from_iterable(grid))

def main():
    instructions = read_data().splitlines()
    print(f"Part one: {apply_instructions(instructions, version="v1")}")
    print(f"Part two: {apply_instructions(instructions, version="v2")}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
