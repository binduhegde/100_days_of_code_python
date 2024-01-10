##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd 
import smtplib
import datetime as dt

now = dt.datetime.now()
today_day = now.day # todays day
today_month = now.month # todays month

# from email id and password
EMAIL_ID = 'binduhegdee@gmail.com'
PASSWORD = "utan tcxs nxdc uhfd"

def smtp_sendmail(from_email, password, to_email, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=message)
    except Exception as e:
        print(f"failed: {e}")
    else:
        print("sent successfully")


df = pd.read_csv('birthdays.csv')
# df of the items whose birthday is today
birthdays_today = df[(df['month']== today_month) & (df['day'] == today_day)]
# print(birthdays_today)

# reading and saving the content of letter.txt
with open('letter.txt') as letter:
    letter_content = letter.read()

# iterating through people whose bday is today and sending them the wishing mail.
for ind in birthdays_today.index:
    message = letter_content.replace("[NAME]", birthdays_today['name'][ind])
    smtp_sendmail(from_email=EMAIL_ID, password=PASSWORD, to_email=birthdays_today['email'][ind], message=message)
