int button = 13; //button
int adcpin = 26; //microphone
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
  int miclist[5000];
  int buttonstate = digitalRead(button);
  if (buttonstate != 1)
  {
    Serial.println("Pressed");
    digitalWrite(LED_BUILTIN,HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);
    for (int i = 0; i < 5000; i++)
    {
      int micvalue = analogRead(adcpin);
      miclist[i] = micvalue;
      Serial.println("added to list ");
    }
    for (int i = 0; i < 5000; i++)
    {
      Serial.print(miclist[i]);
      if (i != 4999)
      {
        Serial.print(", ");
      }
    }
  }
  delay(100);
}
