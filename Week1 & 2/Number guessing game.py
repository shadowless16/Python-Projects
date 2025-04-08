import random

# Define a function that takes user input and compares it with a randomly generated number.
# Use a loop inside the function to keep prompting the user until they guess correctly.
# Handle errors separately by checking if the input is a valid number before performing any comparisons.
# Remove unnecessary conditions (like else: print("Na u havent gotten it")) since the previous checks cover all cases.
# Enhance readability by displaying clear and structured messages to the user.

def random_guess():
    while True:
        try:
            number = int(input("Enter no. : "))
            random_no = random.randint(1, 10)


            if number > random_no:
                print(f"The number {number} Too High")
                print(f"This is ur {number} and this is the {random_no}")
            elif number < random_no:
                print(f"The number {number} is Too low")
                print(f"This is ur {number} and this is the {random_no}")
            elif number == random_no:
                print("U got it right")
                print(f"This is ur {number} and this is the {random_no}")
                break
        except ValueError:
            print("Invalid input")

random_guess()
