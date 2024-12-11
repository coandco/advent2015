import time
from typing import Dict, Optional, Set

from utils import BaseCoord as Coord
from utils import read_data


def step(grid: Dict[Coord, bool], stuck_lights: Optional[Set[Coord]] = None) -> Dict[Coord, bool]:
    if stuck_lights is None:
        stuck_lights = set()
    new_grid = {}
    for loc, is_lit in grid.items():
        if loc in stuck_lights:
            new_grid[loc] = True
            continue
        num_neighbors = sum(grid.get(x, False) for x in loc.neighbors())
        if is_lit and num_neighbors not in (2, 3):
            new_grid[loc] = False
        elif (not is_lit) and num_neighbors == 3:
            new_grid[loc] = True
        else:
            new_grid[loc] = is_lit
    return new_grid


def main():
    grid = {}
    x = y = 0
    for y, line in enumerate(read_data().splitlines()):
        for x, char in enumerate(line):
            grid[Coord(x=x, y=y)] = char == "#"

    p1_grid = grid
    for _ in range(100):
        p1_grid = step(p1_grid)
    print(f"Part one: {sum(p1_grid.values())}")

    p2_grid = grid
    stuck_lights = {Coord(0, 0), Coord(x=x, y=0), Coord(x=0, y=y), Coord(x=x, y=y)}
    for loc in stuck_lights:
        p2_grid[loc] = True
    for _ in range(100):
        p2_grid = step(p2_grid, stuck_lights)
    print(f"Part two: {sum(p2_grid.values())}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
