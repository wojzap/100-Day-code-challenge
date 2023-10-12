
import pandas as pd
import datetime as dt
import random
import smtplib
import account_data

LETTER_TEMPLATES_PATHS = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

LOGIN = account_data.email
PASSWORD = account_data.password


def personalize_letter(birthday_person):
    with open(random.choice(LETTER_TEMPLATES_PATHS), "r") as template_file:
        template = template_file.read()
        letter = template.replace("[NAME]", birthday_person["name"])

    return letter


def send_email(birthday_person, letter):
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(LOGIN, PASSWORD)
        connection.sendmail(from_addr=LOGIN, to_addrs=birthday_person["email"], msg=f"Subject: {birthday_person['name']}, Happy Birthday!\n\n"
                                                                                    f"{letter}")


birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays_data.to_dict(orient="records")

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

for birthday_person in birthdays_dict:
    if birthday_person["month"] == current_month and birthday_person["day"] == current_day:
        letter = personalize_letter(birthday_person)
        send_email(birthday_person, letter)

