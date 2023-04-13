

#!/usr/bin/python3

# Script:                       Ops Challenge 32
# Author:                       Kevin Isaac
# Date of latest revision:      20230228
# Purpose:                       Malware detection pt 2
# Attribution: Alex Wise

    # Task
        # Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen
        # For each file scanned within the scope of your search directory 
            # generate the files MD5 using hashlib
            # assign the MD5 hash to a variable
            # print the variable to the screen along with a timestamp, file name, file size and complete (NOT SYMBOLIC) file path

# Main

import os
import hashlib
import datetime

# Prompt the user for a directory to search in
directory = input("Enter the directory to search in: ")

# Initialize counter for files searched
files_searched = 0

# Recursively search each file and folder in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # For each file scanned, calculate the MD5 hash and print its information
        files_searched += 1
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        with open(file_path, 'rb') as f:
            file_content = f.read()
            md5_hash = hashlib.md5(file_content).hexdigest()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] {file} ({file_size} bytes) - {file_path}: {md5_hash}")

# At the end of the search process, print to the screen how many files were searched
print("Searched", files_searched, "files.")
