#define PIR         2
#define MOTOR       4

void has_presence()
{
  if(digitalRead(PIR) == 1)
  {
    Serial.println("1"); 
  }
  else
  {
    Serial.println("0");  
  }
  
}

void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(MOTOR, OUTPUT);
  pinMode(PIR, INPUT);
}

void loop()
{
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    switch(incomingByte)
    {
      case 'l':
        digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(MOTOR, HIGH);
        break;
      case 'd':
        digitalWrite(LED_BUILTIN, LOW);
        digitalWrite(MOTOR, LOW);
        break;
      case 'g':
        has_presence();
        break;
    }    
  }
}

