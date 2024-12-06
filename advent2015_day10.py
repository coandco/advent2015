from utils import read_data
import time
import re

REPEATED = re.compile(r'((.)\2*)')

def main():
    data = read_data().strip()
    for i in range(50):
        output = []
        for length, digit in REPEATED.findall(data):
            output.extend((len(length), int(digit)))
        data = ''.join(str(x) for x in output)
        if i == 39:
            print(f"Part one: {len(data)}")
    print(f"Part two: {len(data)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
