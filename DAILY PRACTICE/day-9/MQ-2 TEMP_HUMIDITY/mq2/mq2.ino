#define MQ2_PIN 34        
#define GAS_THRESHOLD 800   

void setup() {
  Serial.begin(115200);     
  pinMode(MQ2_PIN, INPUT);
  Serial.println("MQ2 Sensor Warming Up...");
}

void loop() {
    int gasValue = analogRead(MQ2_PIN);

  Serial.print("Sensor Value: ");
  Serial.println(gasValue);

  if (gasValue > GAS_THRESHOLD) {
    Serial.println("WARNING: Gas/Smoke Detected!");
  } else {
    Serial.println("Status: Normal");
  }

  delay(1000); 
}

