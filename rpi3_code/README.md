# Health Companion: Is a pattern focused wearable device to help agign citizens stay safe and contact emergency services if required.

# Perform the following on your RPI3 to run the code

## Heart Pulse Sensor setup:

### For ADC converter perform the following:

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

### For all of the above make sure to activate the gpio pins

* $ sudo raspi-config 

** > Select interfaces > activate the i2c and gpio 

## DS18B20 temperature sensor:

* At the command prompt, enter: sudo nano /boot/config.txt, then add this to the bottom of the file: dtoverlay=w1–gpio
* Exit Nano, and reboot the Pi (sudo reboot)
* Log in to the Pi again, and at the command prompt enter sudo modprobe w1–gpio
* Then enter sudo modprobe w1-therm
* Change directories to the /sys/bus/w1/devices directory by entering: cd /sys/bus/w1/devices
* Now enter ls to list the devices:
* 28-000006637696 w1_bus_master1 is displayed in my case.
* Now enter cd 28-XXXXXXXXXXXX (change the X’s to your own address)
* For example, in my case I would enter: cd 28-000006637696
* Enter cat w1_slave which will show the raw temperature reading output by the sensor: 

## End

* Once all the steps above are done you can go ahead and run the main.py file for full fuctionality


# Resources:

## Temperature Sensor Tutorial: 

* Following this tutorial: http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

## Pulse sensor Tutorial:

* Following this tutorial: https://tutorials-raspberrypi.com/raspberry-pi-heartbeat-pulse-measuring/
* Code from: https://github.com/WorldFamousElectronics/PulseSensor_Amped_Arduino

## Gas Sensor Tutorial:This class measures CO2, TVOC and temperature levels, while using the CCS811 sensor

* Following this tutorial: https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor/raspberry-pi-wiring-test*step-9
