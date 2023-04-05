# make socket server, bind port 12345
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen()

while True:
    conn, addr = s.accept()
    print("Connected by", addr)

    conn.send(input().encode("utf-8"))
    data = conn.recv(1024)
    print(data.decode("utf-8"))