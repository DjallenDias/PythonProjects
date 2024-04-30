import sys
import socket
import threading
import argparse

def recieve(sock):
    while thread_run:
        data = sock.recv(1024).decode()
        if data == "": break
        print(data)

parser = argparse.ArgumentParser(description="Chat Server side socket")
parser.add_argument("HOST", help="Host or Address to server run on")
parser.add_argument("PORT", help="Port for the server to check for connections", type=int)
parser.add_argument("--username")

args = parser.parse_args()

if (args.username):
    username = args.username
else:
    username = "guest"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((args.HOST, args.PORT))

thread_run = True

recieve_thread = threading.Thread(target=recieve, args=[sock])
recieve_thread.start()

while True:
    msg = input()
    if not msg:
        thread_run = False
        sock.shutdown(socket.SHUT_RDWR)
        break

    sock.send(msg.encode())

sock.close()