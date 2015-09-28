void setup() {
  // Maximum for the tinyduino
  Serial.begin(19200);
}

void loop() {
  int val1 = analogRead(0);
  int val2 = analogRead(1);
  Serial.print(val1);
  Serial.print(" ");
  Serial.print(val2);
  Serial.println("");
  delay(50);
}
