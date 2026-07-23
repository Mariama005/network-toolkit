import ipaddress
user_ip=input("Enter an IP address with CIDR (e.g., 192.168.1.10/24): ")

try:
    network = ipaddress.ip_network(user_ip, strict=False)
    print("Network Address:", network.network_address)
    print("Broadcast Address:", network.broadcast_address)
    print("Number of usable hosts:", network.num_addresses - 2)
except ValueError :
    print("That is not a valid IP address with CIDR notation. Please enter a valid IP address.")    
