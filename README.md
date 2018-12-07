# Health Companion: Is a pattern focused wearable device to help agign citizens stay safe and contact emergency services if required.

## Pulse sensor Tutorial: This class uses the pulsesensor to measure heartbeat rate

* extended from https://github.com/WorldFamousElectronics/PulseSensor_Amped_Arduino

## For ADC converter perform the following:

* First install spidev:
* Enable SPI (sudo raspi-config)
* $ sudo apt-get update 
* $ sudo apt-get upgrade
* $ sudo apt-get install python-dev
* $ sudo reboot
* $ wget https://github.com/doceme/py-spidev/archive/master.zip 
* $ unzip master.zip
* $ cd py-spidev-master
* $ sudo python setup.py install

## Gas Sensor Tutorial:This class measures CO2, TVOC and temperature levels, while using the CCS811 sensor
Following this tutorial: https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor/raspberry-pi-wiring-test*step-9

## For all of the above make sure to activate the gpio pins

* $ sudo raspi-config 

** > Select interfaces > activate the i2c and gpio 
