import time
from typing import List, Tuple, Iterable

from utils import read_data


class Rules:
    rules: List[Tuple[str, ...]]
    reversed_rules: List[Tuple[str, ...]]

    def __init__(self, raw_rules: str):
        unsorted_rules = [tuple(line.split(" => ")) for line in raw_rules.splitlines()]
        self.rules = sorted(unsorted_rules, key=lambda x: len(x[0]), reverse=True)
        self.reversed_rules = sorted(((y, x) for x, y in self.rules), key=lambda x: len(x[0]), reverse=True)


    def single_replacements(self, molecule: str, reverse: bool = False) -> Iterable[str]:
        for mfrom, mto in self.rules:
            if reverse:
                mfrom, mto = mto, mfrom
            parts = molecule.split(mfrom)
            for i in range(1, len(parts)):
                yield f"{mfrom.join(parts[:i])}{mto}{mfrom.join(parts[i:])}"

    def steps_to_target(self, target: str):
        # Try to replace the biggest chunk we can, one step at a time
        # Doesn't work for all possible inputs, but works for all AoC-generated ones
        steps = 0
        while target != "e":
            for mfrom, mto in self.reversed_rules:
                try:
                    loc = target.index(mfrom)
                    target = f"{target[:loc]}{mto}{target[loc+len(mfrom):]}"
                    break
                except ValueError:
                    continue
            steps += 1
        return steps


def main():
    raw_rules, molecule = read_data().split("\n\n")
    rules = Rules(raw_rules)
    print(f"Part one: {len(set(rules.single_replacements(molecule)))}")
    print(f"Part two: {rules.steps_to_target(molecule)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
