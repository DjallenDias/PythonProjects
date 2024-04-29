class Person:
    def __init__(self, name, age, datebirth, sex):
        self.name = name
        self.age = age
        self.datebirth = datebirth
        self.sex = sex

    def talk(self, text=""):
        print(text)