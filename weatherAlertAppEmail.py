import smtplib
import ssl
import configparser
from email.message import EmailMessage
import weatherAlertAppMessage

def sendMail():

    config = configparser.ConfigParser()
    config.read('email.env')

    port = config['EMAIL']['PORT']
    smtp_server = str(config['EMAIL']['SMTP_SERVER'])
    sender_email = str(config['EMAIL']['SENDER_EMAIL'])
    password = str(config['EMAIL']['PASSWORD'])

    message = weatherAlertAppMessage.getMessage()

    print("test")


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)