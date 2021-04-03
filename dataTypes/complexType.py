print("Output : ")
# Numeric Type:	Complex

myComplex = 1j
myComplex2 = 1 + 1j
print("Complex", type(myComplex), " value:", myComplex)
print("Complex", type(myComplex2), " value:", myComplex2)

# Integer to Complex
myInt = 10
myComplex = complex(myInt)
print("Integer 2 Complex ", type(myComplex), " value:", myComplex)

# Float to Complex
myFloat = 12.0
myComplex = complex(myFloat)
print("Float 2 Complex ", type(myComplex), " value:", myComplex)

print("Output : ")

# String to Complex
myStr = "12"
myComplex = complex(myStr)
print("String 2 Complex ", type(myComplex), " value:", myComplex)

# Remark Invlid Conversions
myComplex = complex("myStr")
