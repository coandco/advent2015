import heapq
import re
import time
from typing import Iterable, List, NamedTuple, Self

from utils import read_data

DIGITS = re.compile(r"\d+")


class Gamestate(NamedTuple):
    total_spent: int
    boss_hp: int
    boss_atk: int
    player_turn: bool = True
    my_hp: int = 50
    my_armor: int = 0
    mana: int = 500
    shield: int = 0
    poison: int = 0
    recharge: int = 0

    def next_states(self, hard: bool = False) -> Iterable[Self]:
        state = self._asdict()
        if hard and self.player_turn:
            state["my_hp"] -= 1
            if state["my_hp"] <= 0:
                return
        # Next state will always have the opposite turn type
        state["player_turn"] = not state["player_turn"]
        armor_this_turn = False
        if state["poison"]:
            state["boss_hp"] -= 3
            state["poison"] -= 1
        if state["recharge"]:
            state["mana"] += 101
            state["recharge"] -= 1
        if state["shield"]:
            armor_this_turn = True
            state["shield"] -= 1
        if state["boss_hp"] <= 0:
            yield Gamestate(**state)
            return
        if self.player_turn:
            # If we can't cast a spell, we lose and it's a dead end
            if state["mana"] < 53:
                return
            # Cast Magic Missile
            spell_effects = {
                "mana": state["mana"] - 53,
                "boss_hp": state["boss_hp"] - 4,
                "total_spent": state["total_spent"] + 53,
            }
            yield Gamestate(**(state | spell_effects))
            # Cast Drain
            spell_effects = {
                "mana": state["mana"] - 73,
                "boss_hp": state["boss_hp"] - 2,
                "my_hp": state["my_hp"] + 2,
                "total_spent": state["total_spent"] + 73,
            }
            yield Gamestate(**(state | spell_effects))
            # Cast Shield
            if not state["shield"]:
                spell_effects = {"mana": state["mana"] - 113, "shield": 6, "total_spent": state["total_spent"] + 113}
                yield Gamestate(**(state | spell_effects))
            # Cast Poison
            if not state["poison"]:
                spell_effects = {"mana": state["mana"] - 173, "poison": 6, "total_spent": state["total_spent"] + 173}
                yield Gamestate(**(state | spell_effects))
            if not state["recharge"]:
                spell_effects = {"mana": state["mana"] - 229, "recharge": 5, "total_spent": state["total_spent"] + 229}
                yield Gamestate(**(state | spell_effects))
        else:
            state["my_hp"] -= state["boss_atk"] - (7 * armor_this_turn)
            yield Gamestate(**state)


def find_cheapest(boss_hp: int, boss_atk: int, hard: bool = False) -> int:
    heap: List[Gamestate] = [Gamestate(total_spent=0, boss_hp=boss_hp, boss_atk=boss_atk)]
    while True:
        curstate: Gamestate = heapq.heappop(heap)
        # Dead end if we lose
        if curstate.my_hp <= 0:
            continue
        # We should be guaranteed to have a minimum the first time we win, thanks to heapq
        if curstate.boss_hp <= 0:
            return curstate.total_spent
        for new_state in curstate.next_states(hard=hard):
            heapq.heappush(heap, new_state)


def main():
    boss_hp, boss_atk = (int(x) for x in DIGITS.findall(read_data()))
    print(f"Part one: {find_cheapest(boss_hp, boss_atk)}")
    print(f"Part two: {find_cheapest(boss_hp, boss_atk, hard=True)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
