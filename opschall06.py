#!/usr/bin/python3

# Script:                       Ops Challenge 06
# Author:                       Kevin Isaac
# Date of latest revision:      20230123
# Purpose:        Create a script that utilizes the cryptography library to: Encrypt/Decrypt - Send message

# Attribution: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python


# Import Libraries
from cryptography.fernet import Fernet
from os.path import exists

# Variab;e Declaration
user_exit = 'y'

def write_key():
    # calls the generate key methid and puts the key value in a variable called key
  key = Fernet.generate_key()
  # creates a file called key.key and writes the value stored in the key variable to the file
  with open("key.key", "wb") as key_file:
    key_file.write(key)



def load_key():
  # opens the file called key.key with readpermisiions and then read method reads the content
    return open("key.key", "rb").read()
key = load_key()


def encrypt_message():
  #creates a variable to store the message the user wants to encrypt
  user_message = input("What message would you like to encrypt? ")
  # encodes the message aka turns data fron a dtring to bytes
  encoded_message = user_message.encode()
  # intialize the Fernet class, manes it f (f could be anything you want to call it)
  f = Fernet(key)
  # Encrypt the message - pass the encoded message to be encrypted and store the result in a variable called encrypted_message
  encrypted_message = f.encrypt(encoded_message)
  print("Here is your encrypted message: ")
  print(encrypted_message)

def decrypt_message():
  user_input = input("Please provide message to be decrypted: ")

  decoded_message = str.encode(user_input)
  # Initialize Fernet class
  f = Fernet(key)
  decrypted_message = f.decrypt(decoded_message)
  print("This is your decrypted message: ")
  print(decrypted_message)

def encrypt_file():
  # Asking user to provide full path and storing in a variable called file_name
  file_name = input("Please enter full file path for desired encryptd file:\n")

  # This opens the file and reads the contents | below "file" can be anything as variable name
  with open(file_name, "rb") as secret_file:
    # Read contents of the file
    file_data = secret_file.read()
    f = Fernet(key)
  # Encrypt the contents of the file and save it in variable called encrypted_file
  encrypted_file = f.encrypt(file_data)

  # Write the encrypted data to file
  with open(file_name, "wb") as file:
      file.write(encrypted_file)

def decrypt_file():
  # Ask user for full file path to be decrypted
  file_name = input("Please enter the full file path for desired decrypted file:\n")

  # OPend encrptyed file and reads all contents and stores ina variable called file_data
  with open(file_name, "rb") as file:
    file_data = file.read()
    f = Fernet(key)
    # Decrypt the data
    decrypted_data = f.decrypt(file_data)

  # Writw the decrypted date to the file
  with open(file_name, "wb") as file:
    file.write(decrypted_data)




def ask_user():
    print("What would you like to do?")
    print("Mode 1 - Encrypt a File")
    print("Mode 2 - Decrypt a File")
    print("Mode 3 - Encrypt a Message")
    print("Mode 4 - Decrypt a Message")

    mode = input("Please make a selection: ")

    if (mode == "1"):
      encrypt_file()
      print("Your file was encrypted")
    elif (mode == "2"):
      decrypt_file()
      print("Your file was decrypted")
    elif (mode == "3"):
      encrypt_message()
      print("Your message was encrypted")
    elif (mode == "4"):
      decrypt_message()
      print("Your message was decrypted")
    else:
      print("Invaled Selectio, please try again!")

# Check of old key exists
key_exists = exists('./key.key')

# Check the key file exists and if not then cal  load_key finction to read the key
if key_exists:
    key = load_key()

else:
  # If key file doesn't exist then call the write key finc to generate a key
  # Ca;; the load_key function to read the new key and save it ina variable called key
    write_key()
    key = load_key()

while True:
# Infiniite loop that constantly prints user menu 
  ask_user()
  user_exit = input("Do you want to try again?")
  if user_exit == "n":
    print("The program is going to end ")
    break


      
