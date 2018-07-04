import logging
from ChristianGalarza.Python.Session5.Practice3.Shopping import Shopping

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Shopping_log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Main:
    def __init__(self, shop):
        self.shop = shop
        self.items_purchase_amount = {}
        self.items_purchase_price = {}

    def add_item_purchase(self):
        item = input("Insert the item: ")
        quantity = int(input("Insert the quantity to purchasing: "))
        while True:
            if self.shop.verify_availability(item, quantity):
                self.items_purchase_amount[item] = quantity
                self.items_purchase_price[item] = quantity * self.shop.get_price_item(item)
                self.shop.update_quantity_item(item, quantity)
                break
            else:
                print("The item is not exist in the shopping")
                break
        logger.info('Adding product to cart Practice3')

    def print_products(self):
        print("********List of item purchased********")
        for item in self.items_purchase_price:
            print("ITEM: ", item)
            print("TOTAL_PRICE: ", self.items_purchase_price[item])
            print("*******************************")
        logger.info('List of products in your cart shopping')

    def perform_purchase(self):
        while True:
            continue_purchase = input("Do you want to make a purchase?(yes/no): ")
            if continue_purchase.lower() == "yes":
                self.add_item_purchase()
            else:
                break
        logger.info('Product purchased')

    def calculate_price(self):
        total_price = 0
        for i in self.items_purchase_price:
            total_price += self.items_purchase_price[i]
        return total_price

    def balance(self, cash_paid):
        total_price = int(self.calculate_price())
        if cash_paid < total_price:
            return "Cash paid not enough"
        return cash_paid - total_price


print("Welcome to shopping")
store = Shopping()
store.add_item("Asus", 1590, 10)
store.add_item("Toshiba", 1480, 9)
store.add_item("Samsung", 950, 15)

shopping_cart = Main(store)

shopping_cart.perform_purchase()
shopping_cart.print_products()
print("The total price is: ", shopping_cart.calculate_price())
print("The balance is: ", shopping_cart.balance(100))
