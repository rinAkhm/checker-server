import argparse
import logging
import requests


def get_url_server():
    parser = argparse.ArgumentParser()
    parser.add_argument("URL", help= "you need write servers URL", default='yandex.ru')
    server = parser.parse_args().URL 
    return server

if __name__ == '__main__':
    URL = '{0}{1}'.format('https://', get_url_server())
    # logging.basicConfig(filename='logFile.log', format='%(levelname)s %(asctime)s %(message)s')
    reponse = requests.get(URL)
    print (reponse.status_code)
    try:
        print(f'Status: {reponse.status_code}. {URL} is available ')
    except requests.exceptions.HTTPError as error:
        message = f'Error. Status: {error.response.status_code}. {URL} is not available.'

