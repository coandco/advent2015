from collections import Counter

from utils import read_data
import time
import re

P1_DOUBLE = re.compile(r'.*(.)\1')
P1_BANNED = re.compile(r'.*(ab|cd|pq|xy)')
P2_TWOPAIR = re.compile(r'.*(..).*\1')
P2_REPEAT = re.compile(r'.*(.).\1')

def validate_p1(string: str) -> bool:
    counts = Counter(string)
    if (sum(counts[x] for x in 'aeiou') < 3) or P1_BANNED.match(string) or not P1_DOUBLE.match(string):
        return False
    return True

def validate_p2(string: str) -> bool:
    return bool(P2_TWOPAIR.match(string)) and bool(P2_REPEAT.match(string))


def main():
    strings = read_data().splitlines()
    print(f"Part one: {sum(validate_p1(x) for x in strings)}")
    print(f"Part two: {sum(validate_p2(x) for x in strings)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
