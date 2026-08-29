# Architecture

## Modern archival interface

The Python 3 code separates the stable parts of the project into small modules:

- `cube.py` validates a 54-sticker state and calls the optional Kociemba solver.
- `protocol.py` validates face-turn notation and converts each move to one byte.
- `controller.py` opens a serial port only after the caller requests execution.
- `cli.py` combines these parts and uses dry-run mode by default.

The interface has no camera dependency. This makes the protocol easy to review,
test, and demonstrate on a computer that has no robot attached.

## Safety boundary

Parsing and dry runs cannot open a serial port. Hardware access requires both
`--execute` and `--port`. This boundary prevents an accidental servo movement
during normal examples and automated tests.

## Legacy application

The original Python program contains the full camera pipeline and Tkinter UI.
It also creates global camera and UI resources at module load time. It remains
in `legacy/` as source material. It is not imported by the modern package.
