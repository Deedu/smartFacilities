//Pin Layout Constants
const unsigned int led = 13;
const unsigned int methaneInp1=A1;
const unsigned int methaneInp2 = A2;
const unsigned int photoInp = A0;
const unsigned int sonicTrigInp = 11;
const unsigned int sonicEchoInp = 12;
const unsigned int buttonInp = 4;
String writeString = "";


// the setup routine runs once when you press reset:
void setup() {         
Serial.begin(9600);
  // initialize the digital pin as an output.
  pinMode(sonicTrigInp,OUTPUT);
  pinMode(sonicEchoInp,INPUT);
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {

  //Read First sensor, button
  int buttonPush = digitalRead(buttonInp);
  String buttonPushVal = String(buttonPush);
  writeString += buttonPushVal + "~";

  //Do a distance check
  digitalWrite(sonicTrigInp,LOW);
  delayMicroseconds(2);
  digitalWrite(sonicTrigInp,HIGH);
  delayMicroseconds(2);
  digitalWrite(sonicTrigInp,LOW);
  long duration = pulseIn (sonicEchoInp, HIGH);
  int distance = duration/29/2;
  String distVal = String(distance);
  writeString += distVal + "~";

  //PhotoSensor
  int photo = analogRead(0);
  String photoVal = String(photo);
  writeString += photoVal + "~";

  //Methane
  int methane1 = analogRead(methaneInp1);
  String methane1Val = String(methane1);
  writeString += methane1Val + "~";
  int methane2= analogRead(methaneInp2);
  String methane2Val = String(methane2);
  writeString += methane2Val;

  Serial.print(writeString);
  
}
