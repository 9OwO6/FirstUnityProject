import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "wyhjlb@gmail.com"
    # get from gmail account, go to google, security, app passwords, app, other.
    # password = "xxxxxxxxxxxxxx"

    # protect password
    password = os.getenv("PASSWORD")

    receiver = "wyhjlb@gmail.com"

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
