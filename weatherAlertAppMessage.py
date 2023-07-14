import smtplib
import ssl
import configparser
from email.message import EmailMessage


def getMessage():

    config = configparser.ConfigParser()
    config.read('email.env')

    sender_email = str(config['EMAIL']['SENDER_EMAIL'])
    receiver_email = str(config['EMAIL']['RECEIVER_EMAIL'])
    city_name = str(config['EMAIL']['CITY_NAME'])

    message = EmailMessage()
    message['Subject'] = 'Weather Alert'
    message['From'] = sender_email
    message['To'] = receiver_email

    message.set_content('Be aware of weather problems in ' + city_name)

    print(message)
    
    return message