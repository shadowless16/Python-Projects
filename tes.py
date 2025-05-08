def multi_number_calculator():
    print("Multi-Number Calculator")
    print("Enter numbers one by one")
    print("After each number, choose an operator (+, -, *, /) or = to get result")
    print("Enter 'q' at any time to quit\n")
    
    numbers = []
    operators = []
    
    # Get first number
    while True:
        num = input("Enter first number: ").strip().lower()
        if num == 'q':
            print("Bye!")
            return
        try:
            numbers.append(float(num))
            break
        except ValueError:
            print("Please enter a valid number or 'q' to quit")
    
    while True:
        # Get operator
        while True:
            op = input(f"Current total: {numbers[-1]}\nEnter operation (+, -, *, /) or = to finish: ").strip().lower()
            if op == 'q':
                print("Bye!")
                return
            if op == '=':
                if len(numbers) == 1:
                    print("You only entered one number!")
                    continue
                break
            if op in ('+', '-', '*', '/'):
                operators.append(op)
                break
            print("Please enter +, -, *, /, = or 'q' to quit")
        
        if op == '=':
            break
        
        # Get next number
        while True:
            num = input("Enter next number: ").strip().lower()
            if num == 'q':
                print("Bye!")
                return
            try:
                numbers.append(float(num))
                break
            except ValueError:
                print("Please enter a valid number or 'q' to quit")
    
    # Calculate step by step
    result = numbers[0]
    print("\nCalculation steps:")
    for i in range(len(operators)):
        next_num = numbers[i+1]
        op = operators[i]
        
        print(f"{result} {op} {next_num}", end="")
        
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num
        elif op == '*':
            result *= next_num
        elif op == '/':
            if next_num == 0:
                print("\nError: Can't divide by zero!")
                return
            result /= next_num
        
        print(f" = {result}")
    
    print(f"\nFinal result: {result}")

if __name__ == "__main__":
    multi_number_calculator()