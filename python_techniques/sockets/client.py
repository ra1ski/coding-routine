# make socket client and connect to localhost:12345

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))

while True:
    data = s.recv(1024)
    print(data.decode("utf-8"))
    s.send(input().encode("utf-8"))