from utils import read_data
import math


def paper_for_present(raw_present: str) -> int:
    l, w, h = (int(x) for x in raw_present.split("x"))
    return (2*l*w) + (2*w*h) + (2*h*l) + min(l*w, w*h, h*l)


def ribbon_for_present(raw_present: str) -> int:
    l, w, h = (int(x) for x in raw_present.split("x"))
    return (sum(sorted((l, w, h))[:2])*2) + l*w*h


def main():
    print(f"Part one: {sum(paper_for_present(x) for x in read_data().splitlines())}")
    print(f"Part two: {sum(ribbon_for_present(x) for x in read_data().splitlines())}")


if __name__ == '__main__':
    import time
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
