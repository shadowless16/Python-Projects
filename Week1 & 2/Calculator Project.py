username = input("Enter Username : ")

print(f"Hello {username}")
print("Welcome to the calculator app")

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter operator: ")

        if operator == "+":
            sum = num1 + num2
            print(f"The sum of {num1} and {num2} is {sum}")
        elif operator == "-":
            sub = num1 - num2
            print(f"The subtraction of {num1} and {num2} is {sub}")
        elif operator == "*":
            multiplication = num1 * num2
            print(f"The product of {num1} and {num2} is {multiplication}")
        elif operator == "/":
            division = num1 / num2
            print(f"The dvision of {num1} and {num2} is {division}")
        else:
            print(f"This is an invalid operator {username} try again")

        choice = input("Would you like to preform an operation : \nY or N: ").upper()

        if choice == "Y":
            pass
        else:
            print("Exting the app.......")
            break
    except ValueError:
        print("Pls enter a valid number")
        continue
