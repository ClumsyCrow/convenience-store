class Customer:

    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.cart = []

    def __str__(self):
        return f"Customer {self.name} has ${self.funds}."
    
    # Checks what is in the cart and lists it out
    def checkCart(self):
        print("Items in " + self.name + "'s cart:")
        for Item in self.cart:
            print(Item.name)
    
    # Checks whether you can afford an item,
    # then subtracts from funds and adds to cart if you can
    def buy(self, Item):
        if Item.cost <= self.funds:
            self.funds -= Item.cost
            self.cart.append(Item)
        else:
            print("Sorry, you cannot afford this.")