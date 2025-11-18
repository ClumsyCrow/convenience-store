from customer import Customer
from item import Item

def main():
    print("Welcome")

if __name__ == "__main__":
    main()
    margret = Customer("Margret", 2.99)
    print(margret)
    margret.checkCart()