#!/usr/bin/env python3

# subprocess allows us to execute linux commands in python
import subprocess

def get_args():
    input_mac = input("Desired MAC: ")
    input_eth = input("Target Interface:  ")

    return input_mac, input_eth

def change_mac(input_mac, input_eth):
    subprocess.call(["ifconfig", input_eth, "down"]) 
    subprocess.call(["ifconfig", input_eth, "hw", "ether", input_mac]) 
    subprocess.call(["ifconfig", input_eth, "up"]) 
    # subprocess.call(["ifconfig"]) 
 
(input_mac, input_eth) = get_args()
change_mac(input_mac, input_eth)


