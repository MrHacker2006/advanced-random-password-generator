# Phase-1 --> importing all the required libraries
import random
import string
import sys
import pyperclip

# Phase-2 --> Taking Input from the user
while True:
    try:
        print("\nWelcome to the Random Password Generator!\n")

        length = int(input("Enter the length of the password(in integers) which you want to generate : "))
        print("\nWhat things you want to include in your password❓\n")
        include_numbers = str(input("Do you want to include Numbers ?(Y/N): ")).lower().strip() in ['y', 'yes']
        include_lowercase = str(input("Do you want to include Lowercase characters ?(Y/N): ")).lower().strip() in ['y', 'yes']
        include_uppercase = str(input("Do you want to include Uppercase characters ?(Y/N): ")).lower().strip() in ['y', 'yes']
        include_punctuations = str(input("Do you want to include Punctuations ?(Y/N): ")).lower().strip() in ['y', 'yes']
        break
    except ValueError:
        print("\nPlease Enter a valid integer!")

# Phase-3 --> Construction of Character Pool
char_pool = ""
if(include_numbers):
    char_pool += string.digits
if(include_lowercase):
    char_pool += string.ascii_lowercase
if(include_uppercase):
    char_pool += string.ascii_uppercase
if(include_punctuations):
    char_pool += string.punctuation
print(char_pool)

