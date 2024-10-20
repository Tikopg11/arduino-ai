int button = 13; //button
int adcpin = 26; //microphone
unsigned long target_time;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(button, INPUT_PULLUP);
  pinMode(adcpin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() 
{
  // put your main code here, to run repeatedly:
  analogReadResolution(16);
  int miclist[16000];
  int buttonstate = digitalRead(button);
  if (buttonstate != 1)
  {
    digitalWrite(LED_BUILTIN,HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);
    target_time = micros();
    for (int i = 0; i < 16000; i++)
    {
      int micvalue = analogRead(adcpin);
      miclist[i] = micvalue;
      target_time = target_time + 125;
      while(micros() < target_time);
    }
    for (int i = 0; i < 16000; i++)
    {
      if (i != 15999)
      {
        Serial.print(miclist[i]);
        Serial.print(" ");
      }
      else
      {
        Serial.println(miclist[i]);
      }
    }
  }
  delay(100);
}
