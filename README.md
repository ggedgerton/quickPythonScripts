# Quick Scripts

Python Black Hat Tutorials and Scripts to get you started with your adventure into the world of Cyber Security
- - -

## Mac Address Spoofing and Me

<details> 
  <summary>Why do we want to spoof a MAC Address?</summary>

<<<<<<< Updated upstream

Spoofing a MAC Address allows us to  bypass certain access control lists 
=======
> Spoofing a MAC Address allows us to  bypass certain access control lists 
>>>>>>> Stashed changes
</details>

**How Can We Change Our MAC from the Linux CL?**

1. Check our MAC Address

![ifconfig](./image/ifconfig.png)

    note my interface is eth0 and my MAC Address 08:00:27:23:ff:90

2. Linux Commands to change our MAC 

![ifconfig](./image/manualChange.png)

3. Confirm our MAC was changed

![ifconfig](./image/changedMac.png)
    
     My new MAC address is 66:55:44:33:22:11

<details> 
  <summary>So what tools/libraries/modules can we use in Python to automate this process?</summary>

>This [module](https://docs.python.org/3/library/subprocess.html) will let us use command line arguments in our python script
> How do we get user input?

</details>

[Mac Changer Script](/MACchanger.py)

<details> 
  <summary>Besides the obvious <i>allows us to bypass ACL</i>, why would a hack spoof a MAC address?
  </summary>

> To hide on a network or impersonate another device.
</details>

## Netscanning With Python

*This simple network scanner will function similar to Kali Linux's Net Discover*

<details> 
  <summary>For this scanner I am going to send out ARP requests instead of pinging. Why is this preferrable in this instance?
</summary>

> We are assuming we are already on the network, so we don't need to ask devices if they're up or not with a ping, we can ask them who they are with an ARP request.
</details>

<details> 
  <summary>Why does the python script broadcast to "ff:ff:ff:ff:ff:ff"?
</summary>

> When we don't know the MAC address we use the broadcast MAC destination as "ff:ff:ff:ff:ff:ff" as a place holder, so this message will reach all computers on our network. Once we get a reply from a device, we replace "ff:ff:ff:ff:ff:ff" with the known MAC address.
</details>


