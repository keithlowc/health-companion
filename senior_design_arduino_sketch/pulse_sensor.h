#define USE_ARDUINO_INTERRUPTS true 
#include <PulseSensorPlayground.h>


PulseSensorPlayground pulseSensor;

class Pulse
{
  int PulseWire;
  int Threshold = 550;
  int PulseAverageSize;

  public:
    Pulse(int AnalogPin, int sizeAveragePulse)
    {
      PulseWire = AnalogPin;
      PulseAverageSize = sizeAveragePulse;
    }

    void PulseSetUp()
    {
      pulseSensor.analogInput(PulseWire);
      // pulseSensor.blinkOnPulse(LED13);
      pulseSensor.setThreshold(Threshold);

      if (pulseSensor.begin()) {
        Serial.println("We created a pulseSensor object !");
      }
    }

    int PulseSensing()
    {
      int myBPM = pulseSensor.getBeatsPerMinute();

      if (pulseSensor.sawStartOfBeat()) {
        Serial.println("♥  A HeartBeat Happened ! ");
        Serial.print("BPM: ");
        Serial.println(myBPM);
      }
    }

    void getAveragePulse()
    {
      int pulses[PulseAverageSize];
      int i;
      int pulseValue = 0;
      float total;

      for (i = 0; i < PulseAverageSize; i++)
      {
        Serial.print("Iteration # ");
        Serial.println(i);
        Serial.print("This is the current pulse value: ");
        Serial.println(pulseValue);
        pulseValue += PulseSensing();
      }

      total = pulseValue / PulseAverageSize;

      Serial.println("This is the total: ");
      Serial.println(total);
    }
};
