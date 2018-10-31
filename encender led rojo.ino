char opcion = '0';
 int ledrojo = 13;
 
 void setup() {
Serial.begin(9600);
pinMode(ledrojo,OUTPUT);
}

void loop() 
{
if(Serial.available()>0)
{ opcion = Serial.read();
  if(opcion == '0')
  { Serial.println("menu");
   Serial.println("1. encender led rojo");
   Serial.println("2. apagar el led rojo");
  }
 if(opcion == '1')
 { 
   digitalWrite(ledrojo,HIGH);
 }else{
  if(opcion == '2')
  { digitalWrite(ledrojo,LOW);
  }else{
    Serial.println("opcion incorrecta");
  }
 }
}

