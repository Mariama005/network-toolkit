import os

network_prefix = input("Enter the network prefix (e.g., 192.168.1): ")

print(f"Scanning {network_prefix}.1 to {network_prefix}.254...")

for i in range(1, 255):
    ip = f"{network_prefix}.{i}"
    response = os.system(f"ping -n 1 -w 300 {ip} > nul")  # For Windows, use -n and -w; for Linux/Mac, use -c and -W
    if response == 0:
        print(f"{ip} is active")