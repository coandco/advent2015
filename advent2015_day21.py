from itertools import combinations
from typing import NamedTuple, Self, Iterable, Tuple
from utils import read_data
import time
import re

DIGITS = re.compile(r"\d+")


class Equipment(NamedTuple):
    name: str
    cost: int
    atk: int
    def_: int

    @classmethod
    def from_raw(cls, line: str) -> Self:
        name, cost, atk, def_ = line.split()
        return cls(name, int(cost), int(atk), int(def_))


RAW_WEAPONS = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""
WEAPONS = [Equipment.from_raw(x) for x in RAW_WEAPONS.splitlines()]

RAW_ARMOR = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""
ARMOR = [Equipment.from_raw(x) for x in RAW_ARMOR.splitlines()]

RAW_RINGS = """Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""
RINGS = [Equipment.from_raw(x) for x in RAW_RINGS.splitlines()]


class Combatant(NamedTuple):
    hp: int
    atk: int
    def_: int

    def take_hit(self, other: Self) -> Self:
        return Combatant(hp=self.hp - (other.atk - self.def_), atk=self.atk, def_=self.def_)


def ring_combinations() -> Iterable[Tuple[Equipment, ...]]:
    yield tuple()
    for ring in RINGS:
        yield (ring,)
    for combination in combinations(RINGS, 2):
        yield combination


def armor_combinations() -> Iterable[Tuple[Equipment, ...]]:
    yield tuple()
    for piece in ARMOR:
        yield (piece,)


def all_combinations() -> Iterable[Tuple[int, int, int]]:
    for weapon in WEAPONS:
        for armor_combo in armor_combinations():
            for ring_combo in ring_combinations():
                combo = (weapon,) + armor_combo + ring_combo
                yield sum(x.cost for x in combo), sum(x.atk for x in combo), sum(x.def_ for x in combo)


def run_sim(me: Combatant, boss: Combatant) -> bool:
    while me.hp > 0:
        boss = boss.take_hit(me)
        if boss.hp <= 0:
            return True
        me = me.take_hit(boss)
    return False


def find_cheapest_win(boss: Combatant) -> int:
    cheapest_combos = sorted(all_combinations())
    for cost, atk, def_ in cheapest_combos:
        if run_sim(Combatant(100, atk, def_), boss):
            return cost


def find_costly_win(boss: Combatant) -> int:
    expensive_combos = sorted(all_combinations(), reverse=True)
    for cost, atk, def_ in expensive_combos:
        if not run_sim(Combatant(100, atk, def_), boss):
            return cost


def main():
    boss = Combatant(*(int(x) for x in DIGITS.findall(read_data())))
    print(f"Part one: {find_cheapest_win(boss)}")
    print(f"Part two: {find_costly_win(boss)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
