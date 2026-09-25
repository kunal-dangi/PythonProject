##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import smtplib
import datetime as dt
import random
import pandas as pd
data = pd.read_csv("birthdays.csv")

names = data["name"]
years = data["year"]
months = data["month"]
days = data["day"]
emails = data["email"]
current = dt.datetime.now()

current_day = current.day
current_month = current.month
current_year = current.year


for index, row in data.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        birthday_person = row["name"]
        birthday_email = row["email"]


