//Narduino Project by Ahmet YILDIRIM
//homepage:www.mclightning.com
//Code Licence: GNU General Public Licence v3

int mot1ana=3;
int mot1a=2;
int mot1b=4;
//motor1
int ledstat=0;
int leds=8;
//led
int mot2ana=5;
int mot2a=6;
int mot2b=7;
//motor2
int gel=0;

void setup() {
  Serial.begin(9600);
pinMode(mot1ana,OUTPUT);
pinMode(mot1a,OUTPUT);
pinMode(mot1b,OUTPUT);
pinMode(mot2ana,OUTPUT);
pinMode(mot2a,OUTPUT);
pinMode(mot2b,OUTPUT);
pinMode(leds,OUTPUT);
}

void loop() {
  if(Serial.available())
  {
  gel=Serial.read();
  if(gel==97) {
  //  A
  analogWrite(mot1ana,200);
  digitalWrite(mot1a,HIGH);
  digitalWrite(mot1b,LOW);
  }
  if(gel==98) {
  // B
  analogWrite(mot1ana,200);
  digitalWrite(mot1a,LOW);
  digitalWrite(mot1b,HIGH);
  }
  if(gel==99) {
  // C
  digitalWrite(mot1ana,0);
  digitalWrite(mot1a,LOW);
  digitalWrite(mot1b,LOW);
  }
  if(gel==100) {
  // D
  analogWrite(mot2ana,255);
  digitalWrite(mot2a,HIGH);
  digitalWrite(mot2b,LOW);
  Serial.println('d');
  }
  if(gel==101) {
  // E
  analogWrite(mot2ana,255);
  digitalWrite(mot2a,LOW);
  digitalWrite(mot2b,HIGH);
  Serial.println('e');
  }
  if(gel==102) {
  // F
  digitalWrite(mot2ana,0);
  digitalWrite(mot2a,LOW);
  digitalWrite(mot2b,LOW);
  }
  if(gel==103) {
  digitalWrite(leds,HIGH);
  }
  if(gel==104) {
  digitalWrite(leds,LOW);
  }
  Serial.flush();
  }
}
