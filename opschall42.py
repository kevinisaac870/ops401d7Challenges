#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 42
# Author:                        Kevin Isaac
# Date of latest revision:       20230314
# Purpose:                       Ops Challenge: Attack Tools Part 2 of 3

Attribution: Working with Jose

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) TCP ACK Scan             \n""") ### DONE: Select what your third scan type will be
print("You have selected option: ", resp)

range = input("Add the port range\n")

### DONE: Prompt the user to type in a port range for this tool to scan


if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS', True)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU', True)
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    ### DONE: Add missing code block here
    
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sA', True)
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    ### TODO: Add missing code block here
    
elif resp >= '4':
    print("Please enter a valid option")
