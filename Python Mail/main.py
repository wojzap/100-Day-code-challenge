import datetime as dt
import random
import smtplib


# Put your email and password
MY_EMAIL = ""
PASSWORD = ""

with open("quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()
    random_quote = random.choice(quotes_list)

current_weekday = dt.datetime.now().weekday()

if current_weekday == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Hello boss!\n\n{random_quote}"
        )


