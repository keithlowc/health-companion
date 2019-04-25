from config import TwilioKeys, DeviceSettings
from src.communications.twilio_coms import Twilio
from src.temperature.temperature import TemperatureSensor
# from src.gas.gas_sensor import GasSensor
from src.pulse.pulse_sensor import Pulsesensor

import time
import requests


def communication(temperature,pulse):
	data = 'The current Temperature is: {} The pulse range is: {}'.format(temperature,pulse)

	message = Twilio(account_sid= 	TwilioKeys.account_sid,
					auth_token=		TwilioKeys.auth_token,
					myPhone=		TwilioKeys.myPhone,
					TwilioNumber=	TwilioKeys.TwilioNumber,
					message=		TwilioKeys.message + str(data))

	message.make_call()
	message.send_text()

# def gas_sensing():
# 	try:
# 		gas = GasSensor()
# 		co2, tvoc, temp = gas.get_gas()
# 		return co2, tvoc, temp
# 	except Exception as e:
# 		print('There was an ERROR in gas sensing: ' + str(e))
# 		co2 = 'Null'
# 		tvoc = 'Null'
# 		temp = 'Null'
# 		return co2, tvoc, temp

def temperature_sensing():
	temp = TemperatureSensor()
	temperature_val = temp.get_temp()[1]
	return temperature_val

def pulse_and_temp_sensing():
	p = Pulsesensor()
	p.startAsyncBPM()
	counter = 0
	bpm_list = []
	temp_list = []
	call = False
	message = ""

	try:
		while True:
			temperature = temperature_sensing()
			bpm = p.BPM
			if bpm > 0 and temperature > 0:

				print("BPM: %d" % bpm)
				print("Temperature: %d" % temperature)

				bpm_list.append(bpm)
				temp_list.append(temperature)

				counter += 1
				if counter >= DeviceSettings.Bpm_count:
					total_bpm = get_average_from_list(bpm_list)
					total_temp = get_average_from_list(temp_list)
					send_post_request(total_bpm,total_temp)

					response = send_get_request()

					avg_bpm = response["average_bpm"]
					avg_temp = response["average_temp"]

					call = check_data(avg_bpm,avg_temp)

					if call:
						communication(avg_temp,avg_bpm)
					counter = 0

			else:
				print(bpm)
				print("No hearbeat found")
			time.sleep(1)
	except Exception as e:
		print("Exception happened")
		print(e)
		p.stopAsyncBPM()

def get_average_from_list(list_given):
	total = 0
	for x in list_given:
		total += x
	total = total / len(list_given)
	return total

def send_post_request(bpm, temp):
	API_ENDPOINT = DeviceSettings.API_ENDPOINT_DATA
	all_data = {
		'bpm': bpm,
		'bodyTemp': temp,
	}

	r = requests.post(url = API_ENDPOINT, json = all_data)
	response = r.text
	print("This is the response returned: ")
	print(response)
	print("Response was sent")

def send_get_request():
	API_ENDPOINT = DeviceSettings.API_ENDPOINT_AVERAGES
	r = requests.get(API_ENDPOINT)
	response = r.json()
	return response

def check_data(avg_bpm,avg_temp):
	if avg_bpm > 130 and avg_temp > 95 or avg_temp < 99:
		#BPM is too high
		#Temp is normal
		call = False
		return call
	elif avg_bpm < 40 and avg_temp > 95 or avg_temp < 99:
		#bpm is too low
		#temp is normal
		call = False
		return call
	elif avg_bpm > 40 and avg_bpm < 100 and avg_temp > 95 or avg_temp < 99:
		#bpm is normal
		#temp is normal
		call = False 
		return call
	elif avg_bpm > 40 and avg_bpm < 100 and avg_temp < 95:
		#bpm is normal
		#temp is low
		call = False
		return call
	elif avg_bpm > 40 and avg_temp < 100 and avg_temp > 99:
		#bpm is normal
		#temp is high
		call = False
		return call
	elif avg_bpm < 40 or avg_bpm > 125 or avg_temp < 95 or avg_temp > 99:
		call = True
		return call



def main():
	pulse = pulse_and_temp_sensing()
	print(pulse)

if __name__ == '__main__':
	main()













































