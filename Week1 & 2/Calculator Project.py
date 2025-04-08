"""Calculator app"""
print("Welcome To the Calculator appp!!!!!")

while True:
    num1 = float(input("Enter the first number: "))
    choice =  input("What operation would you like to perfomr. \n+, -, /, x: ")
    num2 = float(input("Enter your second number: "))

    if choice == "+":
        result = num1 + num2
        print(f"{num1} + {num2} is = {result}")
    elif choice == "-":
        result = num1 - num2
        print(f"{num1} - {num2} is = {result}")
    elif choice == "/":
        if num2 == 0:
            print("Dvison by zero not posible")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} is = {result}")
    elif choice == "x":
        result = num1 * num2
        print(f"{num1} * {num2} is = {result}")
    else:
        print("Invalid opearator")

    choice2 = input("Would you like to continue: Press (Y). Else Press any other key: ")

    if choice2 == "Y":
        pass
    else:
        print("Invalid option")
