print("Output : ")
# Numeric Type:	Float

myFloat = 1.1
print("Float", type(myFloat), " value:", myFloat)

# String to Float
myStr = "12"
myFloat = float(myStr)
print("String 2 Float ", type(myFloat), " value:", myFloat)

# Integer to Float
myInt = 10
myFloat = float(myInt)
print("Integer 2 Float ", type(myFloat), " value:", myFloat)


#Remark Invalid Conversion
myFloat = float("myStr")
print("String 2 Float ", type(myFloat), " value:", myFloat)