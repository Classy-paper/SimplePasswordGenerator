import random
import string

alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)

def generate_password(length):
    password_str = ""
    for i in range(1, length):
        if len(password_str) < length:
            password_str = password_str + random.choice(alphabet) + str(random.choice(numbers)) + random.choice(uppercase_alphabet) + random.choice(special_characters)

    return password_str

while True:
    length = int(input("Enter a length for your password: "))

    result = generate_password(length)

    print("Your Password is: {}".format(result))
