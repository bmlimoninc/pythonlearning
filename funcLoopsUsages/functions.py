# Scope defined via Indentation


def myfunc(parm1, parm2):
    print("parm1:", parm1, "- parm2: ", parm2)


myfunc("parm1 is ", 10)

# you can pass arguments similar to key = value syntax
myfunc(parm2=10, parm1="parm1 is ")


def myfunc2(parm1, parm2="defaultValue"):
    print("parm1:", parm1, "- parm2: ", parm2)


myfunc2("parm1 is ")


def myfunc3(**args):
    print("parm1:", args["parm1"], "- parm2: ", args["parm2"])


myfunc3(parm2=10, parm1="parm1 is ")


# Remark Can not add an argument without default value after an argument with default value
# def myfunc2(parm1="defaultValue",parm2):


# pass function as argument
def myArgFunc():
    print("this function passed as argument")


def myFunc4(func, parm1):
    print(" This is parm1 ", parm1)
    func()


myFunc4(myArgFunc, 123)


# since function definition can not be empty like all other statements
# we fool interpreter by using pass statement
def myFunc5():
    pass


# Recursion functions can me implemented.
def isPalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[len(string) - 1]:
        return isPalindrome(string[1:len(string) - 1])
    else:
        return False

def main():
    if isPalindrome("AbCdef FEDcBa ".lower().replace(" ","")):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

main()

