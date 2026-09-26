import socket

server = socket.socket()
server.bind(("localhost", 8000))
server.listen(1)
print("Server running! Open http://localhost:8000 in your browser")

while True:
    client, address = server.accept()
    print("Visitor connected from", address)
    request = client.recv(1024)
    print("They sent:")
    print(request.decode(errors="ignore"))

    body = "<h1>Hello from my own web server!</h1><p>You built this.</p>"
    response = (
        "HTTP/1.0 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
        f"{body}"
    )
    client.send(response.encode())
    client.close()