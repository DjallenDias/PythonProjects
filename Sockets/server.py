import sys
import socket
import threading
import argparse

parser = argparse.ArgumentParser(description="Chat Server side socket")
parser.add_argument("HOST", help="Host or Address to server run on")
parser.add_argument("PORT", help="Port for the server to check for connections", type=int)
parser.add_argument("--username")

args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((args.HOST, args.PORT))
sock.listen()

conn, addr = sock.accept()

if (args.username):
    username = args.username
else:
    username = "guest"