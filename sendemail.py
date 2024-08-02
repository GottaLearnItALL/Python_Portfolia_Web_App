import smtplib,ssl

host = "smtp.gmail.com"
port = 465


username = "iamkami.2023@gmail.com"
password = "wmbo wcmr cshc xyiz "

context = ssl.create_default_context()
receiver = "iamakami.2023@gmail.com"

message = """
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


