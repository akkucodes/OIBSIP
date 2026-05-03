import random
import string
print("Password Generator")
# take password length from user
length = int(input("Enter password length: "))
# check if length is valid
if length <= 0:
    print("Length must be greater than 0")
else:
    print("\nChoose what to include:")
    # user choices for character types
    letters = input("Include letters? (y/n): ")
    numbers = input("Include numbers? (y/n): ")
    symbols = input("Include symbols? (y/n): ")
    chars = ""
    # adding selected character sets
    if letters == 'y':
        chars += string.ascii_letters
    if numbers == 'y':
        chars += string.digits
    if symbols == 'y':
        chars += string.punctuation
    # check if at least one option is selected
    if chars == "":
        print("You must choose at least one option")
    else:
        password = ""
        # generate password character by character
        for i in range(length):
            password += random.choice(chars)
        print("\nGenerated Password:", password)
