import argparse
import logging
import requests
import send_sms
import os
import time

DELAY = 60

def get_url_server():
    parser = argparse.ArgumentParser()
    parser.add_argument("URL", help= "you need write servers URL")
    server = parser.parse_args().URL 
    return server

if __name__ == '__main__':
    current_time = time.ctime()
    logging.basicConfig(filename='file.log', level=logging.INFO, format="%(levelname)s %(asctime)s %(message)s")
    URL = '{0}{1}'.format('https://', get_url_server())
    response = requests.get(URL)
    message = f', URL: {URL} - status_code: {response.status_code} '
    while True:
        try:
            response.raise_for_status()
            logging.info(message)
        except requests.exceptions.HTTPError:
            logging.error(message)
            send_sms.client.messages.create(
                body = message,
                from_ = send_sms.TWILLO_NUMBER,
                to = send_sms.TWILIO_MY_NUMBER
                )            
        time.sleep(DELAY)
