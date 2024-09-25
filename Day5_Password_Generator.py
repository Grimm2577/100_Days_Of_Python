# DAY 5 OFFICIALLY UNDERWRAPS!!,  I wanted to be more consistent with my uploads but i caught a really bad cold.....

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []

# checking that the inserted value is not less than 0 to avoid bugs with the code
# looping from 0 to user input of wanted characters, the using the random.choice function to pick a random character
# from the given arrays and then adding it to the password array
if nr_numbers > 0:
    for letter in range(0, nr_letters):
        password += random.choice(letters)
else:
    print("A negative number may not be inserted!, Numbers Not Added")
if nr_symbols > 0:
    for symbol in range(0, nr_symbols):
        password += random.choice(symbols)
else:
    print("A negative number may not be inserted!, Symbols Not Added")
if nr_numbers > 0:
    for num in range(0, nr_numbers):
        password += random.choice(numbers)
else:
    print("A negative number may not be inserted!, Numbers Not Added")

# randomizing all the array indices with the shuffle() function from the random library
random.shuffle(password)

# storing and converting the shuffled array into a string
scrambled_password = "".join(password)

# printing the scrambled password
print(scrambled_password)