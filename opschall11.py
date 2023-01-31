#!/usr/bin/python3

# Script:                       Ops Challenge 11
# Author:                       Kevin Isaac
# Date of latest revision:      20230130
# Purpose:        

# Attribution: Marco, Zoom video and classmates.

# This is not completed.

# import libraries
import sys
from scapy.all import sr1, IP, ICMP, TCP

# Take IP or name as first parameter, send an ICMP echo request packet then display return packet
# p = sr1(IP(dst=sys.argv[2])/ICMP())
# if p:
#   p.show()

# Example 2

# Define target host band TCP port to scan
host = "scanme.nmap.org"
port_range = [22, 80, 443 ]
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

if(response.getlayer(TCP).flags == 0x12):
  print("Port 22 is open")
else:
  print("The port is closed")
