from utils import read_data
from hashlib import md5


def mine(prefix: str, num_zeroes: int = 5) -> int:
    to_test = 1
    while True:
        if md5(f"{prefix}{to_test}".encode('utf-8')).hexdigest()[:num_zeroes] == "0" * num_zeroes:
            break
        to_test += 1
    return to_test


def main():
    print(f"Part one: {mine(read_data(), num_zeroes=5)}")
    print(f"Part two: {mine(read_data(), num_zeroes=6)}")


if __name__ == '__main__':
    import time
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
