'''
Sending an email using python smtplib library

import smtplib

my_email = "myemail.com"
pswrd = "mypassword"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=pswrd)
connection.sendmail(from_addr=my_email, to_addrs="subjectemail@gmail.com", msg="SubjectTest Email\n\nThis is a test email")

connection.close()
'''

import smtplib
import datetime as dt
import random

MY_EMAIL = "myemail@email.com"
MY_PASSWORD = "abcde@123"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("text.txt") as file:
        text = file.readline()
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Test\n\n{text}"
            )
