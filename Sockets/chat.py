import os

class Chat(list):
    def __init__(self, max_len=6):
        self.MAX_LENGTH = max_len
    
    def clear_chat(self):
        if (os.name == "nt"):
            os.system("cls")

        else:
            os.system("clear")

    def show_chat(self):
        self.clear_chat()
        for item in self[::-1]:
            print(item)

    def adjust_length(self):
        if len(self) >= self.MAX_LENGTH:
            del self[-1]

    def update_chat(self, object):
        self.insert(0, object)
        self.adjust_length()
