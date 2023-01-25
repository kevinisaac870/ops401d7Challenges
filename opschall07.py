#!/usr/bin/python3

# Script:                       Ops Challenge 07
# Author:                       Kevin Isaac
# Date of latest revision:      20230124
# Purpose:        Create a script that utilizes the cryptography library to: Encrypt/Decrypt - Send message
# Purpose:        Recursively encrypt/decrypt a single folder and all its contents

# Attribution: Marco, classmates and below:
# https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/
# https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/

import os
from cryptography.fernet import Fernet
from os.path import exists

# Begin a recursive directory crawl
for root, dirs, files in os.walk(".", topdown=True):
    # For each hit, concatenate the current directory path to left of result
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

def directory_crawl():
    # Start a recursive directory crawl
    for root, dirs, files in os.walk(".", topdown=True):
        # For each hit, concatenate the directory path to left of result
        for file in files:
            recursive_encrypt(filename)

def recursive_encrypt(filename):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open (filename, "wb") as file:
        file.write(encrypted_file)

# Function that generates a key
def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    
    # Creates file key.key and saves the value into a file
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Function that loads the generated key
def load_key():
    # Loads the key from the current directory named `key.key`
    # Read method reads the content
    return open("key.key", "rb").read()

# Function that encrypts a folder and all the content inside of it
def encrypt_folder():
    # Asking the full folder path to be encrypted
    path = input("Enter the folder path to be encrypted")

    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            recursive_encrypt(filename)

def recursive_encrypt(filename):
    
    # This opens the file and reads the contents
    with open(filename, "rb") as file:
        # This reads the contents of the file and saves it in a variable called file_data
        file_data = file.read()

    # Initialize the Fernet class
    f = Fernet(key)

    # Encrypt the contents of the file and save in a variable called encrypted_file
    encrypted_file = f.encrypt(file_data)

    # Write the encrypted data to a file
    with open(filename, "wb") as file:
        file.write(encrypted_file)


# Function that decrypts a folder and all the content inside of it
def decrypt_folder():
    # Ask the path to be decrypted
    path = input("Enter the folder path to be decrypted")
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            recursive_decrypt(filename)

def recursive_decrypt(filename):
    # This opens the file and reads the contents
    with open(filename, "rb") as file:
        # This reads the contents of the file and saves it in a variable called file_data
        file_data = file.read()

    # Initialize the Fernet class
    f = Fernet(key)

    # Encrypt the contents of the file and save in a variable called decrypted_file
    decrypted_file = f.decrypt(file_data)

    # Write the decrypted data to a file
    with open(filename, "wb") as file:
        file.write(decrypted_file)



# Function that gives a user a menu
def ask_user():
    mode = input("\nWhat would you like to do? \n1 - Encrypt a folder \n2 - Decrypt a folder")

    if (mode == "1"):
        encrypt_folder()
        print("Folder Encrypted!")
    elif (mode == "2"):
        decrypt_folder()
        print("Folder Decrypted!")
    elif ((mode != "1") and (mode != "2")):
        print("Wrong Choice! Choose again.")
    
key_exists = exists('./key.key')

# Check if the key file exists then call the load_key funtion to read it
if key_exists:
    key = load_key()
else:
    write_key()
    key = load_key()

# Infinite loop for user menu
# USE CONTROL C TO EXIT LOOP!!!
while True:
     ask_user()
