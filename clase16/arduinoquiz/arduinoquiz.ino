//daniel obando - yesid nasner
char serialData;
int pinLed = 13;

void setup() {
 pinMode(pinLed,OUTPUT);
 Serial.begin(9600);

}

void loop() {
  if(Serial.available()>0){
    serialData = Serial.read();
    Serial.print(serialData);
    
    if(serialData== 'opera'){
    digitalWrite(pinLed, HIGH);

    } 
    }
  }

