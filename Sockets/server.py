import socket
import threading
import argparse

from chat import Chat

chat = Chat()

def recieve(conn):
    while thread_run:
        data = conn.recv(1024).decode()
        if data == "": break
        chat.update_chat(data)
        chat.show_chat()
        print()

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
sock.bind((args.HOST, args.PORT))
sock.listen()

conn, addr = sock.accept()

thread_run = True
recieve_thread = threading.Thread(target=recieve, args=[conn])
recieve_thread.start()

while True:
    msg = input()
    if msg == "":
        thread_run = False
        conn.close()
        break
    conn.send(msg.encode())
    chat.update_chat(f">> {msg!r}")
    chat.show_chat()
    print()

conn.close()
sock.close()