#define AO_PIN 2

void setup(){

  Serial.begin(115200);
  Serial.println("warming up the MQ2 sensor");
  delay(2000);

}

void loop(){
  int gasvalue = analogRead(AO_PIN);

Serial.print("MQ2 sensor AO value :");
Serial.println(gasvalue);
}