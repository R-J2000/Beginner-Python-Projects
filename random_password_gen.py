import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    # Shuffle the list of characters which is ordered
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    # One final shuffle for good measure
    random.shuffle(password)

    password = "".join(password)

    print(password)

generate_password()
