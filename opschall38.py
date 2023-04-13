#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: This script detects cross-site scripting (XSS) vulnerabilities on a given URL
# Date:        20230308
# Modified by: Alex Wise
# Attribution from Kevin Isaac: Alex Wise

    # Task
        # Fully annotate any missing comments and populate any missing variables/code
        # Test the script in Web Security Dojo to confirm the output is correct
            # This target URL should yield a positive vulnerability detection: https://xss-game.appspot.com/level1/frame
                # This target URL should yield a negative vulnerability detection: http://dvwa.local/login.php

# Import necessary libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# Get all forms in the HTML content of a given URL
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Get details of a form, including its action, method, and input fields
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Submit a form with a given value and get the response content
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Scan a given URL for XSS vulnerabilities
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    # HTTP and JS code to cause an XSS vulnerability by creating an alert prompt with some text
    js_script = "<script>alert('XSS');</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main function to run the script
if __name__ == "__main__":
    # Get URL input from user
    url = input("Enter a URL to test for XSS:")
    # Call the scan_xss function and print the result
    if scan_xss(url):
        print("Positive detection: Vulnerability found.")
    else:
        print("Negative detection: No vulnerability found.")


# POSITIVE
#  /bin/python3 /home/eighty6face/Ops-Course-Challengeighty6face@eighty6face:~/Ops-Course-Challenges$ /bin/python3 /home/eighty6face/Ops-Course-Challenges/Ops401challenge38.py
Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
[+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
[+] XSS Detected on https://xss-game.appspot.com/level1/frame
[*] Form details:
{'action': '',
 'inputs': [{'name': 'query',
             'type': 'text',
             'value': "<script>alert('XSS');</script>"},
            {'name': None, 'type': 'submit'}],
 'method': 'get'}
Positive detection: Vulnerability found.
