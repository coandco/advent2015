import time
from math import prod
from typing import Dict, Iterable, Tuple

from utils import read_data


def combinations(total: int, components: int) -> Iterable[Tuple[int, ...]]:
    if components == 1:
        yield (total,)
        return
    for i in range(total + 1):
        for j in combinations(total - i, components - 1):
            yield (i,) + j


def score_property(prop: Tuple[int, ...], combination: Tuple[int, ...]) -> int:
    return max(0, sum(x * combination[i] for i, x in enumerate(prop)))


def score_combination(properties: Dict[str, Tuple[int, ...]], combination: Tuple[int, ...]) -> int:
    return prod(score_property(x, combination) for name, x in properties.items() if name != "calories")


def main():
    ingredients = {}
    for line in read_data().splitlines():
        name, props = line.split(":")
        ingredients[name] = {x.split()[0]: int(x.split()[1]) for x in props.split(", ")}
    properties: Dict[str, Tuple[int, ...]] = {}
    # Since they all have the same properties, pick the first one and iterate through its properties
    for prop in next(iter(ingredients.values())):
        properties[prop] = tuple(x[prop] for x in ingredients.values())
    scores = {x: score_combination(properties, x) for x in combinations(100, len(ingredients))}
    print(f"Part one: {max(scores.values())}")
    print(f"Part two: {max(v for k, v in scores.items() if score_property(properties["calories"], k) == 500)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
