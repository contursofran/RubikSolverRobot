"""Explicit serial execution for robot commands."""

from dataclasses import dataclass
from time import sleep


@dataclass(frozen=True)
class SerialSettings:
    port: str
    baud_rate: int = 9600
    timeout: float = 2.0
    command_delay: float = 0.05


def send_commands(commands: bytes, settings: SerialSettings) -> None:
    """Send commands to the robot after the caller explicitly selects a port."""

    if not settings.port.strip():
        raise ValueError("a serial port is required for hardware execution")

    try:
        import serial
    except ImportError as error:
        raise RuntimeError(
            "the serial dependency is missing; install with: "
            "python -m pip install -e '.[hardware]'"
        ) from error

    with serial.Serial(
        settings.port,
        settings.baud_rate,
        timeout=settings.timeout,
    ) as connection:
        for command in commands:
            connection.write(bytes((command,)))
            connection.flush()
            sleep(settings.command_delay)
