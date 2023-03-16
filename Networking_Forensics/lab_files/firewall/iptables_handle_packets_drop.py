#!/usr/bin/env python3

import argparse
import os
import signal
import sys

from netfilterqueue import NetfilterQueue
from scapy.layers.inet import IP
from scapy.sendrecv import send


def iptables_add_rule(ip_address):
    os.system(f"iptables -A INPUT -s {ip_address} -j NFQUEUE --queue-num 1")


def iptables_remove_rule(ip_address):
    os.system(f"iptables -D INPUT -s {ip_address} -j NFQUEUE --queue-num 1")


def handle_packet(packet):
    ip = IP(packet.get_payload())
    source_ip = ip.src
    print(f"Receiving packet from {source_ip}")

    if source_ip == args.source_ip:
        print(f"Dropping packet from {source_ip}")
        packet.drop()
        print("================================")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Python script to demonstrate iptables functions")
    parser.add_argument("source_ip", help="Source IP address to filter")
    return parser.parse_args()


def main():
    if os.geteuid() != 0:
        print("You must be root to run this script.")
        sys.exit(1)

    global args
    args = parse_arguments()

    iptables_add_rule(args.source_ip)

    q = NetfilterQueue()
    q.bind(1, handle_packet)

    try:
        print("Waiting incoming packets...")
        q.run()
    except KeyboardInterrupt:
        print("Exiting...")
        q.unbind()
        iptables_remove_rule(args.source_ip)
        print("Rules are removed...")


if __name__ == "__main__":
    main()
