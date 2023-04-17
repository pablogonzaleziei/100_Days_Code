import UI

# define the ingredients and their initial quantities
water = 500
coffee_beans = 100
milk = 200
cups = 5

def make_coffee(water_needed, coffee_beans_needed, milk_needed, cost):
    """
    Function to make a cup of coffee.
    """
    global water, coffee_beans, milk, cups
    if water >= water_needed and coffee_beans >= coffee_beans_needed and milk >= milk_needed and cups >= 1:
        print("Making coffee...")
        water -= water_needed
        coffee_beans -= coffee_beans_needed
        milk -= milk_needed
        cups -= 1
        print("Enjoy your coffee!")
        if cost > 0:
            amount_paid = 0
            while True:
                payment = input("Please pay ${:.2f}, or enter 'q' to quit: ".format(cost - amount_paid))
                if payment.lower() == "q":
                    print("Payment canceled.")
                    print("Your money returned is ${:.2f}.".format(amount_paid))
                    break
                try:
                    payment = float(payment)
                    if payment < 0:
                        print("Invalid input. Please enter a positive amount.")
                    else:
                        amount_paid += payment
                        if amount_paid >= cost:
                            change = amount_paid - cost
                            print("Thank you for your purchase! Your change is ${:.2f}.".format(change))
                            break
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
    else:
        print("Sorry, not enough ingredients.")

# display the main menu
while True:
    print("Select an option:")
    print("1. Make espresso ($2.50)")
    print("2. Make latte ($3.00)")
    print("3. Make cappuccino ($3.50)")
    print("4. Refill ingredients")
    print("5. Quit")

    option = input("Enter your choice: ")

    if option == "1":
        make_coffee(50, 20, 0, 2.5) # espresso requires 50ml water and 20g coffee beans, costs $2.50
    elif option == "2":
        make_coffee(100, 20, 50, 3.0) # latte requires 100ml water, 20g coffee beans, and 50ml milk, costs $3.00
    elif option == "3":
        make_coffee(100, 20, 100, 3.5) # cappuccino requires 100ml water, 20g coffee beans, and 100ml milk, costs $3.50
    elif option == "4":
        water = 500
        coffee_beans = 100
        milk = 200
        cups = 5
        print("Ingredients refilled.")
    elif option == "5":
        break
    else:
        print("Invalid option.")

print("Goodbye!")
