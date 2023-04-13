#!/usr/bin/python3

# Script:                       Ops Challenge 27
# Author:                       Kevin Isaac
# Date of latest revision:      20230221
# Purpose:                       Logs pt 2
# Attribution: Alex Wise

    # Task 
        # Add a log rotation feature based on size

# Main
 
# Import necessary modules
import os
import time
import datetime
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
log_size = 250 # 1 MB
handler = RotatingFileHandler('log_file.log', mode='a', maxBytes=log_size, backupCount=2)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
logging.basicConfig(level=logging.DEBUG, handlers=[handler])

# Run an infinite loop to continuously check for internet connectivity
while True:
    # Get the current date and time
    now = datetime.datetime.now()

    try:
        # Ping the Google DNS server to check for internet connectivity
        response = os.system("ping -c 1 8.8.8.8")

        if response == 0:
            # Log an "info" message if the network is active
            logging.info("Network Active")
            # Print a message to the console indicating the network is active
            print("Network Active")
        else:
            # Log a "warning" message if the network is inactive
            logging.warning("Network Inactive")
            # Print a message to the console indicating the network is inactive
            print("Network Inactive")

    # Catch any exceptions that might be thrown while pinging the Google DNS server
    except Exception as e:
        # Log an "error" message with the exception details
        logging.error(f"Error occurred: {e}")
        # Print a message to the console indicating an error occurred
        print("Error occurred:", e)

    # Wait for 2 seconds before checking for connectivity again
    time.sleep(2)
