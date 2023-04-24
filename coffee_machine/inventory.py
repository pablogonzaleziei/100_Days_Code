# inventory.py

class Inventory():
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] < quantity:
                print(f"Not enough {item_name} in stock.")
            else:
                self.inventory[item_name] -= quantity
        else:
            print(f"{item_name} not found in inventory.")

    def print_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
