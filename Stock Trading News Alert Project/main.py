import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "ZA5FTFO7BSVTWS9B"
API_KEY_NEWS = "f42bdce3a48045a69b87fa8de59b745f"
# Twilio
ACCOUNT_SID = "[your_acc_sid]"
AUTH_TOKEN = "[your_auth_token]"

articles = []

def get_news():
    global articles
    url = (f"https://newsapi.org/v2/everything?"
           f"q={COMPANY_NAME}"
           f"&language=en"
           f"&from={yesterday_date}"
           f"&to={yesterday_date}"
           f"&sortBy=popularity"
           f"&apiKey=f42bdce3a48045a69b87fa8de59b745f")
    r = requests.get(url)
    data = r.json()

    articles = [{"title": data["articles"][i]["title"],
                 "description": data["articles"][i]["description"]}
                for i in range(3)]


def send_sms():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    if percentage_difference > 0:
        arrow_img = "🔺"
    else:
        arrow_img = "🔻"

    message_body = (
        f"{STOCK}: {arrow_img}{'%.2f' % percentage_difference}\n"
        f"Headline: {articles[0]['title']}\n"
        f"Brief: {articles[0]['description']}\n"
        f"Headline: {articles[1]['title']}\n"
        f"Brief: {articles[1]['description']}\n"
        f"Headline: {articles[2]['title']}\n"
        f"Brief: {articles[2]['description']}\n"
    )
    message = client.messages.create(
        from_="+18316235899",
        body=message_body,
        to="+48793480033"
    )

    print(message.sid)


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY_STOCK}'
r = requests.get(url)
data = r.json()

yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
day_before_yesterday = datetime.datetime.today() - datetime.timedelta(days=2)

yesterday_date = f"{yesterday.year}-{yesterday.month}-{yesterday.day}"
day_before_yesterday = f"{day_before_yesterday.year}-{day_before_yesterday.month}-{day_before_yesterday.day}"

yesterday_close_price = float(data["Time Series (Daily)"][yesterday_date]["4. close"])
day_before_yesterday_close_price = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

percentage_difference = ((yesterday_close_price - day_before_yesterday_close_price)
                         / day_before_yesterday_close_price) * 100

if percentage_difference < -0.1 or percentage_difference > 0.1:
    get_news()
    send_sms()


