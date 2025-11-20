from customer import Customer

class Clerk:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Clerk's name is {self.name}."

    def talk(self):
        print("Welcome in! How may I help you?")