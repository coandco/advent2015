from typing import Set

from utils import read_data, BaseCoord as Coord


OFFSETS = {
    "^": Coord(x=0, y=-1),
    ">": Coord(x=1, y=0),
    "v": Coord(x=0, y=1),
    "<": Coord(x=-1, y=0)
}


def total_houses(raw_input: str, robo_santa: bool = False) -> int:
    houses: Set[Coord] = {Coord(0, 0)}
    santa_loc = robo_loc = Coord(0, 0)
    for i, char in enumerate(raw_input):
        if i % 2 == 0 or not robo_santa:
            santa_loc = santa_loc + OFFSETS[char]
            houses.add(santa_loc)
        else:
            robo_loc = robo_loc + OFFSETS[char]
            houses.add(robo_loc)
    return len(houses)


def main():
    print(f"Part one: {total_houses(read_data())}")
    print(f"Part two: {total_houses(read_data(), robo_santa=True)}")


if __name__ == '__main__':
    import time
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
