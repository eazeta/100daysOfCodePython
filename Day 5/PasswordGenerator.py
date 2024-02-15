import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
length = int(input('Length: '))
len_symbols = int(input('No of Symbols: '))
len_numbers = int(input('No of Numbers: '))

length = length - len_symbols - len_numbers

password = []

for i in range(length):
  password += r.choice(letters)
for i in range(len_numbers):
  password += r.choice(numbers)
for i in range(len_symbols):
  password += r.choice(symbols)

password = ''.join(password)

print(password)