# Flag to control the main calculator loop
on = True

# Function to get two numbers from the user
def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

# Addition operation
def add():
    a, b = get_numbers()
    print("Result:", a + b)

# Subtraction operation
def subtraction():
    a, b = get_numbers()
    print("Result:", a - b)

# Multiplication operation
def multiply():
    a, b = get_numbers()
    print("Result:", a * b)

# Division operation with zero-check validation
def divide():
    a, b = get_numbers()
    if b == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print("Result:", a / b)

# Main program loop
while on:
    operation = input("Please press: +, -, *, / or Q: ")

    if operation == "+":
        add()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation.lower() == "q":
        on = False
        print("Thanks for today, bye-bye!")
    else:
        print("It's not a correct operation")
