
#!/usr/bin/python3

# Script:                       Ops Challenge 26
# Author:                       Kevin Isaac
# Date of latest revision:      20230220
# Purpose:                       Logs
# Attribution: Alex Wise

        #Task
            # Add logging capabilities to your Python tool using the logging library
            # Experiment with log types. Build in some error handling, then induce some errors. Send log data to a file in the local directory
            # Confirm your logging feature is working as expected



# Main



# Import necessary modules
import os
import time
import datetime
import logging

# Set up logging
logging.basicConfig(filename='log_file.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

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
