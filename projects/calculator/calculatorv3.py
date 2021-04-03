import math


def calculation(ex):
    total = str(eval(ex))
    return total


text1 = "Enter Your number:  "
text2 = "Enter Your root:  "
text3 = "Enter Your power:  "
text4 = "Enter Your modulo:  "

switch = {
    1: [" + ", 2, text1, text1],
    2: [" - ", 2, text1, text1],
    3: [" * ", 2, text1, text1],
    4: [" / ", 2, text1, text1],
    5: ["math.sqrt", 1, text1],
    6: [" ** ", 2, text2, text3],
    7: [" % ", 2, text1, text4],
}

expression = lambda parmList, operand: str(parmList[1]) + operand + "(" + str(parmList[0]) + ")"


def menu():
    choice = int(menuDisplay())
    result = 0
    exp = ""

    if choice == 0:
        return False

    operation = switch.get(choice)
    inputVal = []
    print(operation)
    for i in range(operation[1]):
        inputVal.append(input(operation[2 + i]))

    inputVal.append("")

    exp = expression(inputVal, operation[0])

    result = calculation(exp)
    print("Result is: ", result)

    input("Press enter to continue")

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
    print("7. Module of                   ")
    print("0. Exit                         ")
    choice = input("Enter Your choice:  ")

    return choice


def calculator():
    while menu():
        pass

    print("\nCalculator Terminated by User")


calculator()
