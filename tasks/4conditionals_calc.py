on = True
def add():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    print(a+b)

def subtraction():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    print(a-b)

def multiply():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    print(a*b)

def devide():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    print(a/b)

while on:
    operation = input("Please press: +, -, *, /,  or Q: ")
    if operation == "+":
        add()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiply()
    elif operation == "/":
        devide()
    elif operation == "Q":
        on = False
        print("Thanks for today, bye-bye!")
    else:
        print("it's not correct operation")