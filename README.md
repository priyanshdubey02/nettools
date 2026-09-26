# Network Toolkit

Small Python tools built while learning networking fundamentals. Each tool demonstrates one piece of how the internet works — DNS resolution, HTTP conversations, TCP handshakes, and DHCP leases.

## Tools

### dns_lookup.py — DNS Resolver
Enter a domain name, get its IP address. Includes query timing — run the same lookup twice and watch DNS caching make the second one faster.

Run: `python dns_lookup.py`

### http_client.py — Raw HTTP Client
Sends a hand-built HTTP GET request over a TCP socket and prints the server's raw response: status line, headers, and body. Try `example.com` for a clean 200 OK, or `google.com` to watch a real 301 redirect.

Run: `python http_client.py`

### web_server.py — Mini Web Server
Listens on localhost:8000, prints every incoming request's headers, and serves a small HTML page. Open it in a browser to see the other side of the HTTP conversation.

Run: `python web_server.py`, then visit `http://localhost:8000`

### port_scanner.py — TCP Port Scanner
Performs a TCP connect scan over a port range and reports which ports are open. Built on the 3-way handshake — an accepted connection means an open port.

Run: `python port_scanner.py`

### dhcp_watch.py — DHCP Lease Viewer
Reads your machine's network configuration and displays its DHCP lease: IP address, subnet mask, gateway, DNS servers, DHCP server, and lease times.

Run: `python dhcp_watch.py`


## What I learned
- **DNS** — how names become IPs, and why caching makes repeat lookups faster
- **HTTP** — requests, responses, status codes, headers, redirects
- **TCP** — the 3-way handshake, ports, and how connections get established
- **DHCP** — the DORA handshake, leases, and how devices get their network identity

## Requirements
Python 3.x — standard library only, no external packages needed.
