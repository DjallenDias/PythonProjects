import os
import socket
import threading
import argparse

MAX_MSG_HIST = 20

msg_hist = []

def clear():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def show_mesages():
    clear()
    for msg in msg_hist[::-1]:
        print(msg)
    print(".\n.\n")

def update_msg_hist(msg):
    if len(msg_hist) > MAX_MSG_HIST:
        del msg_hist[-1]
    
    msg_hist.insert(0, msg)
    show_mesages()

def recieve(sock):
    while thread_run:
        data = sock.recv(1024).decode()
        if data == "":
            clear()
            break
        update_msg_hist(data)

parser = argparse.ArgumentParser(description="Chat Server side socket")
parser.add_argument("HOST", help="Host or Address to server run on")
parser.add_argument("PORT", help="Port for the server to check for connections", type=int)
parser.add_argument("--username")

args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((args.HOST, args.PORT))

thread_run = True
recieve_thread = threading.Thread(target=recieve, args=[sock])
recieve_thread.start()

if (args.username):
    username = args.username
else:
    username = "guest"

while True:
    msg = input()
    if not msg:
        thread_run = False
        sock.shutdown(socket.SHUT_RDWR)
        clear()
        break
    sock.send(msg.encode())
sock.close()