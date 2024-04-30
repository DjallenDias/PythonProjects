import sys
import socket
import threading

HOST = "localhost"
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

conn, addr = sock.accept()

print(f"{addr} connected")

conn.send("hey".encode())
