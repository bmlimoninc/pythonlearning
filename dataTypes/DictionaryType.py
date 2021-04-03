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