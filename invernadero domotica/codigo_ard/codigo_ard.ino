const int pinLED = 13;

char serialData;
int pinLed = 12;


const int sensor = A1;          //Pin en el que está conectado el sensor
const int Rc = 1000;            //Resistencia de calibración
const int relay = 2;            //Pin en en que está conectado el Relay            
int V;
int contador = 0;
long Rsensor;
long Resk;
unsigned long tr = 1;            //Tiempo de regado  en minutos                                   //AJUSTAR
unsigned long tespera = 10;      //Tiempo espera en minutos                                       //AJUSTAR
const int rr = 0.5 ;               //Resistencia (en kohmios) a partir de la cual empieza a regar   //AJUSTAR

int dato1;
int dato2;
float voltios;
float temperaturaC;
int alarma=7;
int techo=8;
int ventilador=9;


void ControlAlarma()
{
  if(temperaturaC<24 && dato2>850)
  {
  digitalWrite(alarma,LOW);
  } 
  
  if(temperaturaC>=24)
  {
    digitalWrite(alarma,HIGH);
  }

}

void ControlTecho()
{ 
  if(temperaturaC>=24)
  {
    digitalWrite(techo,HIGH);
  }
  else
  {
    digitalWrite(techo,LOW);
  }

}

void ControlVentilador()
{

  if(temperaturaC>=24)
  {
    digitalWrite(ventilador,HIGH);
  }
  else
  {
    digitalWrite(ventilador,LOW);
  }

}


void setup() {
  
  // put your setup code here, to run once:

   pinMode(pinLed,OUTPUT);
 Serial.begin(9600);
 
  //puerta
Serial.begin(9600);
pinMode(pinLED, OUTPUT);
pinMode(10,OUTPUT);
pinMode(6,INPUT);
pinMode(5,INPUT);
   
   Serial.begin(9600);             //inicia comunicación serial
  pinMode (relay,OUTPUT);         //Configurar relay como salida
  pinMode(alarma,OUTPUT);
  pinMode(techo,OUTPUT);
  pinMode(ventilador,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  
  V =  analogRead(sensor);        //leer sensor
  Rsensor = 1024L * Rc / V - Rc;  //calcular resistencia del sensor
  Resk = Rsensor /1000;           //pasar a kiloohmios

  Serial.print(contador); Serial.println("  riegos.");  //contador para ver en serial cuantas veces se ha regado
Serial.print("Valor resistencia: "); Serial.print(Resk); Serial.println(" mil ohmios ");   //escribir en serial el valor de la resistencia
  delay(1000);

 if (Resk>rr){
  digitalWrite(relay,HIGH);       //activar relay
  delay(tr*60*1000);              // Espera Tiempo de regado con relay activado
  digitalWrite(relay,LOW);        //desactivar relay
  delay(tespera*60*1000);         // Espera Tiempo de espera entre regados con relay desactivado para que el agua se filtre a la tierra y llegue al sensor
  contador = contador + 1 ;   
  }
 
 //puerta

// luz
  if(Serial.available()>0){
    serialData = Serial.read();
    Serial.print(serialData);
    
    if(serialData== '1'){
    digitalWrite(pinLed, HIGH);
    } else{
      if(serialData== '0'){
        digitalWrite(pinLed, LOW);
      }
    }
  }

  if (Serial.available()>0) 
  {
    char option = Serial.read();
    if (option >= '1' && option <= '9')
    {
      option -= '0';
      for (int i = 0;i<option;i++) 
      {
        digitalWrite(pinLED, HIGH);
        delay(200);
      
      digitalWrite(pinLED, LOW);
       
        
      }
    }
  }

    
 
 dato1 = analogRead(A0);
  voltios = (dato1 / 1023.0) * 5;
  temperaturaC = voltios / 10e-3; 
  Serial.print("TEMPERATURA : ");
  Serial.print(temperaturaC);
  Serial.println(" C");
  delay(300);
  
  Serial.println("");
  
  dato2 = analogRead(A1);
 // Serial.print("HUMEDAD : ");
 // Serial.println(dato2);
  delay(1000);
  int lecturaporcentaje = map(dato2, 1023, 0, 0, 100);
  Serial.print("la humedad es del: ");
  Serial.print(lecturaporcentaje);
  Serial.println("%");

  ControlAlarma();
  ControlVentilador();
  ControlTecho();
  

}
