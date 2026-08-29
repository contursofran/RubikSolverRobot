"""Cube-state validation and optional Kociemba solving."""

from collections import Counter

FACE_ORDER = "URFDLB"
SOLVED_STATE = "".join(face * 9 for face in FACE_ORDER)


class CubeStateError(ValueError):
    """The supplied sticker state is not valid for the solver."""


def validate_cube_state(state: str) -> str:
    """Return a normalized 54-sticker state or raise ``CubeStateError``.

    This validates the format and color counts. The Kociemba solver performs
    the remaining cubie-orientation and permutation checks.
    """

    normalized = "".join(state.split()).upper()
    if len(normalized) != 54:
        raise CubeStateError("cube state must contain exactly 54 stickers")

    invalid = sorted(set(normalized) - set(FACE_ORDER))
    if invalid:
        raise CubeStateError(
            "cube state contains invalid face symbols: " + ", ".join(invalid)
        )

    counts = Counter(normalized)
    wrong_counts = [face for face in FACE_ORDER if counts[face] != 9]
    if wrong_counts:
        details = ", ".join(f"{face}={counts[face]}" for face in wrong_counts)
        raise CubeStateError(f"each face symbol must occur 9 times ({details})")

    centers = "".join(normalized[index] for index in (4, 13, 22, 31, 40, 49))
    if centers != FACE_ORDER:
        raise CubeStateError(
            f"center stickers must follow URFDLB order (received {centers})"
        )

    return normalized


def solve_cube(state: str) -> str:
    """Solve a validated cube state with the optional ``kociemba`` package."""

    normalized = validate_cube_state(state)
    if normalized == SOLVED_STATE:
        return ""

    try:
        import kociemba
    except ImportError as error:
        raise RuntimeError(
            "the solver dependency is missing; install with: "
            "python -m pip install -e '.[solver]'"
        ) from error

    try:
        return str(kociemba.solve(normalized))
    except ValueError as error:
        raise CubeStateError(f"the cube state is not solvable: {error}") from error
