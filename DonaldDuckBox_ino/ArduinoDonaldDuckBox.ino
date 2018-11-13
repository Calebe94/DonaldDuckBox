#include <dht.h>

#define DHT11_PIN 7
#define TRIG_PIN  6
#define ECHO_PIN  5
#define LED       4

dht DHT;

int read_distance()
{
  long duration = 0; 
  int distance = 0;
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  duration = pulseIn(ECHO_PIN, HIGH);
  
  distance = (duration*0.034)/2;
  return distance;
}

void send_data()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("T:");
  Serial.print(DHT.temperature);
  Serial.print("-H:");
  Serial.print(DHT.humidity);
  Serial.print("-P:");
  Serial.println(read_distance());
}

void setup()
{
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    switch(incomingByte)
    {
      case 'l':
        digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(LED, HIGH);
        break;
      case 'd':
        digitalWrite(LED_BUILTIN, LOW);
        digitalWrite(LED, LOW);
        break;
      case 'g':
        send_data();
        break;
    }    
  }
}

