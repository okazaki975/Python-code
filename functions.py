
import random
import string

numbers_selection = int(input("How many numbers should be in your password?: "))
selection_list = []

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random_numbers = str([random.choice(numbers) for _ in range(numbers_selection)])
selection_list += random_numbers

alphabet_selection = int(input("How many alphabets should be in your password?: "))

alphabet = string.ascii_lowercase
random_letters = [random.choice(alphabet) for _ in range(alphabet_selection)]
selection_list += random_letters

symbol_selection = int(input("How many symbols should be in your password?: "))

special_characters = string.punctuation
random_symbols = [random.choice(special_characters) for _ in range(symbol_selection)]
selection_list += random_symbols

# = random_symbols + random_numbers + random_letters
print(selection_list)
password = ''

for char in selection_list:
    password += char
print(password)
