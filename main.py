import requests
import keys

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
stock_difference = (abs(yesterday_close-previous_close)/yesterday_close)*100
if stock_difference >= 1:
    news_response = requests.get(news_endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    print(news_data[:3])





## STEP 3: alert user



#some formatting
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

