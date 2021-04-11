



variable = 10

def func():
    variable = 22

    print("variable in func "+str(variable))

def func2():
    global variable
    variable = 33

    print("variable in func2 "+str(variable))

######

func()
print("variable in glabal scope " + str(variable))

func2()
print("variable in glabal scope " + str(variable))
