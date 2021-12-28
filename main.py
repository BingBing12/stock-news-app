import requests
import keys
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "apikey": keys.stock_key,
    "symbol": STOCK
}
news_params = {
    "apiKey": keys.news_key,
    "qInTitle": COMPANY_NAME
}
stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
response = requests.get(stock_endpoint, params=stock_params)
response.raise_for_status()
stock_data = response.json()
close_data = stock_data["Time Series (Daily)"]
yesterday_close = float(close_data.popitem()[1]["4. close"])
previous_close = float(close_data.popitem()[1]["4. close"])
stock_difference = round((abs(yesterday_close - previous_close) / yesterday_close) * 100)
if stock_difference >= 5:
    news_response = requests.get(news_endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]

    account_sid = keys.sid
    auth_token = keys.auth
    client = Client(account_sid, auth_token)
    for news in news_data:
        if yesterday_close > previous_close:
            symbol = "🔺"
        else:
            symbol = "🔻"
        text = f"{STOCK}: {symbol}{stock_difference} Headline: {news['title']} Brief: {news['description']}"
        print(text)
        message = client.messages.create(
            body=text,
            from_=keys.phone,
            to=keys.verified_phone
        )
        print(message.status)

