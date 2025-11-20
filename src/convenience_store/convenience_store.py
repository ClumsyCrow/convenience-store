from customer import Customer
from item import Item
from clerk import Clerk

def main():
    print("Welcome")

    # Instantiating object instances
    cashier = Clerk("Anthony")
    margret = Customer("Margret", 3)
    soda = Item("Soda", 3)
    lettuce = Item("Lettuce", 5)
    coffee = Item("Coffee", 5)
    eggs = Item("Eggs", 15)

    # Adding Items to shelves
    '''
    makes a collection of Item instances
    and puts them into a list that the
    Customer can buy from
    '''

    # Defines lines the Clerk can say
    '''
    contains a list of quotes that
    the Clerk can randomly grab from
    when the Customer buys an Item
    (could be dependant on what Items
    are currently in the store)
    '''

if __name__ == "__main__":
    main()
