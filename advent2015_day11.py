import string

from utils import read_data
import time

STRAIGHTS = string.ascii_lowercase


def _increment(char: str) -> str:
    # ascii 'a' is 97, so we subtract 97 to make it 0, increment it, wrap it, and shift it back up
    return chr(((ord(char) - 97 + 1) % 26) + 97)

def increment(password: str) -> str:
    exploded = [x for x in password]
    for i in reversed(range(len(password))):
        exploded[i] = _increment(exploded[i])
        if exploded[i] != 'a':
            break
    return ''.join(exploded)

def validate(password: str) -> bool:
    prev = prev_prev = '\0'
    pairs = set()
    seen_straight = False
    for char in password:
        if char in ('i', 'o', 'l'):
            return False
        if char == prev and char not in pairs:
            pairs.add(char)
        if ord(char) == (ord(prev)+1) and (ord(prev) == (ord(prev_prev)+1)):
            seen_straight = True
        prev_prev = prev
        prev = char
    return seen_straight and len(pairs) >= 2


def main():
    password = read_data().strip()
    while not validate(password):
        password = increment(password)
    print(f"Part one: {password}")
    password = increment(password)
    while not validate(password):
        password = increment(password)
    print(f"Part two: {password}")



if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
