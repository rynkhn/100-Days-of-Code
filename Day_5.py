import random
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for char in range(0,nr_letters):
    password.append(random.choice(letters))

for char in range(0,nr_symbols):
    password.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

pas = ""

for char in password:
    pas += char

print(f"Your password is: {pas}")