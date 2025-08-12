# Phase-1 --> importing all the required libraries
import random
import string
import sys
import csv
import os
import pyperclip

# Phase-2 --> Taking Input from the user
def generate_and_save_password():
    while True:
        try:
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


        # finding length of the remaining password
        random_chars = []
        required_length= length-len(guaranteed_char)


        # Selecting remainging password
        for i in range(required_length):
            random_chars.append(random.choice(char_pool))
        
        # Merging the both the lists
        password_char = guaranteed_char + random_chars
        # print(password_char)


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
        random.shuffle(random_chars)
        # print(random_chars)
        
        # Converting List into string
        final_password = "".join(random_chars)
        # print(final_password)

        # copying the password into your clipboard
        pyperclip.copy(final_password)
        print(f"Your Password is : {final_password}")
        print("The password is copied in your clipboard automatically ")


    # Phase-5 --> Storing User Input for Future-Use

    opinion = str(input("\nDo you want to store the output for the Future Use? (Y/N): ")).strip().lower() in ['y', 'yes']

    if(opinion):
        login_name = str(input("Enter Your name: ")).strip().lower()
        service_name = str(input("Enter the Name of the Website Or App, for which you are creating password: ")).strip().lower()
        
        file_path = 'password.csv'

        # Checking file already exists or not
        file_exists = os.path.exists(file_path)

        with open(file_path , 'a', newline='') as csvfile:
            column_names = ['user_name', 'web_name', 'password']
    
            writer = csv.DictWriter(csvfile, fieldnames=column_names)

            # If the file is new(doesn't exist)
            if not file_exists:
                writer.writeheader() # This will write column names (only once), if the file is new, if the file is old it get skipped automatically.

            # We are writing the actual data row
            writer.writerow({'user_name': login_name, 'web_name':service_name, 'password':final_password})
        print(f"Password for {service_name} is sucessfully stored at {file_path}")
    else:
        print("Ok, your password was not saved.")
        print("\nThank you for using our password generator!")


# Phase-6--> Reading the Password of the user(already stored)
def retrieval():
    print("Reading Part started:\n ")
    login_name = str(input("Enter the name of the user, which you have entered earlier: ")).strip().lower()
    service_name = str(input("Enter the name of website or app name , for which you have generated password earlier: ")).strip().lower()
   
    file_path = 'password.csv'
    file_exists = os.path.exists(file_path)
    column_names = ['user_name', 'web_name', 'password']

    if not file_exists:
        print("OOPs your data file does not exists, maybe it get deleted!")
    else:
        with open(file_path, 'r', newline='') as csvfile:

            reader = csv.DictReader(csvfile, fieldnames=column_names)
            
            password_found = False
            
            for row in reader:
                if row['user_name']==login_name and row['web_name']==service_name:
                    print(f"Your Password is Founded sucessfully : \n{row['password']}")
                    password_found = True
                    break
            if not password_found:
                print("We have tried our best to find your password, but we are not able to find that!")


if __name__ == "__main__":
    print("\nWelcome to the Random Password Generator!\n")
    choice = int(input("Enter 1 for generating password\nEnter 2 for retrieving old passowrd\nEnter your choice: "))
    if(choice == 1):
        generate_and_save_password()
    elif(choice == 2):
        retrieval()
    else:
        print("Please Enter a valid choice!")