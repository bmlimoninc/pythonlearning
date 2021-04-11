print("Output : ")
# Numeric Type:	Integer

myInt = 10
print("Integer: ", type(myInt), " value:", myInt)

# Float to Integer conversion
myFloat = 12.0
myInt = int(myFloat)
print("Float 2 Integer: ", type(myInt), " value:", myInt)

# Remark: Don't forget that anything other then decimal point will be lost
myFloat = 12.2
myInt = int(myFloat)
print("Float 2 Integer: ", type(myInt), " value:", myInt)

# how to swap variables
num1 = 5
num2 = 6
print("Num1: " + str(num1) + " - Num2:" + str(num2))

# Method 1
num1, num2 = num2, num1
print("Num1: " + str(num1) + " - Num2:" + str(num2))

# Method 2
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Num1: " + str(num1) + " - Num2:" + str(num2))

# Method 3
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2
print("Num1: " + str(num1) + " - Num2:" + str(num2))  # num1 and Num2 is now float because of division

# Method 4
num1 = 5
num2 = 6

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print("Num1: " + str(num1) + " - Num2:" + str(num2))
