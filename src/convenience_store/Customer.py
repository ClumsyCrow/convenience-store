class Customer:

    def __init__(self, name, funds):
        self.name = name
        self.funds = funds

    def __str__(self):
        return f"{self.name} has ${self.funds}."