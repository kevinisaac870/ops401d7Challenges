#!/usr/bin/python3

# Script:                       Ops Challenge 16
# Author:                       Kevin Isaac
# Date of latest revision:      20230206
# Purpose:         Develop a custom tool that performs brute force attacks

# Attribution: Marco, Zoom video and classmates.


import time, getpass

# Offensive
def iterator():
  path=input("Please enter dictionary file path:\n")
  doc=open(path)
  contents=doc.readline()
  print()
  
  # Loop
  while contents:
    print(contents.rstrip())
    contents=doc.readline()
    time.sleep(1)


# Defensive
def defender():
  string=getpass.getpass("Please enter password to query:\n")
  path=input("Please enter dictionary file path:\n")
  doc=open(path)
  contents=doc.readline()
  answer=False

  # Loop
  while contents:
    contents.rstrip()
    contents=doc.readline()

    if contents.rstrip() == string:
      answer=True
      break
    
  if answer:
    print("\nFile contained entered string. ")

  else:
    print("\nFile did NOT contain entered string. ")

iterator()
defender()