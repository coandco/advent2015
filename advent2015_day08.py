import time

from utils import read_data


def main():
    literal_count = mem_count = expanded_count = 0
    for line in read_data().splitlines():
        literal_count += len(line)
        mem_count += len(eval(line))
        expanded_count += len(f'"{line.replace('\\', '\\\\').replace('"', r'\"')}"')
    print(f"Part one: {literal_count - mem_count}")
    print(f"Part two: {expanded_count - literal_count}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
