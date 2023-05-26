/*
   EMG Sensor Data Acquisition Code
   Author: Jaider Hoyos
   Platform: Arduino Mega
   Date: 26-05-2023

   This code reads analog values from an EMG (Electromyography) sensor connected to the right side 
   and prints them to the serial port. The EMG sensor measures muscle activity and provides an 
   analog signal that represents the detected electrical signals.

   To use this code, connect the EMG sensor to the designated pin on the right side of the Arduino 
   Mega. Ensure that the serial communication baud rate is set to 9600 in order to view the output 
   in the serial monitor.

   Note: Make sure to adjust the pin assignment (emgPin) according to your specific wiring 
   configuration.
*/
const byte numChars = 64;
char receivedChars[numChars];

boolean newData = false;


int emgPin = A1;  // EMG sensor pin (right side)

void setup() {
  Serial.begin(115200);  // Initialize serial communication
  Serial.println("<Arduino is ready>");
}

void loop() {
  int emgValue = analogRead(emgPin);
  delay(10);  // Delay for stability
  newData = true;
  replyToPython(emgValue);   
}




void replyToPython(int value) {
    if (newData == true) {
        Serial.print("<");
        Serial.print(value);
        Serial.println('>');
        newData = false;
    }
}