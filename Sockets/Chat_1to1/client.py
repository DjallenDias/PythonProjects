import socket
import threading

from chat import Chat
from cli import Cli

def recieve(sock):
    while thread_run:
        data = sock.recv(1024).decode()
        if data == "": break
        chat.update_chat(data)
        chat.show_chat()
        print()


chat = Chat()
cli = Cli("Client")

args = cli.parse_args()

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
    chat.update_chat(f">> {msg!r}")
    chat.show_chat()
    print()

sock.close()