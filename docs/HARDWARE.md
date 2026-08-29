# Hardware notes

## Historical setup

The source indicates that the prototype used:

- an Arduino-compatible board;
- two hobby servos on pins 3 and 4;
- a USB webcam;
- a serial connection at 9600 baud;
- a mechanical arm that pushes and holds the cube;
- a rotating base that changes cube orientation.

The repository does not include a bill of materials, wiring diagram, CAD files,
or servo specifications. Do not infer electrical limits from the source code.

## Safe test sequence

1. Disconnect servo power.
2. Upload the protocol test sketch from `firmware/rubik_robot/`.
3. Run the Python CLI without `--execute` and inspect its command output.
4. Connect to the test sketch and confirm the `ACK` lines in the serial monitor.
5. Review the original motion code in `legacy/arduino_moves.ino`.
6. Restore motion one operation at a time and calibrate mechanical limits.
7. Keep the cube and hands clear during powered tests.

## Firmware status

The modern sketch validates the serial protocol only. It does not attach servos
or move the mechanism. The old sketch contains the historical motion sequences,
but it has known compile and command-dispatch defects. It needs repair and
hardware-specific calibration before use.
