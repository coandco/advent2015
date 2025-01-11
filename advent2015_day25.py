import re
import time

from utils import read_data

DIGITS = re.compile(r"\d+")


def xy_to_n(row: int, column: int) -> int:
    full_diagonals = sum(range(row + column - 1))
    return full_diagonals + column


def code_number_n(n: int) -> int:
    current = 20151125
    for _ in range(n - 1):
        current = (current * 252533) % 33554393
    return current


def main():
    row, column = (int(x) for x in DIGITS.findall(read_data()))
    print(f"Part one: {code_number_n(xy_to_n(row, column))}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
