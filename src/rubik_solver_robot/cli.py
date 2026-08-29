"""Command-line entry point for dry runs and explicit serial execution."""

import argparse
import sys

from .controller import SerialSettings, send_commands
from .cube import CubeStateError, solve_cube
from .protocol import MoveError, encode_solution, parse_solution


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Solve a cube or encode moves for the archived robot."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--solution", help="moves such as: R U R' U'")
    source.add_argument(
        "--cube-state",
        help="54 stickers in URFDLB order; whitespace is ignored",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="send commands to hardware; the default is a dry run",
    )
    parser.add_argument("--port", help="serial port, required with --execute")
    parser.add_argument("--baud", type=int, default=9600, help="serial baud rate")
    parser.add_argument(
        "--command-delay",
        type=float,
        default=0.05,
        help="seconds between serial bytes",
    )
    return parser


def run(args: argparse.Namespace) -> int:
    solution = args.solution if args.solution is not None else solve_cube(args.cube_state)
    moves = parse_solution(solution)
    commands = encode_solution(moves)

    print("Moves:", " ".join(moves) or "already solved")
    print("Commands:", " ".join(chr(command) for command in commands) or "none")

    if not args.execute:
        print("Mode: dry run (no serial data sent)")
        return 0

    if not args.port:
        raise ValueError("--port is required with --execute")
    if args.command_delay < 0:
        raise ValueError("--command-delay cannot be negative")

    settings = SerialSettings(
        port=args.port,
        baud_rate=args.baud,
        command_delay=args.command_delay,
    )
    send_commands(commands, settings)
    print(f"Mode: sent {len(commands)} command(s) to {args.port}")
    return 0


def main() -> int:
    try:
        return run(build_parser().parse_args())
    except (CubeStateError, MoveError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
