"""Conversion from cube notation to the prototype's serial protocol."""

import re
from collections.abc import Iterable

MOVE_PATTERN = re.compile(r"^[URFDLB](?:2|')?$")

COMMANDS = {
    "F": "F",
    "F'": "f",
    "F2": "1",
    "B": "B",
    "B'": "b",
    "B2": "2",
    "U": "U",
    "U'": "u",
    "U2": "3",
    "D": "D",
    "D'": "d",
    "D2": "4",
    "L": "L",
    "L'": "l",
    "L2": "5",
    "R": "R",
    "R'": "r",
    "R2": "6",
}


class MoveError(ValueError):
    """The solution contains notation that the robot cannot execute."""


def parse_solution(solution: str | Iterable[str]) -> list[str]:
    """Normalize and validate a solution in standard face-turn notation."""

    raw_moves = solution.split() if isinstance(solution, str) else list(solution)
    moves = [move.strip().upper().replace("’", "'") for move in raw_moves]
    invalid = [move for move in moves if not MOVE_PATTERN.fullmatch(move)]
    if invalid:
        raise MoveError("unsupported cube move(s): " + ", ".join(invalid))
    return moves


def encode_solution(solution: str | Iterable[str]) -> bytes:
    """Encode a solution as the one-byte commands used by the prototype."""

    return "".join(COMMANDS[move] for move in parse_solution(solution)).encode("ascii")
