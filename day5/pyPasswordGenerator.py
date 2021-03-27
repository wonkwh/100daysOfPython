# Password Generator Project
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

# password = ""
# for char in password_list:
#     password += char
password = ''.join(password_list)
print(f"Your password is: {password}")

# https://replit.com/@appbrewery/password-generator-end comment solution test


def pass_gen():
    alphas = list(string.ascii_letters)
    puncs = list(string.punctuation)
    nums = list(range(0, 9))
    random.shuffle(list(zip(alphas, puncs, nums)))

    print("Welcome to PyPassword Generator!")
    letter = int(input("How many letters would you like in your password: "))
    symbols = int(input("How many symbols would you like in your password: "))
    num = int(input("How many number would you like in your password: "))
    pass_gen = alphas[0:letter] + puncs[0:symbols] + nums[0:num]
    random.shuffle(pass_gen)
    print(f"Your password is: {''.join([str(x) for x in pass_gen])}")


pass_gen()
