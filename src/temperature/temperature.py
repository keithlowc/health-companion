'''
This class provides the room temperature while using the sensor: DS18B20
with the Raspberrypi

Example of usage on: if__name__ == '__main__'
'''

import os
import glob
import time

class TemperatureSensor:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folder = glob.glob(self.base_dir + '28*')[0]
        self.device_file = self.device_folder + '/w1_slave'

    def read_temp_raw(self):
        os.chdir('/home/pi')
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = (lines[1])[equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return (temp_c, temp_f)

    def get_temp(self):
        celcius, farenheit = self.read_temp()
        time.sleep(1)
        os.chdir(self.current_dir)
        return celcius, farenheit


if __name__ == '__main__':
    obj = TemperatureSensor()
    print(obj.get_temp())

