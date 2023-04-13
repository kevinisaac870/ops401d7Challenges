#!/usr/bin/python3

# Script:                       Ops Challenge 33
# Author:                       Kevin Isaac
# Date of latest revision:      20230301
# Purpose:                       Malware detection pt 3
# Attribution: Alex Wise

    #task
        # Successfully connect to the VirusTotal API
        # Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
        # Print to the screen the number of positives detected and total files scanned
        
# Main

import os
import requests

apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. "export API_KEY_VIRUSTOTAL= PUT KEY HERE", "echo $API_KEY_VIRUSTOTAL" SHoudl show your API KEY

hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 

# Send a request to the VirusTotal API to retrieve information about the file hash
response = requests.get('https://www.virustotal.com/api/v3/files/' + hash, headers={'x-apikey': apikey})

# Parse the JSON response from the API
json_response = response.json()

# Get the number of positives and total files scanned from the JSON response
positives = json_response['data']['attributes']['last_analysis_stats']['malicious']
total = json_response['data']['attributes']['last_analysis_stats']['total']

# Print the number of positives and total files scanned to the screen
print('Positives: ' + str(positives))
print('Total files scanned: ' + str(total))
