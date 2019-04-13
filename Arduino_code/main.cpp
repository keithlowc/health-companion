#include "pulse_sensor.h";
#include "temp_sensor.h";

Pulse pulsing(0); // Analog input 
TemperatureSensor tempSensor; // Digital pin #2

void setup()
{
  Serial.begin(9600);
  pulsing.PulseSetUp();
  tempSensor.InitializeTemperatureSensing();
}

void loop()
{
  pulsing.PulseSensing();
  tempSensor.CaptureTemperature();
}