#!/usr/bin/env python3


# Script:                        Ops 401 Challenge 37
# Author:                        Kevin Isaac
# Date of latest revision:       20230307
# Purpose:                       Cookie Capture Capades

Attribution: Alex Wise

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
headers = {'Cookie': '; '.join([str(x)+'='+str(y) for x,y in cookie.items()])}
response = requests.get(targetsite, headers=headers)
# - Generate a .html file to capture the contents of the HTTP response
filename = "response.html"
with open(filename, "w") as f:
    f.write(response.text)
print(f"Response saved to {filename}")
# - Open it with Firefox
webbrowser.get('firefox').open(filename)
# Stretch Goal
# - Give Cookie Monster hands
