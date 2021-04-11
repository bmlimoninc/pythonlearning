lamdaFunc = lambda x: x + 1
print("Result is :", lamdaFunc(10))

lamdaAddition = lambda x, y: x + y
print("Result is :", lamdaAddition(10, 12))


# Use lambda to put an anonymous lambda function in another function.
def myFuncRandomGenerator(input):
    return lambda n: n % input

# we set  modulo of function as 2 here for function myIndexer
myIndexer = myFuncRandomGenerator(2)
myIndexer2 = myFuncRandomGenerator(3)

# user only know function myIndexer and myIndexer2 but technically does not know details.
print("myModuler: " + str(myIndexer(3)))
print("myModuler2: " + str(myIndexer2(3)))
