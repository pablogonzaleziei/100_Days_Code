from tkinter import *

ingredients = {
    "water": 500,
    "coffee_beans": 100,
    "milk": 200,
    "cups": 5
}

coffee_types = {
    "espresso": {"water": 50, "coffee_beans": 20, "milk": 0, "cost": 2.5},
    "latte": {"water": 100, "coffee_beans": 20, "milk": 50, "cost": 3.0},
    "cappuccino": {"water": 100, "coffee_beans": 20, "milk": 100, "cost": 3.5}
}

def make_coffee(coffee_type):
    """
    Function to make a cup of coffee.
    """
    global ingredients
    water_needed = coffee_type["water"]
    coffee_beans_needed = coffee_type["coffee_beans"]
    milk_needed = coffee_type["milk"]
    cost = coffee_type["cost"]

    enough_ingredients = all(ingredients.get(ingredient, 0) >= quantity for ingredient, quantity in coffee_type.items() if ingredient != "cost")

    if enough_ingredients:
        for ingredient, quantity in coffee_type.items():
            if ingredient != "cost":
                ingredients[ingredient] -= quantity
        message.set(f"Making {coffee_type_name}...\nEnjoy your coffee!")
        cost_label.config(text=f"Cost: ${cost:.2f}")
    else:
        message.set("Sorry, not enough ingredients.")
        cost_label.config(text="Cost:")

def refill_ingredients():
    global ingredients
    ingredients = {
        "water": 500,
        "coffee_beans": 100,
        "milk": 200,
        "cups": 5
    }
    message.set("Ingredients refilled.")
    cost_label.config(text="Cost:")

def buy_coffee():
    global coffee_type_name
    coffee_type_name = var.get()
    coffee_type = coffee_types[coffee_type_name]
    cost = make_coffee(coffee_type)
    if cost:
        message.set(f"You bought {coffee_type_name} for ${cost:.2f}")

root = Tk()
root.title("Coffee Machine")

var = StringVar()
var.set("espresso")

# create labels and buttons
Label(root, text="Select coffee type:").pack(pady=5)
Radiobutton(root, text="Espresso", variable=var, value="espresso").pack()
Radiobutton(root, text="Latte", variable=var, value="latte").pack()
Radiobutton(root, text="Cappuccino", variable=var, value="cappuccino").pack()

Button(root, text="Buy", command=buy_coffee).pack(pady=10)
Button(root, text="Refill ingredients", command=refill_ingredients).pack(pady=10)

message = StringVar()
message.set("Welcome!")
message_label = Label(root, textvariable=message, font=("Arial", 14), fg="green")
message_label.pack(pady=20)

cost_label = Label(root, text="Cost:", font=("Arial", 14))
cost_label.pack(pady=5)

root.mainloop()
