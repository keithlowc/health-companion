'''
This class measures CO2, TVOC and temperature levels, while using the CCS811 sensor
Following this tutorial: https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor/raspberry-pi-wiring-test#step-9
'''

from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811

class GasSensor:

	def __init__(self):
		self.ccs =  Adafruit_CCS811()

	def get_gas(self):
		while not self.ccs.available():
			pass
		temp = self.ccs.calculateTemperature()
		self.ccs.tempOffset = temp - 25.0

		if self.ccs.available():
		    temp = self.ccs.calculateTemperature()
		    if not self.ccs.readData():
		    	CO2_measurement = self.ccs.geteCO2()
		    	TVOC_measurement = self.ccs.getTVOC()
		    else:
		    	print("THERE WAS AN ERROR MEASURING GAS!")
		return CO2_measurement, TVOC_measurement

if __name__ == '__main__':
	obj = GasSensor()
	co2, tvoc = obj.get_gas()
	print('The CO2 level is: ' + str(co2) + ' ppm\n')
	print('The TVOC level is: ' + str(tvoc))