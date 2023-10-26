from twilio.rest import Client
import smtplib

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"
SERVER_LOCATION = "smtp.gmail.com"
EMAIL_PORT = 587
SENDER_EMAIL = "YOUR EMAIL"
SENDER_EMAIL_PASSWORD = "YOUR EMAIL PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, user_data, message):
        with smtplib.SMTP(SERVER_LOCATION, EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
            for user in user_data:
                connection.sendmail(SENDER_EMAIL, user["email"], message)
