'''
All keys from api's should go here

Make sure to create environment variables, using .bash_profile 
ie: export TWILIO_ACC="Key goes here"
'''
import os


class TwilioKeys:

	account_sid = ""
	auth_token = ""
	myPhone = ""
	TwilioNumber = ""

	message = 'This is an Automated message from HEALTH COMPANION, Please send medical assistance to 490 8th Ave, New York, NY 10001.' #This is the address of a macdonalds in ny :)

class DeviceSettings:

	Bpm_count = 5
	API_ENDPOINT_DATA = 'https://healthcompanionv1.herokuapp.com/data'
	API_ENDPOINT_AVERAGES = 'http://healthcompanionv1.herokuapp.com/data/averages'
