import sys


# MASTER_PASSWORD = 'Password12345'
MASTER_PASSWORD = input("Please reset your password: ")
password = input("Please enter your password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome")