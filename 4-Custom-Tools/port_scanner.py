#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

# Define the target
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print(f"[-] Error: Hostname '{sys.argv[1]}' could not be resolved.")
        sys.exit(1)
else:
    print("[-] Invalid arguments. Usage: python3 port_scanner.py <IP/Domain>")
    sys.exit(1)

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time Started:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 50)

# Common penetration testing ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080]

try:
    for port in ports:
        # Using a context manager automatically closes the socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0) # 1 second timeout
            
            # Attempt TCP handshake connection
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port:<5} is OPEN")
                
except KeyboardInterrupt:
    print("\n[-] Exiting script via user interruption.")
    sys.exit(0)
