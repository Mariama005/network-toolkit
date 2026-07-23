import socket
target = input("Enter a host to scan (e.g.,127.0.0.1): ")

print(f"Scanning host: {target}")

for port in range(1, 101): # Scanning ports from 1 to 101
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Set a timeout for the connection attempt
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Open")
    sock.close()