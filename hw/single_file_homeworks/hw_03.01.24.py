# 1

import math


def D(a, b, c):
    d = pow(b, 2) - 4 * a * c
    if d > 0:
        d2 = math.sqrt(d)
        x1 = (-b + d2) / (2 * a)
        x2 = (-b - d2) / (2 * a)
        print(f"X1 = {x1} \nX2 = {x2}")
    elif d == 0:
        x = (-b) / 2 * a
        print(f"X = {x}")
    else:
        print("None")


D(2, 4, 1)

# 2

import random
import string


def generate_password():
    password_list = []
    for _ in range(random.randint(1, 10)):
        password_list.append(random.choice(string.ascii_uppercase))
    for _ in range(random.randint(1, 10)):
        password_list.append(random.choice(string.ascii_lowercase))
    for _ in range(random.randint(2, 10)):
        password_list.append(random.choice(string.digits))
    for _ in range(random.randint(1, 10)):
        password_list.append(random.choice(string.punctuation))

    random.shuffle(password_list)

    password = ''.join(password_list)

    while len(password) < 8:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    return password


print(f"Generated password: {generate_password()}")








