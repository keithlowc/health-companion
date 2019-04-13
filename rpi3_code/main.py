# from config import TwilioKeys
# from src.communications.twilio_coms import Twilio
from src.temperature.temperature import TemperatureSensor
from src.gas.gas_sensor import GasSensor
from src.pulse.pulse_sensor import Pulsesensor

import time
import requests


# def communication(celcius,farenheit,co2,tvoc,pulse):
# 	data = 'The current Temperature is: {} C, {} F. The CO2 levels are: {} The TVOC levels are: {} The pulse range is: {}'.format(celcius,farenheit,co2,tvoc,pulse)

# 	message = Twilio(account_sid= 	TwilioKeys.account_sid,
# 					auth_token=		TwilioKeys.auth_token,
# 					myPhone=		TwilioKeys.myPhone,
# 					TwilioNumber=	TwilioKeys.TwilioNumber,
# 					message=		TwilioKeys.message + str(data))

# 	message.make_call()
# 	message.send_text()

def gas_sensing():
	try:
		gas = GasSensor()
		co2, tvoc, temp = gas.get_gas()
		return co2, tvoc, temp
	except Exception as e:
		print('There was an ERROR in gas sensing: ' + str(e))
		co2 = 'Null'
		tvoc = 'Null'
		temp = 'Null'
		return co2, tvoc, temp

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

	try:
		while True:
			temperature = temperature_sensing()
			bpm = p.BPM
			if bpm > 0 and temperature > 0:
				print("BPM: %d" % bpm)
				bpm_list.append(bpm)
				temp_list.append(temperature)
				counter += 1
				if counter >= 5:
					total_bpm = get_average_from_list(bpm_list)
					total_temp = get_average_from_list(temp_list)
					send_post_request(total_bpm,total_temp)
					counter = 0
			else:
				print(bpm)
				print("Not hearbeat found")
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
	API_ENDPOINT = 'http://healthcompanionv1.herokuapp.com/data'
	all_data = {
		'bpm': bpm,
		'bodyTemp': temp,
	}

	r = requests.post(url = API_ENDPOINT, json = all_data)
	response = r.text
	print("Response was sent")

def main():
	pulse = pulse_and_temp_sensing()
	print(pulse)

if __name__ == '__main__':
	main()













































