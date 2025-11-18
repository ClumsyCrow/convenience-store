from customer import Customer
from item import Item

def main():
    print("Welcome")

if __name__ == "__main__":
    main()
    margret = Customer("Margret", 3)
    soda = Item("Soda", 3)
    lettuce = Item("Lettuce", 5)

    print(margret)
    margret.checkCart()
    print(soda)

    margret.buy(soda)
    margret.checkCart()
    margret.buy(lettuce)
    margret.checkCart()