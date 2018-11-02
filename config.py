'''
All keys from api's should go here

Make sure to create environment variables, using .bash_profile 
ie: export TWILIO_ACC="Key goes here"
'''
import os


class TwilioKeys:

	account_sid = os.environ.get("TWILIO_ACC")
	auth_token = os.environ.get("TWILIO_AUTH")
	myPhone = os.environ.get("MY_PHONE")
	TwilioNumber = os.environ.get("TWILIO_NUM")

	
	message = 'This is an Automated message from HEALTH COMPANION, Please send medical assistance to 490 8th Ave, New York, NY 10001.' #This is the address of a macdonalds in ny :)

