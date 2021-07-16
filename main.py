import os
import pandas
import array
import random
import time


#  Function to clear CLS after every iteration
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate(n):
    MAX_LEN = n

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    return password


class Password:
    def __init__(self):
        f = open("passwords.csv", 'a')  # Creates a cvv file, if it doesn't exist.
        f.close()  # Closing it because we would be using pandas rather than python's default file manager

        self.col_names = ["Website's name", "Password"]

    def print_file(self):
        passwords_csv_file = pandas.read_csv("passwords.csv", names=self.col_names)
        print(passwords_csv_file)

    def insert(self, website_name, passwd):
        data_to_be_inserted = {"Website's name": [website_name], "Password": [passwd]}

        df = pandas.DataFrame(data_to_be_inserted)
        df.to_csv('passwords.csv', mode='a', header=False, index=False)


data = Password()
while True:
    clear()

    print(" (1): New Password \n (2): Get Old Passwords \n (3): Exit")
    cond = input()

    if cond == '1':
        n = input("Enter the length of the password: ")
        n = int(n)

        passwd = generate(n)
        print(passwd)

        cond = input("Do you want to save this password? (y/n) ")
        if cond == 'y':
            name = input("Enter the website's name / username: ")
            data.insert(name, passwd)
            clear()
            print("Saved")
            time.sleep(1)
        else:
            continue

    elif cond == '2':
        data.print_file()
        input("\n\n Press any key to continue.")
    elif cond == '3':
        exit()
    else:
        print("Invalid")
        time.sleep(1)
        continue
