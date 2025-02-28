
import random
import string

letters = string.ascii_letters

numbers = string.digits

symbols = "#a$56!"


password_length = int(input("How long should the password be: (minimum 6):"))

if password_length < 6:
    print("Password length must be at a least 6. Try again!")

else:
    password = []
    password.append(random.choice(letters))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    all_characters = letters + numbers + symbols

while len(password) < password_length:
 password.append(random.choice(all_characters))
 random.shuffle(password)
 final_password = "" .join(password)
 print("Your passwoed is:", final_password)