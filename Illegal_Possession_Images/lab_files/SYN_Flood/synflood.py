from scapy.all import *

def send_syn(target_ip_address, target_port, number_of_packets_to_send = 4, size_of_packet = 65000):
	ip = IP(dst=target_ip_address)
	tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
	raw = Raw(b"X" * size_of_packet)
	p = ip / tcp / raw
	send(p, count=number_of_packets_to_send, verbose=0)
	print('send_syn(): Sent ' + str(number_of_packets_to_send) + ' packets of '+ str(size_of_packet) + 'size to ' + target_ip_address + ' on port ' + str(target_port))

send_syn(target_ip_address = "127.0.0.1", target_port= 80)