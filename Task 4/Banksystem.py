import secrets
import string
import os


print("Welcome to our Banking system program")
def start():
    print("Please make your option")
    print("1 : Staff login")
    print("2 : Close App")
    option = input()

    if (option == "2" or option.lower() == "close app"):
        exit()

    while (not(option == "2" or option.lower() == "close app") and not(option == "1" or option.lower() == "staff login")):
        print("Please enter a valid option!")
        option = input()

    if (option == "1") or (option.lower() == "staff login"):
        staff_login()

# function to check if login details is in specified file
def check_string_file(file_name, login_details):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if login_details in line:
                return True
    return False

def staff_login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    if check_string_file('Staff.txt', username) and check_string_file('Staff.txt', password):

        # creates a file and stores the user session
        user_file = f"{username}.txt"
        user_session = open(user_file, 'w').write(f'{username}\n{password}')

        account_actions(username)
    else:
        print("Username or Password Incorrect")
        print("Would you like to try again? Yes or No")
        repeat = input()

        while (repeat.lower() != 'yes' and repeat.lower() != 'no'):
            print("Enter a valid input! Yes or No")
            repeat = input()

        if (repeat.lower() == "yes"):
            staff_login()
        else:
            start()


def account_actions(username):
    print("What would you like to do now ?")
    print("1 : Create New Bank Account")
    print("2 : Check Account Details")
    print("3 : Logout")
    answer = input()
    if (answer == "1") or (answer.lower() == "create new bank account"):
        account_name = input("Enter your account name : ")
        opening_balance = input("Opening balance : ")
        account_type = input("Account type : ")
        account_email = input("Email : ")

        # generates a random set of 10 digits
        account_number = ''.join(secrets.choice(string.digits)for i in range(10))
        customer_file = open("Customer.txt", 'a').write(f'{account_number}\n{account_name}\n{account_type}\n{account_email}\n{opening_balance}\n\n')
        print("Account created successfully")
        print(f"Your account number is {account_number}")
        account_actions()



    if (answer == "2") or (answer.lower() == "check account details"):
        account_detail = input("Enter your account number : ")
        in_customer_file = open("Customer.txt", 'r')
        if check_string_file('Customer.txt', account_detail):
            print(in_customer_file.read())
            in_customer_file.close()
            account_actions()

    if (answer == "3") or (answer.lower() == "logout"):
        user_file = f"{username}.txt"
        os.remove(user_file)
        start()

start()
