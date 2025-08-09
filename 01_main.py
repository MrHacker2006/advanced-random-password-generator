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
        print("What things you want to include in your password❓\n")
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
# print(char_pool)
if char_pool == "":
    print("Please Select atleast one choice from the provided options")
    sys.exit()


# Phase-4 Password Generation + Printing the password
resp = str(input("\nDo you want to include one character from each of your choice? (Y/N): ")).strip().lower()

if resp not in ['y','yes', 'n', 'no']:
    print("Please Enter a Vaild Choice!")
    sys.exit()

enforce = resp in ['y','yes']
if (enforce):
    guaranteed_char = []
    if(include_numbers):
        guaranteed_char.append(random.choice(string.digits))
    if(include_lowercase):
        guaranteed_char.append(random.choice(string.ascii_lowercase))
    if(include_uppercase):
        guaranteed_char.append(random.choice(string.ascii_uppercase))
    if(include_punctuations):
        guaranteed_char.append(random.choice(string.punctuation))
    # print(guaranteed_char)


     # finding lenght of the remaining password
    random_chars = []
    required_length= length-len(guaranteed_char)


     # Selecting remainging password
    for i in range(required_length):
        random_chars.append(random.choice(char_pool))
    
    # Merging the both the lists
    password_char = guaranteed_char + random_chars
    print(password_char)


    # Shuffling the list
    random.shuffle(password_char)
    
    # Converting List into string
    final_password = "".join(password_char)


    # copying the password into your clipboard
    pyperclip.copy(final_password)
    print(f"Your Password is : {final_password}")
    print("The password is copied in your clipboard automatically ")
else:
    random_chars = []
    for i in range(length):
        random_chars.append(random.choice(char_pool))
    # print(random_chars)

    #shuffling the list
    random.shuffle(random.chars)
    # print(random_chars)
    
    # Converting List into string
    final_password = "".join(random_chars)
    # print(final_password)

    # copying the password into your clipboard
    pyperclip.copy(final_password)
    print(f"Your Password is : {final_password}")
    print("The password is copied in your clipboard automatically ")