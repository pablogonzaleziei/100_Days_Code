# main.py
import inventory

# Define the initial inventory
initial_inventory = {"coffee": 100, "water": 1000, "milk": 500, "sugar": 200}

# Create an instance of the Inventory class
inv = inventory.Inventory(initial_inventory)

# Define the recipes for the coffees
recipes = {
    "espresso": {"coffee": 1, "water": 50},
    "latte": {"coffee": 1, "water": 50, "milk": 100},
    "cappuccino": {"coffee": 1, "water": 50, "milk": 50},
    "americano": {"coffee": 1, "water": 100},
    "macchiato": {"coffee": 1, "water": 50, "milk": 50},
}

# Define a function to make a coffee
def make_coffee(recipe):
    if inv.check_inventory(recipe):
        print("Making coffee...")
        inv.update_inventory(recipe)
        print("Coffee is ready!")
    else:
        print("Sorry, there are not enough ingredients to make this coffee.")

# Make some coffees
make_coffee(recipes["espresso"])
make_coffee(recipes["latte"])
make_coffee(recipes["cappuccino"])
make_coffee(recipes["americano"])
make_coffee(recipes["macchiato"])

# Get the current inventory
print(inv.get_inventory())
