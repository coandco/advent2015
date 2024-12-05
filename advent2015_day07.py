from typing import NamedTuple, List, Optional, Tuple, Dict

from utils import read_data
import time


class Connection(NamedTuple):
    name: str
    prereqs: List[str]
    op: Optional[str]
    args: List[str]


def parse_line(line: str) -> Tuple[str, Connection]:
    raw_expr, name = line.split(" -> ")
    expr = raw_expr.split(" ")
    if len(expr) == 1:
        op = "ASSIGN"
        args = [expr[0]]
    elif len(expr) == 2:  # Means this is a NOT
        op = expr[0]
        args = [expr[1]]
    elif len(expr) == 3:
        op = expr[1]
        args = [expr[0], expr[2]]
    else:
        raise Exception(f"bad line length: {line}")
    prereqs = [x for x in args if not x.isdigit()]
    return name, Connection(name, prereqs, op, args)


def resolve_known(known: Dict[str, int], connection: Connection) -> int:
    def resolve_val(val: str) -> int:
        return int(val) if val.isdigit() else known[val]

    args = connection.args
    if connection.op == "ASSIGN":
        return resolve_val(args[0])
    if connection.op == "AND":
        return resolve_val(args[0]) & resolve_val(args[1])
    elif connection.op == "OR":
        return resolve_val(args[0]) | resolve_val(args[1])
    elif connection.op == "NOT":
        return ~resolve_val(args[0])
    elif connection.op == "LSHIFT":
        return resolve_val(args[0]) << resolve_val(args[1])
    elif connection.op == "RSHIFT":
        return resolve_val(args[0]) >> resolve_val(args[1])
    else:
        raise Exception(f"Unknown op {connection.op}")


def resolve_connections(connections: Dict[str, Connection]) -> int:
    connections = connections.copy()
    known_connections = {}
    while connections:
        to_drop = []
        for name, connection in connections.items():
            if all(x in known_connections for x in connection.prereqs):
                known_connections[name] = resolve_known(known_connections, connection)
                to_drop.append(name)
        for name in to_drop:
            del connections[name]
    return known_connections["a"]


def main():
    connections = {}
    for line in read_data().splitlines():
        name, connection = parse_line(line)
        connections[name] = connection
    signal_a = resolve_connections(connections)
    print(f"Part 1: {signal_a}")
    connections["b"] = Connection(name="b", prereqs=[], op="ASSIGN", args=[str(signal_a)])
    print(f"Part 2: {resolve_connections(connections)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
