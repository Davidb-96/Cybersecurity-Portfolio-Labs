#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

# Define the target (Example: TryHackMe Target IP)
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("[-] Invalid arguments. Usage: python3 port_scanner.py <IP>")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

# Common penetration testing ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080]

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.0) # 1 second timeout
        
        # Attempt connection
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\n[-] Exiting script via keyboard interrupt.")
    sys.exit()
except socket.gaierror:
    print("\n[-] Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\n[-] Could not connect to server.")
    sys.exit()
