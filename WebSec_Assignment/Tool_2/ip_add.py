import socket

def get_ip_address(domain):
    return socket.gethostbyname(domain)

print(get_ip_address("blackbox.ai")) 


#import socket
#import sys
#from typing import Self

#if hasattr(socket, 'AF_PACKET'):
#    # Create a raw socket to capture packets
#    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
#    sock.bind((Self.interface, 0))
#else:
#    print("Error: AF_PACKET is not supported on this platform")
#    sys.exit(1)


#from typing import Self
#import pcap # type: ignore

#pc = pcap.pcap(Self.interface)
#while True:
#    packet = pc.next()
#    Self.process_packet(packet)