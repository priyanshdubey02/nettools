import subprocess

result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)
lines = result.stdout.splitlines()

wanted = ["Host Name", "DHCP Enabled", "IPv4 Address", "Subnet Mask",
          "Default Gateway", "DHCP Server", "DNS Servers",
          "Lease Obtained", "Lease Expires"]

print("=== Your machine's DHCP lease ===\n")
for line in lines:
    clean = line.strip()
    for key in wanted:
        if clean.startswith(key):
            print(clean)
