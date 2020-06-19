#!/usr/bin/env python3

# subprocess allows us to execute linux commands in python
import subprocess

input_mac = input("Desired MAC: ")
input_eth = input("Target Interface:  ")


subprocess.call(["ifconfig", input_eth, "down"]) 
subprocess.call(["ifconfig", input_eth, "hw", "ether", input_mac]) 
subprocess.call(["ifconfig", input_eth, "up"]) 
# subprocess.call(["ifconfig"]) 
 