#!/usr/bin/env python


# scapy module lets us work with network packets
import scapy.all as scapy
def py_scan(ip):

    # what subnet are we scanning?
    arp_request = scapy.ARP(pdst=ip)

    # Broadcast our ARP to all devices on the network with ff:ff:ff:ff:ff:ff
    broadcast_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # ARP packets contain two main parts 1. The subnet to scan 2. The broadcast address
    arp_request_packet = broadcast_destination/arp_request

    # Now lets catch the responses in a variable
    # note that we timeout after one second so our script doesnt just hang, waiting for a response
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    responses = scapy.srp(arp_request_packet, timeout=1)[0]

    # lets see who responded with a scapy function called .summary()
    # print(responses.summary())
    print('\n')
    print("IP\t\t\tAt MAC Address\n-------------------------------------------")
    for response in responses:
        print(response[1].psrc + "\t\t" + response[1].hwsrc)
        print("-------------------------------------------")

py_scan("10.0.2.0/24")
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    responses, ignored = scapy.srp(arp_request_packet, timeout=1)

    # lets see who responded with a scapy function called .summary()
    print(responses.summary())


<<<<<<< Updated upstream
<<<<<<< Updated upstream
py_scan("10.0.2.1/24")
>>>>>>> Stashed changes
=======
py_scan("10.0.2.1/24")
>>>>>>> Stashed changes
=======
py_scan("10.0.2.1/24")
>>>>>>> Stashed changes
