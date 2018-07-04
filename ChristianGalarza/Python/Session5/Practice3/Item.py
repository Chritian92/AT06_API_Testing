class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price

