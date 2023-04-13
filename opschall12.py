#!/usr/bin/python3

# Script:                       Ops Challenge 12
# Author:                       Kevin Isaac
# Date of latest revision:      20230131
# Purpose:      Ops Challenge: Network Security Tool with Scapy Part 2 of 3
# Attribution from Kevin Isaac: Alex Wise

    # Task
        #Add the following features to your Network Security Tool:
            #User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
            #ICMP Ping Sweep tool
            #Prompt user for network address including CIDR block, for example “10.10.0.0/24”
                  #Create a list of all addresses in the given network
                  #Ping all addresses on the given network except for network address and broadcast address
                  #If no response, inform the user that the host is down or unresponsive.
                  #If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
                        #Otherwise, inform the user that the host is responding.
                        #Count how many hosts are online and inform the user.

                  
              


# Main

# Import library
from scapy.all import sr1, IP, TCP, ICMP, srp
import sys
import ipaddress

# User menu 
while True:
  print("Choose scan mode:")
  print("1. TCP port range scan")
  print("2. ICMP ping sweep")
  mode = input("Which would you like? (1 or 2): ")
  if mode in ["1", "2"]:
    break
  print("No other options. Please try again.")

if mode == "1":
  # TCP port range scan
  # Set the target host and port range to scan
  host = input("Enter target host: ")
  port_range = [int(p) for p in input("Enter port range separated by space (e.g. 22 80 443): ").split()]
  src_port = 22

  # Iterate over each port in the specified range
  for dst_port in port_range:
    # Craft and send a TCP SYN packet to the target host and port
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"),timeout=1,verbose=0)

    # Check the response flags to determine if the port is open, closed, or filtered
    if response[TCP].flags == 0x12:
      print("Port %d is open." % dst_port)
      sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"))
    elif response[TCP].flags == 0x14:
      print("Port %d is closed." % dst_port)
    else:
      print("Port %d is filtered." % dst_port)

elif mode == "2":
  # ICMP ping sweep
  # Prompt user for network address including CIDR block
  network = input("Enter network address with CIDR block (e.g. 192.168.0.0/24): ")
  network_obj = ipaddress.ip_network(network)
  broadcast = str(network_obj.broadcast_address)
  network = str(network_obj.network_address)
  
  # Create a list of all addresses in the given network
  hosts = [str(host) for host in network_obj.hosts()]
  
  online_count = 0
  
  # Ping all addresses on the given network except for network addresses and broadcast address
  for host in hosts:
    resp = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)
    if resp is None:
      print(f"{host} is down or unresponsive")
    elif resp.getlayer(ICMP).type == 3 and resp.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
      print(f"{host} is actively blocking ICMP traffic")
    else:
      print(f"{host} is responding")
      online_count += 1
  
  # Count how many hosts are online and inform the user
  print(f"{online_count} hosts are online")

  # End
