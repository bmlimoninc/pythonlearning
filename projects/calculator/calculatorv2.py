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


def myExit():
    return False


switch = {
    0: myExit,
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division,
    5: squareRoot,
    6: powerofNumber
}


def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switch.get(argument, "nothing")
    # Execute the function
    return func()


def menu():
    choice = menuDisplay()
    result = numbers_to_strings(choice)
    if result:
        print("Result is: ", result)
        return True

    return False


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
