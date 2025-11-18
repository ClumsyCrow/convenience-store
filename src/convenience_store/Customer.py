class Customer:

    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.cart = []

    def __str__(self):
        return f"{self.name} has ${self.funds}."
    
    def checkCart(self):
        print("Items in " + self.name + "'s cart:")
        for Item in self.cart:
            print(Item.name)
    
    def buy(self, Item):
        if Item.cost <= self.funds:
            self.funds -= Item.cost
            self.cart.append(Item)
        else:
            print("Sorry, you cannot afford this.")