# importing random library
import random

print("This program is a random password generator. Please follow the prompt below.")

try:
    # using int ensures that users input is an integer
    password_length = int(input("Please enter how long your password needs to be using a number: "))
except:
    print("Please enter a whole number greater than zero.")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&'
# password will be generated randomly using characters from string library

# loop will run number of times depending on the password_length entered by the user

password = [] # creates an empty list

# loops through characters in range of password_length entered by user
try:
    for c in range(password_length): 
        password.append(random.choice(characters)) # appends characters to password list
    print(''.join(password)) # prints password
except NameError:
    print("You cannot enter a letter, letters, decimals.") 