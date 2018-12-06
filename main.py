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

# def temp():
# 	temp = TemperatureSensor()
# 	celcius, farenheit = temp.get_temp()
# 	return celcius, farenheit

def gas_sensing():
	try:
		gas = GasSensor()
		co2, tvoc = gas.get_gas()
		return co2, tvoc
	except Exception as e:
		print('There was an ERROR in gas sensing: ' + str(e))
		co2 = 'Null'
		tvoc = 'Null'
		return co2, tvoc

def pulse_sensing():
	p = Pulsesensor()
	p.startAsyncBPM()
	counter = 0
	pulse_range = []
	try:
		x = input('Ready To start HEARTBEAT sensing? Y/N')
		if x.upper() == 'Y':
			while counter <= 10:
				counter += 1
				bpm = p.BPM
				if bpm > 0:
					print("BPM: %d" % bpm)
					pulse_range.append(bpm)
				else:
					print("HEARTBEAT not found - setting to 0")
					pulse_range.append(0)
				time.sleep(1)
			p.stopAsyncBPM()
			return str(pulse_range)
	except:
		p.stopAsyncBPM()

def main():
	# celcius, farenheit = temp()
	co2, tvoc = gas_sensing()
	pulse = pulse_sensing()
	communication(1,1,co2,tvoc, pulse)

main()
