
#!/usr/bin/python3

# Script:                       Ops Challenge 18
# Author:                       Kevin Isaac
# Date of latest revision:      202300208
# Purpose:                       Automated Brute Force Wordlist Attack Tool Part 3 of 3

# Attribution: Working with Jose

import zipfile


def crack_password(password_list, obj):
	# Tracking line no. at which password is found
	idx = 0

	# Open file in read byte mode only as "rockyou.txt"
	# File contains some special characters and hence
	# UnicodeDecodeError will be generated
	with open(password_list, 'rb') as file:
		for line in file:
			for word in line.split():
				try:
					idx += 1
					obj.extractall(pwd=word)
					print("Password found at line", idx)
					print("Password is", word.decode())
					return True
				except:
					continue
	return False


password_list = "rockyou.txt"

zip_file = "gfg.zip"

# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)

# Count of number of words present in file
cnt = len(list(open(password_list, "rb")))

print("There are total", cnt,
	"number of passwords to test")

if crack_password(password_list, obj) == False:
	print("Password not found in this file")
