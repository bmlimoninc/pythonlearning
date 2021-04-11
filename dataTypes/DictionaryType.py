print("Output : ")
# Mapping Type:	Dictionary

mydict = {"key": "value", "key2": "value2"}
print("Dict", type(mydict), " value:", mydict)

mydict2 = {"1": 1, "key2": 2}
print("Dict", type(mydict2), " value:", mydict2)

mydict3 = {"1": 1, "key2": 2}
print("Dict", type(mydict3), " value:", mydict3)

mydict4 = {"1": 1, "key2": 2}
print("Dict", type(mydict4), " value:", mydict4)

mydictofOtherTypes = {"1": 1, "key2": {"key21": "dict21", "key22": "dict22"}, "key3": [2, ["1"]]}
print("DictofOtherTypes", type(mydictofOtherTypes), " value:", mydictofOtherTypes)

###########################################################
# dictionary Tips

myDict = {"key": "value", "key2": "value2"}

# how to get value of key
print("Value for {} is: {}".format("key", mydict.get("key")))

# how to set a value for key
myDict["key"] = "thisIsNewValue"
print("New Dictionary is " + str(myDict) )

# How to get Keys in Dictionary
print("Keys in Dictionary are " + str(myDict.keys()) )
# How to get Values in Dictionary
print("Values in Dictionary are " + str(myDict.values()) )
myDict.clear()


# easy access to keys and Values
myDict = {"key": "value", "key2": "value2"}
print("myDict:" + str(myDict))
firstVal, secondVal = myDict.values()
firstKey, secondKey = myDict.keys()

print("First Value:", firstVal)
print("Second Value:", secondVal)
print("First Key:", firstKey)
print("Second Key:", secondKey)
