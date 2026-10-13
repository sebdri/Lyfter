class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_product(self):
        if len(self.products) == 0:
            print("There are no products in the inventory.")
            return

        print("\n===== PRODUCTS IN THE INVENTORY =====")

        for product in self.products:
            print(f"Name: {product.name}")
            print(f"Price: ${product.price:.2f}")
            print(f"Quantity: {product.quantity}")
            print("--------------------------")

    def total_inventory(self):
        total = 0

        for product in self.products:
            total += product.price * product.quantity

        return total


invent = Inventory()

while True:

    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the quantity: "))

    product = Product(name, price, quantity)

    invent.add_product(product)

    continu = input("Do you want to add another product? (y/n): ")

    if continu.lower() == "n":
        break

print("\n===== INVENTORY =====")
invent.show_product()

print(f"\nTotal inventory value: ${invent.total_inventory():.2f}")