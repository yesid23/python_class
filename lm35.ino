//declaro variable para guardar temoperatura en celcius
float tempC;
//declaro variable para el pin A0
int pinSensorT = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
tempC = analogRead(pinSensorT);
tempC = (5.0*tempC*100) / 1024.0;
Serial.println(tempC);
delay(2000);
}
