# Legacy audit notes

The `legacy/` directory preserves the original uploaded files without a code
rewrite. They show the complete prototype idea, but they are not a supported
runtime.

## Desktop application

- The file uses Python 2 `print` statements while importing Python 3 modules.
- Camera, GUI, solver, detection, and serial control share global state.
- The program creates a Tk root window and opens camera index 0 during import.
- The serial port is fixed to `COM5` at 9600 baud.
- Long hardware waits run in the same workflow as UI operations.
- Color detection uses fixed pixel regions, area limits, and HSV thresholds.
- The solve action refers to names that are not consistently defined.
- Dependencies and supported versions were not recorded.

## Arduino sketch

- At least one statement is missing a semicolon in the uploaded source.
- A function block near the end is not closed correctly.
- A lowercase `r` command calls the clockwise `R()` function.
- A one-byte variable is compared with the multi-character values `L2` and `R2`.
- The desktop code sends `5` and `6` for these half turns, but the sketch does
  not handle those bytes.
- The loop prints a value even when no new serial byte is available.
- Servo angles and delays are fixed for one physical assembly.

## Publication decision

The modern package gives the repository a safe demonstration path. The old files
remain useful as a historical record. Exact restoration of the camera UI and
mechanical behavior is outside the archive scope.
