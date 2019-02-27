#define USE_ARDUINO_INTERRUPTS true 
#include <PulseSensorPlayground.h>


PulseSensorPlayground pulseSensor;

class Pulse
{
  int PulseWire;
  int Threshold = 550;

  public:
    Pulse(int AnalogPin)
    {
      PulseWire = AnalogPin;
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

    void PulseSensing()
    {
      int myBPM = pulseSensor.getBeatsPerMinute();
      int range = 15;
      //array of size 15 and add each bpm to it
      //to later take the 

      for (int i = 0; i <= range; i++) 
      {
	      if (pulseSensor.sawStartOfBeat()) {
	        Serial.println("♥  A HeartBeat Happened ! ");
	        Serial.print("BPM: ");
	        Serial.println(myBPM);
	      }
	  }
    }
};