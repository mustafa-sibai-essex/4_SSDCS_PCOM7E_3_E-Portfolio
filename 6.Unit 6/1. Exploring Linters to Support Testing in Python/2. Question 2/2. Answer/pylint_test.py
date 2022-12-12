# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

"""This code takes the user input and encodes it or decodes it"""
import string

SHIFT = 3
choice = input("would you like to encode or decode?")
word = input("Please enter text")
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ""
if choice == "encode":
    for letter in word:
        if letter == " ":
            ENCODED = ENCODED + " "
        else:
            X = LETTERS.index(letter) + SHIFT
            ENCODED = ENCODED + LETTERS[X]
        if choice == "decode":
            for letter in word:
                if letter == " ":
                    ENCODED = ENCODED + " "
                else:
                    X = LETTERS.index(letter) - SHIFT
                    ENCODED = ENCODED + LETTERS[X]

print(ENCODED)
