#!/usr/bin/python3


# Script:                       Ops Challenge 03
# Author:                       Kevin Isaac
# Date of latest revision:      20230118
# Purpose:       Uptime sensor tool that checks systems are responding and notifies by email

# Attribution: Marco and classmates

import os
import time
import datetime
import smtplib
from getpass import getpass
from decouple import config

# Ask the user for an email address and password to use for sending notifications.
def send_email():
        today = datetime.today()
        if current_ping == 0:
                message = "Host is Up", str(today)
        else:
                message = "Host is Down", str(today)
        email.sendmail(username, username, message)

email = smtplib.SMTP('smtp.gmaill.com', 465)

email.starttls()
username = config('username', default='')
password = config('password', default='')
email.login(username, password)

message = os.system("ping -c 1 8.8.8.8")

while True:
        last_ping = current_ping    
        current_ping = os.system("ping -c 1 8.8.8.8")
        print("ping -c 1 8.8.8.8")
        time.sleep(2)
        today = datetime.today()
        
        if current_ping == 0:
                print(str(today) + " Network Active to 8.8.8.8")
                #  print("Network Active")
        else:
                print(str(today) + " Network Inactive to 8.8.8.8")

        if current_ping != last_ping:
                send_email()


        

# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

