on = True

def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add():
    a, b = get_numbers()
    print("Result:", a + b)

def subtraction():
    a, b = get_numbers()
    print("Result:", a - b)

def multiply():
    a, b = get_numbers()
    print("Result:", a * b)

def divide():
    a, b = get_numbers()
    if b == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print("Result:", a / b)

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
