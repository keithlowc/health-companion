#include <OneWire.h>
#include <DallasTemperature.h>

int ONE_WIRE_BUS = 2;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

class TemperatureSensor
{
  public:
    void InitializeTemperatureSensing()
    {
      Serial.println("Temperature sensing has started!");
      sensors.begin();
    }

    void CaptureTemperature()
    {
      sensors.requestTemperatures();
      Serial.println(sensors.getTempCByIndex(0));
      delay(1000);
    }
};
