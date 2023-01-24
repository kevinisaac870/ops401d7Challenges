#!/usr/bin/python3

# Script:                       Ops Challenge 06
# Author:                       Kevin Isaac
# Date of latest revision:      20230123
# Purpose:        Create a script that utilizes the cryptography library to: Encrypt/Decrypt - Send message

# Attribution: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python


# Import Libraries
from cryptography.fernet import Fernet


def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)


write_key()
mode_choice = input()
key = load_key()
f = Fernet(key)


def load_key():
    return open("key.key", "rb").read()

def encrypt_message():
  user_message = input("What message would you like to encrypt? ")
  encoded_message = user_message.encode()
  f = Fernet(key)
  encrypted_message = f.encrypt(encoded_message)
  print("Here is your encrypted message: ")
  print(encrypted_message)

def decrypt_message():
  user_input = input("Please provide message to be decoded: ")
  decoded_message = user_input.decode()
  f = Fernet(key)
  decrypted_encrypted = f.decrypt(decoded_message)
  print(decrypted_encrypted)




def ask_user():
  choice = '0'
  while choice == '0':
  print("Please select from the list: ")
  print("1. Encrypt FIle\n2. Decrypt File\n3. Encrypt a Message\n 4. Decrypt a Message")

  # End
