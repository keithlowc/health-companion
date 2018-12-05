from config import TwilioKeys
from src.communications.twilio_coms import Twilio
from src.temperature.temperature import TemperatureSensor
from src.gas.gas_sensor import GasSensor
from src.pulse_sensing.pulsesensor import Pulsesensor

def communication(celcius,farenheit,co2,tvoc,pulse):
	data = 'The current Temperature is: {} C, {} F. The CO2 levels are: {} The TVOC levels are: {} The pulse range is: {}'.format(celcius,farenheit,co2,tvoc,pulse)

	message = Twilio(account_sid= 	TwilioKeys.account_sid,
					auth_token=		TwilioKeys.auth_token,
					myPhone=		TwilioKeys.myPhone,
					TwilioNumber=	TwilioKeys.TwilioNumber,
					message=		TwilioKeys.message + str(data))

	message.make_call()
	message.send_text()

def temp():
	temp = TemperatureSensor()
	celcius, farenheit = temp.get_temp()
	return celcius, farenheit

def gas_sensing():
	gas = GasSensor()
	co2, tvoc = gas.get_gas()
	return co2, tvoc

def pulse_sensing():
	p = Pulsesensor()
	p.startAsyncBPM()
	time = 0
	pulse = []

	while time <= 5:
		time += 1
		bpm = p.bpm
		if bpm > 0:
			print('BPM: %d' % bpm)
			pulse.append(bpm)
		else:
			print('HEARTBEAT NOT FOUND!')
		time.sleep(1)
	p.stopAsyncBPM()
	return pulse

def main():
	celcius, farenheit = temp()
	co2, tvoc = gas_sensing()
	pulse = pulse_sensing()
	communication(celcius,farenheit,co2,tvoc, pulse)

main()
