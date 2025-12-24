import random

# Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'


# Function to generate password
def generate_password(num_letters, num_symbols, num_numbers):
    # Generate random characters from each set
    password_chars = ''.join(random.choices(letters, k=num_letters))
    password_chars += ''.join(random.choices(symbols, k=num_symbols))
    password_chars += ''.join(random.choices(numbers, k=num_numbers))

    # Shuffle the characters to make the password more random
    password_list = list(password_chars)
    random.shuffle(password_list)

    return ''.join(password_list)


# Main program
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate and print the password
password = generate_password(nr_letters, nr_symbols, nr_numbers)
print(password)