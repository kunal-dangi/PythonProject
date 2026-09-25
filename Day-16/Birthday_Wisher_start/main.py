import random
import smtplib
import datetime as dt
import random

current = dt.datetime.now()
day = current.weekday()
if day == 4:
    my_email = "kunaldangi065@gmail.com" # your email here
    my_password = "Kunal" # your password here!

    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quotes = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password) # have to turn of 2 factor verification before using this and
                                                            # also on less secure app access on!!
        connection.sendmail(from_addr=my_email, to_addrs="kunaldangi165@gmail.com",
                        msg= f"Subject:Quote For You!\n\n{quotes}") # just write subject like this
                                                                        # and use \n\n to write body afterward
    print(f"Working Quote:  {quotes}")
