import socket
import threading

from chat import Chat
from cli import Cli

def recieve(conn):
    while thread_run:
        data = conn.recv(1024).decode()
        if data == "": break
        chat.update_chat(data)
        chat.show_chat()
        print()

chat = Chat()
cli = Cli("Server")

args = cli.parse_args()


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