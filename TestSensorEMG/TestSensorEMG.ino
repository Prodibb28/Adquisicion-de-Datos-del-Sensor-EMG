int emgPin = A1;
int emgValue = 0;

void setup() {
  Serial.begin(9600);

}

void loop() {
 emgValue = analogRead(emgPin);
 Serial.println(emgValue);
 delay(10);
}
