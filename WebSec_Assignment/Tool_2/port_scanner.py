import socket

target_ip = "216.24.57.1"
ports = [22, 80, 443]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()
 
 
#import nmap

#nm = nmap.PortScanner()

#target = "45.33.32.156"

#nm.scan(target, arguments="-sV -sC")

#for host in nm.all_hosts(): 
#    print("Host: %s (%s)" % (host, nm[host].hostname()))
 #   print("State: %s" % nm[host].state())
 #   for protocol in nm[host].all_protocols():
 #       print("Protocol: %s" %protocol)
 #       port_info = nm[host][protocol]
 #       for port, state in port_info.items():
 #           print("Port: %s\tState: %s" % (port, state))
 
