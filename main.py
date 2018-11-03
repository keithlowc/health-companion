from config import TwilioKeys
from src.communications.twilio_coms import Twilio
from src.temperature.temperature import TemperatureSensor
from src.gas.gas_sensor import GasSensor


def communication(celcius,farenheit,co2,tvoc):
	data = 'The current Temperature is: {} C, {} F\nThe CO2 levels are: {}\nThe TVOC levels are: {}'.format(celcius,farenheit,co2,tvoc)

	message = Twilio(account_sid= 	TwilioKeys.account_sid,
					auth_token=		TwilioKeys.auth_token,
					myPhone=		TwilioKeys.myPhone,
					TwilioNumber=	TwilioKeys.TwilioNumber,
					message=		TwilioKeys.message + data)

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

def main():
	celcius, farenheit = temp()
	co2, tvoc = gas_sensing()
	communication(celcius,farenheit,co2,tvoc)

main()
