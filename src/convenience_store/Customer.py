class Customer:

    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.cart = []

    def __str__(self):
        return f"{self.name} has ${self.funds}."
    
    def checkCart(self):
        print(self.cart)