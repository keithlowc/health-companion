from config import TwilioKeys
from src.communications.twilio_coms import Twilio
from src.temperature.temperature import TemperatureSensor


def communication(celcius,farenheit):
	message = Twilio(account_sid= 	TwilioKeys.account_sid,
					auth_token=		TwilioKeys.auth_token,
					myPhone=		TwilioKeys.myPhone,
					TwilioNumber=	TwilioKeys.TwilioNumber,
					message=		TwilioKeys.message + 'The current temp is: C: ' + str(celcius) + ' F: ' + str(farenheit))

	message.make_call()
	message.send_text()

def temp():
	temp = TemperatureSensor()
	celcius, farenheit = temp.get_temp()
	return celcius, farenheit

def main():
	celcius, farenheit = temp()
	communication(celcius,farenheit)

main()