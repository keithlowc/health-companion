'''
This class was made with twilio's api to make calls and send text messages,
with information provided by the user

Example of usage on: if__name__ == '__main__'
'''

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say


class Twilio:
	def __init__(self, account_sid, auth_token, myPhone, TwilioNumber, message):
		self.account_sid = account_sid
		self.auth_token = auth_token
		self.myPhone = myPhone
		self.TwilioNumber = TwilioNumber
		self.message = message
		self.client = Client(self.account_sid, self.auth_token)

	def send_text(self):
		print('\n+++++++++++++++++++++ START send_text() +++++++++++++++++++++')		
		self.client.messages.create(to=self.myPhone, from_=self.TwilioNumber, body=self.message)
		print('Message sent succesfully!')
		print('+++++++++++++++++++++ END send_text() +++++++++++++++++++++')	

	def make_call(self):
		print('\n+++++++++++++++++++++ START make_call() +++++++++++++++++++++')	
		new_message = self.message
		new_message = new_message.replace(' ','+')
		url = 'http://twimlets.com/echo?Twiml=%3CResponse%3E%3CSay%3E{}.%3C%2FSay%3E%3C%2FResponse%3E'.format(new_message)

		self.client.calls.create(to = self.myPhone,from_ = self.TwilioNumber,url= url,)
		print('Call was succesful!')
		print('+++++++++++++++++++++ END make_call() +++++++++++++++++++++')


if __name__ == '__main__':
	account_sid = input('Enter account_sid:\n')
	auth_token = input('Enter auth_token:\n')
	my_phone = input('Enter Your Phone number ("+13156668888"):\n')
	TwilioNumber = input('Enter Your twilio number ("+13156668888"):\n')
	message = input('Enter message:\n')
	x = Twilio(account_sid=account_sid,
				auth_token=auth_token,
				myPhone=my_phone,
				TwilioNumber=TwilioNumber,
				message=message)
	x.send_text()
	x.make_call()