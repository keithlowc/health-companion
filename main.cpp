#include "pulse_sensor.h";

Pulse test(0); // Analog input 

void setup()
{
  Serial.begin(9600);
  test.PulseSetUp();
}

void loop()
{
  test.PulseSensing();
}