
from replit import clear
from art import logo
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculate():
    """Calculator""" #docstring
    clear()
    print(logo)
    operations = {"+": add, "-": sub, "*": multiply, "/": divide}
    first_digit = float(input("Type the first number: "))
    symbol = input("Type an operaor (+ - * /): ")
    second_digit = float(input("Type the second number: "))
    answer = operations[symbol](first_digit,second_digit)
    print(answer)
    while input("Cotinue? ")=='yes':
        new_digit = float(input("New number: "))
        new_symbol = input("Type an operaor (+ - * /): ")
        new_answer = operations[new_symbol](answer,new_digit)
        answer=new_answer
        print(new_answer)
    if input("Reset? ")== 'yes':
        calculate()
calculate()


    


