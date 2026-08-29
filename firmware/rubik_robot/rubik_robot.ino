// RubikSolverRobot serial protocol test firmware.
//
// This sketch does not attach servos or move hardware. It lets you verify the
// desktop command stream before you restore and calibrate the legacy motion
// code.

const long SERIAL_BAUD_RATE = 9600;
const char VALID_COMMANDS[] = "Ff1Bb2Uu3Dd4Ll5Rr6S";

bool isValidCommand(char command) {
  for (unsigned int index = 0; index < sizeof(VALID_COMMANDS) - 1; ++index) {
    if (VALID_COMMANDS[index] == command) {
      return true;
    }
  }
  return false;
}

void setup() {
  Serial.begin(SERIAL_BAUD_RATE);
  Serial.println("READY RubikSolverRobot protocol test");
}

void loop() {
  if (Serial.available() <= 0) {
    return;
  }

  const char command = Serial.read();
  if (!isValidCommand(command)) {
    Serial.print("ERR ");
    Serial.println(command);
    return;
  }

  Serial.print("ACK ");
  Serial.println(command);
}
