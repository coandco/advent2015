import time
from collections import defaultdict
from typing import Dict, List, NamedTuple

from utils import read_data


class Reindeer(NamedTuple):
    name: str
    speed: int
    uptime: int
    downtime: int

    @staticmethod
    def from_raw(raw: str) -> "Reindeer":
        r = raw.split()
        name, speed, uptime, downtime = r[0], int(r[3]), int(r[6]), int(r[13])
        return Reindeer(name, speed, uptime, downtime)

    def position_at(self, stop_time: int) -> int:
        cycle_time = self.uptime + self.downtime
        cycle_distance = self.uptime * self.speed
        num_cycles = stop_time // cycle_time
        remainder = stop_time % cycle_time
        remainder_uptime = remainder if remainder <= self.uptime else self.uptime
        return (num_cycles * cycle_distance) + (remainder_uptime * self.speed)


def get_winners(contestants: List[Reindeer], at: int) -> List[str]:
    scores = {x.name: x.position_at(at) for x in contestants}
    max_score = max(scores.values())
    return [k for k, v in scores.items() if v == max_score]


def score_race(contestants: List[Reindeer], stop_time: int = 2503):
    scores: Dict[str, int] = defaultdict(int)
    for i in range(1, stop_time + 1):
        for winner in get_winners(contestants, i):
            scores[winner] += 1
    return max(scores.values())


def main():
    contestants = [Reindeer.from_raw(x) for x in read_data().splitlines()]
    print(f"Part one: {max(x.position_at(2503) for x in contestants)}")
    print(f"Part two: {score_race(contestants)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
