from utils import read_data
import time

CORRECT_DATA = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

def main():
    canonical_sue_data = {(x := line.split(": "))[0]: int(x[1]) for line in CORRECT_DATA.splitlines()}
    sue_attrs = {}
    for line in read_data().splitlines():
        line = line.replace(":", "").replace(",", "")
        _, rawnum, k1, v1, k2, v2, k3, v3 = line.split()
        sue_attrs[int(rawnum)] = {k1: int(v1), k2: int(v2), k3: int(v3)}
    p1_sues = sue_attrs
    for compound, val in canonical_sue_data.items():
        p1_sues = {k: v for k, v in p1_sues.items() if compound not in v or v[compound] == val}
    print(f"Part one: {next(iter(p1_sues))}")
    p2_sues = sue_attrs
    for compound, val in canonical_sue_data.items():
        if compound in ("cats", "trees"):
            p2_sues = {k: v for k, v in p2_sues.items() if compound not in v or v[compound] > val}
        elif compound in ("pomeranians", "goldfish"):
            p2_sues = {k: v for k, v in p2_sues.items() if compound not in v or v[compound] < val}
        else:
            p2_sues = {k: v for k, v in p2_sues.items() if compound not in v or v[compound] == val}
    print(f"Part two: {next(iter(p2_sues))}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
