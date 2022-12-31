from typing import Iterable

from utils import read_data


def running_sum(raw_input: str) -> Iterable[int]:
    current = 0
    for char in raw_input:
        current += 1 if char == '(' else -1
        yield current


def main():
    *_, last = running_sum(read_data())
    print(f"Part one: {last}")
    print(f"Part two: {next(i for i, x in enumerate(running_sum(read_data()), start=1) if x < 0)}")


if __name__ == '__main__':
    import time
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
