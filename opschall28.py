#!/usr/bin/python3

# Script:                       Ops Challenge 28
# Author:                       Kevin Isaac
# Date of latest revision:      20230222
# Purpose:                       Logs pt 3
# Attribution: Alex Wise


    # Task
        # Use StreamHandler and FileHandler in your Python script
            # FileHandler should write to a local file.
            # StreamHandler should output to the terminal


# Main

import os 
import time 
import datetime 
import logging 
from logging.handlers import RotatingFileHandler 
from logging import StreamHandler 

log_size = 250 

# Create a file handler to write log messages to a local file
file_handler = RotatingFileHandler('log_file.log', mode='a', maxBytes=log_size, backupCount=2)

# Set the format of the log messages for the file handler
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

# Create a stream handler to output log messages to the terminal
stream_handler = StreamHandler()

# Set the format of the log messages for the stream handler
stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

# Get the root logger and set its level to DEBUG
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

# Add the file and stream handlers to the root logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Run an infinite loop to continuously check for internet connectivity
while True:
    now = datetime.datetime.now() 
    try:
        response = os.system("ping -c 1 8.8.8.8") # Ping the Google DNS server to check for internet connectivity

        if response == 0: 
            logging.info("Network Active") 
            print("Network Active") 
        else: 
            logging.warning("Network Inactive") 
            print("Network Inactive") #
    except Exception as e: 
        logging.error(f"Error occurred: {e}") 
        print("Error occurred:", e) 

    time.sleep(2) 
