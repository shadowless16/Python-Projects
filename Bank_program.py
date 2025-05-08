import time
import random
import json

with open('user_info.json', 'r') as file:
    user_data = json.load(file)
    acct_password = user_data['Account_Number']

print(user_data)
acct_details = {}
acct_balance = 0
def show_balnace():
    global acct_balance 
    print(f"💰 Current Balance: ₦{acct_balance}")

def deposit(deposit_amount):
    global acct_balance 
    acct_balance += deposit_amount
    print(f"✅ You have succcefully deposited ₦{deposit_amount}")
    print(f"💰 Your current acct balance is ₦{acct_balance}")


def withdraw(withdrawl_amount):
    global acct_balance 
    if withdrawl_amount  > acct_balance:
        print("❌ U are broke")
    elif acct_balance <= 0:
        print("⚠️ Enter a valid amount.")
    else:
        acct_balance -= withdrawl_amount
        print(f"✅ You have succcefully withdrawn ₦{withdrawl_amount}")
        print(f"💰 Your current acct balance is ₦{acct_balance}")


while True:
    print("***********************************")
    print("    Welcome To The Banking App")
    print("***********************************")

    print("1. Exsting Acct")
    print("2. New Acct")

    try:
        acct_choice = int(input("Enter an option"))
    except ValueError:
        print("Invalid Input... \nEnter a number")

    if acct_choice == 1:
        print("***********************************")
        print("    Welcome To The Banking App")
        print("***********************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("***********************************")

        password = int(input("Enter ur acct number: "))

        if password == acct_password:
            print("Sign in successfull")

            try:
                choice = int(input("Enter ur choice from (1 - 4):"))
                if choice == 1:
                    show_balnace()
                    time.sleep(2.5)
                elif choice == 2:
                    try:
                        deposit_amount = int(input("Enter amount to deposit: "))
                        deposit(deposit_amount)
                        time.sleep(2.5)
                    except ValueError:
                        print("Enter Digit Digits")
                        time.sleep(2.5)
                elif choice == 3:
                    try:
                        withdrawl_amount = int(input("Enter amount to depojuisit: "))
                        withdraw(withdrawl_amount)
                        time.sleep(2.5)
                    except ValueError:
                        print("Enter Digit Digits")
                        time.sleep(2.5)
                elif choice == 4:
                    print("Exiting the app....")
                    break
            except ValueError:
                print("Enter Digit from 1 - 4")
            else:
                print("Incorrect or does not exsit")
        
    elif acct_choice == 2:
        
        while True:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")

            if first_name.isnumeric() and last_name.isnumeric():
                print("Invalid input")
            elif first_name == "" or last_name == "":
                print("Field cant be empty")
            else:
                print("Next step!")
                break

        while True:
            phone_number = int(input("Enter your phone number: "))
            Processed_number = str(phone_number)

            if phone_number == "" or len(Processed_number) != 11:
                print("Please fill in all fields correctly.")
                print("The number must be 11 digits")
            else:
                print("Next Step!")
                break

        while True:
            gender = input("Enter your gender (M/F): ").strip().lower()

            if gender == "m" or gender == "f" or gender == "male" or gender == "female":
                print("Next Step!")
                break
            else:
                print("Next Step!")
                break

        while True:
            try:
                age = int(input("Enter your age: "))

                if age < 18:
                    print("You can create an acct yet")
                    break
                else:
                    print("Next step")
                    break
            except ValueError:
                print("U must enter a number")

        acct_number = random.randint(10000000000, 90000000000)

        if acct_number in user_info.json:
            print("Already exsit")
        else:
            print("u are cool to go")

        user_info = {
            "first Name": first_name,
            "Last Name": last_name,
            "Phone Number": phone_number,
            "Gender": gender,
            "Age": age,
            "Account Number": acct_number
        }

        with open('user_info.json', 'w') as info:
            json.dump(user_info, info, indent=4)

        print("***********************************")
        print("\n✅ Registration Complete!")
        print("Account Name:", first_name, last_name)
        print("Phone Number:", phone_number)
        print("Gender:", gender)
        print("Age:", age)
        print("Account Number:", acct_number)
        print("***********************************")

        print(user_info)

