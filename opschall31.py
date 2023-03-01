#!/usr/bin/python

# Pair programmed
# Driver: Ben Arno
# Navigators: Kevin Isaac, Jose Cardozo

#Imports
import os
from sys import platform
#Ops401, Challenge2.py
def linuxSearch(file, dir):
  # DONE: Search each file in the directory by name
  # DONE: For each positive detection, print to the screen the file name and location
  # DONE: At the end of the search process, print to the screen how many files were searched and how many hits were found.
  print(f"SEARCHING {dir} for {file}...")
  os.system(f"find -D rates {dir} -name {file}")

def windowsSearch(file, dir):
  # DONE: Search each file in the directory by name
  # DONE: For each positive detection, print to the screen the file name and location
  # DONE: At the end of the search process, print to the screen how many files were searched and how many hits were found.
  os.system(f"dir .\{dir} \"{file}*\" /s")

# DONE: Prompt the user to type in a file name to search for
fName = input("Please enter a filename:\n")

# DONE: Prompt the user for a directory to search in
dName = input("Please enter the directory to search:\n")

if platform == "linux" or platform =="linux2":
  linuxSearch(fName, dName)
elif platform == "win32":
  windowsSearch(fName, dName)
