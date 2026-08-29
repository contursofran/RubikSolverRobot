import unittest

from rubik_solver_robot.protocol import MoveError, encode_solution, parse_solution


class ProtocolTests(unittest.TestCase):
    def test_encodes_all_move_forms(self) -> None:
        solution = "F F' F2 B B' B2 U U' U2 D D' D2 L L' L2 R R' R2"
        self.assertEqual(encode_solution(solution), b"Ff1Bb2Uu3Dd4Ll5Rr6")

    def test_accepts_curly_prime_and_lowercase(self) -> None:
        self.assertEqual(parse_solution("r u’"), ["R", "U'"])

    def test_rejects_unsupported_notation(self) -> None:
        with self.assertRaisesRegex(MoveError, "unsupported"):
            encode_solution("R M U")

    def test_accepts_an_empty_solution(self) -> None:
        self.assertEqual(encode_solution(""), b"")


if __name__ == "__main__":
    unittest.main()
