// pyserialcom.ino
// Arduino side of the sound-triggered sprayer. Listens on the serial port
// for 'K' (knock -> swing the hammer) and 'S' (spray -> flash the LED).

int LedPin = 7;
int HammerPin = 8;
bool flag = false;
int freq = 20;
String inByte;

void setup() {
  Serial.begin(9600);
  Serial.println("Ready!");

  pinMode(LedPin, OUTPUT);
  digitalWrite(LedPin, LOW);

  pinMode(HammerPin, OUTPUT);
  digitalWrite(HammerPin, LOW);
}

// .toInt()
// Serial.read() => int

void loop() {
  // Read one incoming serial command if any bytes are waiting.
  if (Serial.available() > 0) {
    // String inByte = Serial.readStringUntil('\n');
    String inByte = Serial.readString();
    Serial.println(inByte);

    // Knock signal: swing the hammer once.
    if (inByte == "K") {
      flag = true;
    }

    if (flag == true) {
      digitalWrite(HammerPin, HIGH);
      delay(freq);
      digitalWrite(HammerPin, LOW);
      delay(freq);
      flag = false;
    }

    // Spray signal: flash the LED twice.
    if (inByte == "S") {
      Serial.println("Spray!");
      digitalWrite(LedPin, HIGH);
      delay(200);
      digitalWrite(LedPin, LOW);
      delay(200);
    }

    if (inByte == "U") {
      Serial.print("Unspray!");
    }

    /*
    unsigned long now = millis ();
    while (millis () - now < 1000)
    {
      Serial.read();
    }
    */
    Serial.flush();
  }
}
