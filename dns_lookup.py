import socket
import time

while True:
    website = input("Enter a website (or 'quit' to stop): ")
    if website == "quit":
        break
    try:
        start = time.time()
        ip_address = socket.gethostbyname(website)
        elapsed = time.time() - start
        print(website, "lives at", ip_address)
        print(f"Lookup took {elapsed:.3f} seconds")
    except socket.gaierror:
        print("Couldn't find that website. Check the spelling and try again.")

print("Done!")
