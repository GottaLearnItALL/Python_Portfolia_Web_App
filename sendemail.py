import smtplib, ssl
import os


def send_email(message,receiver):
    host = "smtp.gmail.com"
    port = 465
    #receiver = "iamkami.2023@gmail.com"
    username = "iamkami.2023@gmail.com"
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver,message)




