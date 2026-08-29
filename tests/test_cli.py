import argparse
import contextlib
import io
import unittest
from unittest.mock import patch

from rubik_solver_robot.cli import run


def arguments(**overrides: object) -> argparse.Namespace:
    values: dict[str, object] = {
        "solution": "R U' F2",
        "cube_state": None,
        "execute": False,
        "port": None,
        "baud": 9600,
        "command_delay": 0.05,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class CliTests(unittest.TestCase):
    @patch("rubik_solver_robot.cli.send_commands")
    def test_dry_run_does_not_send_serial_data(self, send_commands) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = run(arguments())

        self.assertEqual(result, 0)
        send_commands.assert_not_called()
        self.assertIn("Mode: dry run", output.getvalue())

    @patch("rubik_solver_robot.cli.send_commands")
    def test_execute_sends_encoded_commands(self, send_commands) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = run(arguments(execute=True, port="TEST_PORT"))

        self.assertEqual(result, 0)
        sent_commands, settings = send_commands.call_args.args
        self.assertEqual(sent_commands, b"Ru1")
        self.assertEqual(settings.port, "TEST_PORT")

    @patch("rubik_solver_robot.cli.send_commands")
    def test_execute_requires_a_port(self, send_commands) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(ValueError, "--port"):
                run(arguments(execute=True))
        send_commands.assert_not_called()


if __name__ == "__main__":
    unittest.main()
