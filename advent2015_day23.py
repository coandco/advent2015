from typing import NamedTuple, Tuple, Union, Self

from utils import read_data
import time


class ProgramState(NamedTuple):
    a: int = 0
    b: int = 0
    pc: int = 0

    def execute(self, op: str, args: Tuple[Union[str, int], ...]) -> Self:
        if op == "hlf":
            return ProgramState(**(self._asdict() | {"pc": self.pc + 1, args[0]: getattr(self, args[0]) // 2}))
        elif op == "tpl":
            return ProgramState(**(self._asdict() | {"pc": self.pc + 1, args[0]: getattr(self, args[0]) * 3}))
        elif op == "inc":
            return ProgramState(**(self._asdict() | {"pc": self.pc + 1, args[0]: getattr(self, args[0]) + 1}))
        elif op == "jmp":
            return ProgramState(**(self._asdict() | {"pc": self.pc + int(args[0])}))
        elif op == "jie":
            if getattr(self, args[0]) % 2 == 0:
                return ProgramState(**(self._asdict() | {"pc": self.pc + int(args[1])}))
            return ProgramState(**(self._asdict() | {"pc": self.pc + 1}))
        elif op == "jio":
            if getattr(self, args[0]) == 1:
                return ProgramState(**(self._asdict() | {"pc": self.pc + int(args[1])}))
            return ProgramState(**(self._asdict() | {"pc": self.pc + 1}))
        raise Exception("Unknown op!")

def main():
    program = [x.split() for x in read_data().replace(",", "").splitlines()]
    curstate = ProgramState()
    while 0 <= curstate.pc < len(program):
        op, *args = program[curstate.pc]
        curstate = curstate.execute(op, args)
    print(f"Part one: {curstate.b}")
    curstate = ProgramState(a=1)
    while 0 <= curstate.pc < len(program):
        op, *args = program[curstate.pc]
        curstate = curstate.execute(op, args)
    print(f"Part two: {curstate.b}")



if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
