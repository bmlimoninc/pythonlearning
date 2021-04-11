print("Output : ")
# Numeric Type:	String

myStr = "myStr"
print("String", type(myStr), " value:", myStr)

# Integer to String
myInt = 10
myStr = str(myInt)
print("Integer 2 String ", type(myStr), " value:", myStr)

# Float to String
myFloat = 12.0
myStr = str(myFloat)
print("Float 2 String ", type(myStr), " value:", myStr)

#########################################################3
# String Tips

# String Formatting
txt = "Bitcoin current price is {:.2f} dollars"
price = 57815.31
print(txt.format(price))

# String Formatting with multiple value
txt = "Bitcoin gain %{} in a year. Within {} years, we may see value of {:.2f} dollars"

percent = 40
duration = 10
price = 879655
print(txt.format(percent, duration, price))

# giving index number to placeholder.
txt = "Bitcoin gain %{0} in a year. Within {1} years, we may see value of {2:.2f} dollars"
print(txt.format(percent, duration, price))
# REMARK!! index given in Curly bracket are index of values in format() function.
# percent has index 0 and price has index 2

# named indexes
txt = f"Bitcoin gain %{percent} in a year. Within {duration} years, we may see value of {price:.2f} dollars"
print(txt.format(percent=40, duration=10, price=879655))

# how to split string into parts
txt = "How to split string into parts"
splitted = txt.split(" ")
print("Splitted List:" + str(splitted))
print("Splitted List type:" + str(type(splitted)))
print("Splitted item type:" + str(type(splitted[0])))

# how to replce substrings
txt = "How to replce sub string in a string. " \
      "However all hows(except this) will be rellaced"
replacedText = txt.replace("How", "HOW")

print(replacedText)


# lover/Upper Case strings
txt = " ThisisASTRinG "

print("Upper String:", txt.upper())
print("Lower String:", txt.lower())

# how to find if characters in string is a digit

txt = "10"
print("Is txt is digit ?:", str(txt.isdigit()))

txt = "RFC-4141"
print("Is txt is digit ?:", str(txt.isdigit()))

# join Iterable objects with string
joiner = ","

myList = ["this", "is", "a", "join", "example"]
print("Joined:" + joiner.join(myList))

myDict = {"key": "value", "key2":"value2"}
print("Joined:" + joiner.join(myDict))
print("Joined:" + joiner.join(myDict.keys()))
print("Joined:" + joiner.join(myDict.values()))

# swap 2 string
str1 = "1234"
str2 = "abcd"

str1, str2 = str2 , str1
print("Str1: " + str(str1) + " - Str2:" + str(str2))
