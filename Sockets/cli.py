import argparse

class Cli(argparse.ArgumentParser):
    def __init__(self, side: str) -> None:
        super().__init__()
        
        self.description = f"Chat {side} side socket"
        self.add_argument("HOST", help="Host or Address to server run on")
        self.add_argument("PORT", help="Port for the server to check for connections", type=int)
        self.add_argument("--username")