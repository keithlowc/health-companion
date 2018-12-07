from config import TwilioKeys
from src.communications.twilio_coms import Twilio
from src.temperature.temperature import TemperatureSensor
from src.gas.gas_sensor import GasSensor
from src.pulse.pulse_sensor import Pulsesensor
import time

def communication(celcius,farenheit,co2,tvoc,pulse):
	data = 'The current Temperature is: {} C, {} F. The CO2 levels are: {} The TVOC levels are: {} The pulse range is: {}'.format(celcius,farenheit,co2,tvoc,pulse)

	message = Twilio(account_sid= 	TwilioKeys.account_sid,
					auth_token=		TwilioKeys.auth_token,
					myPhone=		TwilioKeys.myPhone,
					TwilioNumber=	TwilioKeys.TwilioNumber,
					message=		TwilioKeys.message + str(data))

	message.make_call()
	message.send_text()

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

def pulse_sensing():
	p = Pulsesensor()
	p.startAsyncBPM()
	counter = 0
	pulse_range = []
	try:
		x = input('Ready To start HEARTBEAT sensing? Y/N ')
		if x.upper() == 'Y':
			while counter <= 20:
				bpm = p.BPM
				if bpm > 0:
					print("BPM: %d" % bpm)
					pulse_range.append(bpm)
					counter += 1
				else:
					print("HEARTBEAT NOT FOUND ON TRY " + str(counter))
				time.sleep(1)
			p.stopAsyncBPM()
			average = str(get_average_from_list(pulse_range))
			return average
	except:
		p.stopAsyncBPM()

def get_average_from_list(list_given):
	total = 0
	for x in list_given:
		total = total + x
	total = total / len(list_given)
	return total


def main():
	co2, tvoc, temp = gas_sensing()
	pulse = pulse_sensing()
	print(pulse)
	communication(temp,temp,co2,tvoc, pulse)

main()
