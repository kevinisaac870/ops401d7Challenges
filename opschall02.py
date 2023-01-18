#!/usr/bin/python3

# Script:                       Ops Challenge 02
# Author:                       Kevin Isaac
# Date of latest revision:      20230117
# Purpose:      Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down


import os
import time
from datetime import datetime


# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
while True:
    var1 = os.system("ping -c 1 8.8.8.8")
    print("ping -c 1 8.8.8.8")
    time.sleep(2)
    today = datetime.today()

    if var1 == 0:
        print(str(today) + " Network Active to 8.8.8.8")
        #  print("Network Active")
    else:
        print(str(today) + " Network Inactive to 8.8.8.8")
        # print("Network Inactive")

    # The following are for personal reference:
    # print(str(today) + " Network Active to 8.8.8.8")
    # print(today)
    # print("Current year:", today.year)
    # print("Current month:", today.month)
    # print("current day:", today.day)

# End
