#!/usr/bin/env python

import scapy.all as scapy

# scapy.ARP(op=2) = allows us to receive packets
# scapy.ARP(pdst) = ip of target
# scapy.ARP(hwdst) = MAC of target
# scapy.ARP(srdst) = router gateway IP, we are MitM'ing

packet = scapy.ARP(op=2, pdst='', hwdst='',psrc='10.0.2.2' )
