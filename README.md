# Check if the service is up
This script allows you to get sms notifications if the service is down (there is a check every 60 seconds).

# Usage
1. Prepare a working directory and execute these commands:
```
git clone https://github.com/rinAkhm/checker-server.git
cd checker-server

pip install -r requirements.txt
 
echo "TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_NUMBER=
TWILIO_MY_NUMBER=" > .env
```
2. Register on [twilio.com](twilio.com), create a number and copy `sid`, `token`, `twilio number` and `your number` to `.env` file.

3. Run the script providing the service you want to check
```
python check_service.py <domain-url>
```

for example 
```
python check_service.py yandex.ru
```