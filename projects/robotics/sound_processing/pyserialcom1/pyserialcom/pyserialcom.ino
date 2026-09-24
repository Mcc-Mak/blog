int LedPin =7;
int HammerPin = 8;
bool flag = false;
int freq = 20;
String inByte;
void setup() {
Serial.begin(9600);
Serial.println("Ready!");
pinMode(LedPin,OUTPUT);
digitalWrite(LedPin,LOW);
pinMode(HammerPin,OUTPUT);
digitalWrite(HammerPin,LOW);
}
//.toInt()
//Serial.read() => int

void loop() {


if(Serial.available()>0) //receive less than 2 bytes 
{

 //String inByte  = Serial.readStringUntil('\n');
 String inByte  = Serial.readString();
Serial.println(inByte);
if(inByte =="K")
{
  flag = true;
  }

if(flag ==true){

digitalWrite(HammerPin,HIGH);
delay(freq);
digitalWrite(HammerPin,LOW);
delay(freq);
flag = false;
}

if(inByte == "S")
{
  Serial.println("Spray!");
  digitalWrite(LedPin,HIGH);
  delay(200);
  digitalWrite(LedPin,LOW);
  delay(200);
  
  
  }
if(inByte == "U")
{
  Serial.print("Unspray!");
  }


/*
unsigned long now = millis ();
while (millis () - now < 1000)
{
  Serial.read();
}
*/
Serial.flush();
}

  }
