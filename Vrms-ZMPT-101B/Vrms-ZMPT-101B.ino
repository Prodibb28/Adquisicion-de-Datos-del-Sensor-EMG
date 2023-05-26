#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

float sigmaVolt=0;
float sigmaCurr=0;
float fp=0;
float P=0;
float S=0;
float voltage=0; 
float voltajeSensor=0;
float corriente=0;
unsigned long tiempo=0;
unsigned long period=200;
int sample=0;
float sigma=0;
void setup() {

  cbi(ADCSRA, ADPS2);
  sbi(ADCSRA, ADPS1);
  sbi(ADCSRA, ADPS0);
 Serial.begin(115200);  
}

void loop() {
  P=0;
  S=0;
  sigmaVolt=0;
  sigmaCurr=0;
  voltage =0;
  sample=0;
  sigma=0;
  tiempo=millis();
  while(millis()-tiempo<period)//Duración 0.5 segundos(Aprox. 30 ciclos de 60Hz)
  { 
  getVnC();
  P+=voltage*corriente;

  sigmaVolt += sq(voltage);
  sigmaCurr += sq(corriente);
  sample++; 
  }
 
  voltage = sqrt((sigmaVolt)/sample);
  corriente = sqrt((sigmaCurr)/sample);
  P=abs(P/sample);
  S=voltage*corriente;
  fp=P/S;
  Serial.println("PA: " + String(S) + " - PR: " +String(P)+ " - fp: " +String(fp));
}
void getVnC(){
  voltage = (analogRead(A1)- 511.5);

  voltajeSensor = analogRead(A0) * (5 / 1023.0); //voltaje del sensor
  corriente=(voltajeSensor-2.5)*1.45; //corriente=VoltajeSensor*(30A/1V)
}
