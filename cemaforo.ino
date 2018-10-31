int ledrojo = 13;
int lednar = 12;
int ledverde = 11;

void setup() {
  // put your setup code here, to run once:
pinMode(ledrojo,OUTPUT);
pinMode(lednar,OUTPUT);
pinMode(ledverde,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(ledrojo,HIGH);
delay(100); //tiempo de espera
digitalWrite(ledrojo,LOW);
delay(30);
digitalWrite(ledrojo,HIGH);
delay(100); //tiempo de espera
digitalWrite(ledrojo,LOW);
delay(30);
digitalWrite(ledrojo,HIGH);
delay(100); //tiempo de espera
digitalWrite(ledrojo,LOW);
delay(30);
digitalWrite(lednar,HIGH);
delay(100); //tiempo de espera
digitalWrite(lednar,LOW);
delay(30);
digitalWrite(lednar,HIGH);
delay(100); //tiempo de espera
digitalWrite(lednar,LOW);
delay(30);
digitalWrite(lednar,HIGH);
delay(100); //tiempo de espera
digitalWrite(lednar,LOW);
delay(30);
digitalWrite(ledverde,HIGH);
delay(000); //tiempo de espera
digitalWrite(ledverde,LOW);
delay(000);
}
