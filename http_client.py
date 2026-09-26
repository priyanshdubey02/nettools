import socket

while True:
    website = input("Enter a website (or 'quit' to stop): ")
    if website == "quit":
        break
    try:
        ip = socket.gethostbyname(website)
        s = socket.socket()
        s.connect((ip, 80))
        request = f"GET / HTTP/1.0\r\nHost: {website}\r\n\r\n"
        s.send(request.encode())
        response = s.recv(4096)
        print(response.decode(errors="ignore"))
        s.close()
    except Exception as e:
        print("Something went wrong:", e)

print("Done!")