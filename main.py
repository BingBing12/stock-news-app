import requests
import keys

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "apikey": keys.stock_key,
    "symbol": STOCK
}

stock_endpoint = "https://www.alphavantage.co/query"
response = requests.get(stock_endpoint, params=stock_params)
response.raise_for_status()
stock_data = response.json()
close_data = stock_data["Time Series (Daily)"]
yesterday_close = float(close_data.popitem()[1]["4. close"])
previous_close = float(close_data.popitem()[1]["4. close"])
stock_difference = ((yesterday_close-previous_close)/yesterday_close)*100
if stock_difference >= 5:
    print("get news")


## STEP 2: Use https://newsapi.org to get relevant news


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

