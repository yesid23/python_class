const int LED =13;
const int BOTON = 7;
int off = 0; 
int estadoled = 0; // 0 LED apagado, 1 LED encendido
int valorled = 0; 
void setup(){ 
 pinMode(LED,OUTPUT); 
 pinMode(BOTON,INPUT); 
}
void loop() {       
off= digitalRead(BOTON); 
if ((off == HIGH) && (valorled == LOW)){
estadoled=1-estadoled;
delay(10);
}
valorled = off; 
if (estadoled==1){
 digitalWrite(LED, HIGH); // enciende el LED
}
else{
 digitalWrite(LED,LOW); // apagar el LED
}
}
