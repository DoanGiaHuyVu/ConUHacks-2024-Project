from twilio.rest import Client
import datetime as dt
from main import *


def sending_newsletter(user_email):
    import smtplib

    my_email = "adamosayinghi@gmail.com"
    password = "tqlfrjigxyetsixn"

    # Yahoo: smtp.mail.yahoo.com (SMTP info)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # tls: Transport Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=user_email,
                            msg="Subject:Hello student\n\nWelcome to the USSA community! We're thrilled to have you on board, ready to embark on a monthly journey of learning marvels.")
def activate_newsletter(user_email):
    months_in_a_year = 1
    testing_time = dt.datetime(year=dt.datetime.now().year, month=dt.datetime.now().month, day=1)
    while months_in_a_year != 12:
        if testing_time == dt.datetime.now():
            sending_newsletter(user_email)
            months_in_a_year -= 1

# account_sid = "AC7c86b3e0c201bde277a8b74c7646350d"
# auth_token = "19898c10d58a8626f388bb7d8a8aad80"
#
# message = "It's going to rain today :'("
#
# client = Client(account_sid, auth_token)
# message = client.messages \
#         .create(
#         body=message,
#         from_='+15854878959',
#         to='+1 514 963 1025' # user input
#     )
