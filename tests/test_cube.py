import unittest

from rubik_solver_robot.cube import (
    SOLVED_STATE,
    CubeStateError,
    solve_cube,
    validate_cube_state,
)


class CubeStateTests(unittest.TestCase):
    def test_accepts_solved_state(self) -> None:
        self.assertEqual(validate_cube_state(SOLVED_STATE), SOLVED_STATE)

    def test_solved_state_needs_no_moves_or_optional_dependency(self) -> None:
        self.assertEqual(solve_cube(SOLVED_STATE), "")

    def test_removes_whitespace_and_normalizes_case(self) -> None:
        spaced = "\n".join(
            SOLVED_STATE[index : index + 9].lower()
            for index in range(0, 54, 9)
        )
        self.assertEqual(validate_cube_state(spaced), SOLVED_STATE)

    def test_rejects_wrong_length(self) -> None:
        with self.assertRaisesRegex(CubeStateError, "exactly 54"):
            validate_cube_state(SOLVED_STATE[:-1])

    def test_rejects_wrong_symbol_count(self) -> None:
        with self.assertRaisesRegex(CubeStateError, "must occur 9 times"):
            validate_cube_state("R" + SOLVED_STATE[1:])

    def test_rejects_wrong_center_order(self) -> None:
        stickers = list(SOLVED_STATE)
        stickers[4], stickers[13] = stickers[13], stickers[4]
        with self.assertRaisesRegex(CubeStateError, "center stickers"):
            validate_cube_state("".join(stickers))


if __name__ == "__main__":
    unittest.main()
