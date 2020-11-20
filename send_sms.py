import os

from twilio.rest import Client
from dotenv import load_dotenv
 
load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_MY_NUMBER = os.getenv('TWILIO_MY_NUMBER')
TWILLO_NUMBER = os.getenv('TWILLO_NUMBER')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
       



