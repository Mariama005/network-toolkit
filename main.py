def subnet_calculator():
    import ipaddress
    user_ip = input("Enter an IP address with CIDR (e.g. 192.168.1.0/24): ")
    try:
        network = ipaddress.ip_network(user_ip, strict=False)
        print("Network Address:", network.network_address)
        print("Broadcast Address:", network.broadcast_address)
        print("Number of usable hosts:", network.num_addresses - 2)
    except ValueError:
        print("That doesn't look like a valid IP address with CIDR notation.")

def port_scanner():
    import socket
    target = input("Enter a host to scan (e.g. 127.0.0.1): ")
    print(f"Scanning {target}...")
    for port in range(1, 101):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

def ping_sweep():
    import os
    network_prefix = input("Enter the network prefix (e.g. 192.168.1): ")
    print(f"Scanning {network_prefix}.1 to {network_prefix}.254...")
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        response = os.system(f"ping -n 1 -w 300 {ip} > nul")
        if response == 0:
            print(f"{ip} is active")

def main():
    print("=== Network Toolkit ===")
    print("1. Subnet Calculator")
    print("2. Port Scanner")
    print("3. Ping Sweep")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        subnet_calculator()
    elif choice == "2":
        port_scanner()
    elif choice == "3":
        ping_sweep()
    else:
        print("Invalid choice.")

main()