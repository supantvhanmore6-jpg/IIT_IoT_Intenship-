void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; 
  }
  Serial.println("UART Initialized...");
}
void loop() {
  Serial.println("Hello World");
  delay(2000);
}
