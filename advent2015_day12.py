from utils import read_data
import time
import re
import json

DIGITS = re.compile(r'-?\d+')

def prune(data):
    if isinstance(data, dict):
        if "red" in data.values():
            for key in list(data.keys()):
                del data[key]
            return
        for k, v in data.items():
            if type(v) in (dict, list):
                prune(v)
    elif isinstance(data, list):
        for item in data:
            if type(item) in (dict, list):
                prune(item)

def main():
    print(f"Part one: {sum(int(x) for x in DIGITS.findall(read_data()))}")
    data = json.loads(read_data())
    prune(data)
    print(f"Part two: {sum(int(x) for x in DIGITS.findall(json.dumps(data)))}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
