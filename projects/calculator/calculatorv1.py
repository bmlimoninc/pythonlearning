import math

def addition():
    number1 = int(input("Enter Your number:  "))
    number2 = int(input("Enter Your number:  "))
    return number1 + number2


def subtraction():
    number1 = int(input("Enter Your number:  "))
    number2 = int(input("Enter Your number:  "))
    return number1 - number2


def multiplication():
    number1 = int(input("Enter Your number:  "))
    number2 = int(input("Enter Your number:  "))
    return number1 * number2


def division():
    number1 = int(input("Enter Your number:  "))
    number2 = int(input("Enter Your number:  "))
    return number1 / number2


def squareRoot():
    number1 = input("Enter Your number:  ")

    return math.sqrt(float(number1))


def powerofNumber():
    number1 = int(input("Enter Your number:  "))
    power = int(input("Enter power:  "))

    return number1 ** power


def menu():
    choice = int(menuDisplay())
    result = 0
    if choice == 1:
        result = addition()
    elif choice == 2:
        result = subtraction()
    elif choice == 3:
        result = multiplication()
    elif choice == 4:
        result = division()
    elif choice == 5:
        result = squareRoot()
    elif choice == 6:
        result = powerofNumber()
    else:
        return False

    print("Result is: ", result)
    return True


def menuDisplay():
    print("################################")
    print("This is Basic Console Calculator")
    print("Please enter your choice.       ")
    print("1. Addition                     ")
    print("2. Subtraction                  ")
    print("3. Multiplication               ")
    print("4. Division                     ")
    print("5. Square Root                  ")
    print("6. Power of                     ")
    print("0. Exit                         ")
    choice = input("Enter Your choice:  ")

    return choice

def calculator():
    while menu():
        pass

    print("\nCalculator Terminated by User")

calculator()