STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
News_API = "78951289168540d9af011c6ef82c35ac"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """


import requests

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "0QM1ERFR91XKBBQS"
}

response_stock = requests.get("https://www.alphavantage.co/query", params=stock_params)
response_stock.raise_for_status()
data = response_stock.json()["Time Series (Daily)"]
# print(data)
data_list = list(data.values())
open_daily = data_list[0]
att_open = open_daily["1. open"]
att_close = open_daily["4. close"]
difference_1st_day = abs(float(data_list[1]["4. close"]) - float(att_close))
difference_2nd_day = abs(float(data_list[2]["4. close"]) - float(att_close))
print(difference_1st_day, difference_2nd_day)
diff_1_percent = (difference_1st_day / float(att_close)) * 100
print(diff_1_percent)
diff_2_percent = (difference_2nd_day / float(att_close)) *100
print(diff_2_percent)

news_params = {
    "apiKey": News_API,
    "qInTitle": COMPANY_NAME
}
response_news = requests.get("https://newsapi.org/v2/everything", params=news_params)
response_news.raise_for_status()
data_news = response_news.json()["articles"]
first_three = data_news[:3]
print(first_three)
formatted_message = [f"Headline:{data_news['title']}, \n Brief:{data_news['content']}" for data_news in first_three]
if diff_1_percent * 10 >= 1 and diff_2_percent *10 >= 1:
    print(formatted_message)
else:
    pass


# then do your twilio shit