from ChristianGalarza.Python.Session5.Practice3.Item import *


class Shopping:

    def __init__(self):
        self.list_items = []

    def add_item(self, name_item, price, quantity):
        self.list_items.append(Item(name_item, price, quantity))

    def verify_availability(self, name_item, quantity):
        for item in self.list_items:
            return name_item == item.name and 0 < quantity <= item.quantity

    def update_quantity_item(self, name_item, quantity):
        for item in self.list_items:
            if name_item == item.name:
                item.quantity -= quantity

    def get_price_item(self, name_item):
        for item in self.list_items:
            if name_item == item.name:
                return item.price
