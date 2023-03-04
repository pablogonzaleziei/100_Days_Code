import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password generator\n")
n_letters = int(input("How many letters\n"))
n_symbols = int(input("How many symbols\n"))
n_numbers = int(input("How many numbers\n"))
total_characters = n_letters+n_numbers+n_symbols
password=[]
print(n_numbers)
for a in range(0,n_numbers):
    password.append(numbers[random.randint(0,len(numbers)-1)])
    print(password)
for b in range(0,n_letters):
    password.append(letters[random.randint(0,len(letters)-1)])
for c in range(0,n_symbols):
    password.append(symbols[random.randint(0,len(symbols)-1)])
random.shuffle(password)
print(password)

    