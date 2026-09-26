import socket

target = input("Enter an IP or website to scan: ")
ip = socket.gethostbyname(target)
print(f"Scanning {target} ({ip})...\n")

for port in range(7, 9995):
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

print("\nScan complete!")
