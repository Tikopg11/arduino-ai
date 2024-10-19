int button = 13; //button
int adcpin = 26; //microphone
void setup() 
{
  // put your setup code here, to run once:
  pinMode(button, INPUT_PULLUP);
  pinMode(adcpin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

uint16_t miclist[16000];

void loop() 
{
  // put your main code here, to run repeatedly:
  analogReadResolution(16);
  int buttonstate = digitalRead(button);
  if (buttonstate != 1)
  {
    digitalWrite(LED_BUILTIN,HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);
    unsigned long Target = micros() + 125;
    for (int i = 0; i < 16000; i++)
    {
      int micvalue = analogRead(adcpin);
      miclist[i] = micvalue;
      while (micros() < Target);
      Target = Target + 125;
    }
    for (int i = 0; i < 15999; i++)
    {
      if (i != 15998)
      {
        Serial.print(miclist[i]);
        Serial.print(" ");
      }
      else
      {
        Serial.println(miclist[15999]);
      }
    }
  }
}
