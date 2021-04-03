print("Output : ")
# Set Types:	set - frozenset

mySet = {"item1", "item2", "item3"}
print("Set", type(mySet), " value:", mySet)

mySet2 = {"item1", 1, 2, "item3"}
print("Set", type(mySet2), " value:", mySet2)

mySet3 = {10,2,8,1}
print("Set", type(mySet3), " value:", mySet3)

myFrozenSet = frozenset({"item1", "item2", "item3"})
print("FrozenSet", type(myFrozenSet), " value:", myFrozenSet)

myFrozenSet2 = frozenset({10,2,8,1})
print("FrozenSet", type(myFrozenSet2), " value:", myFrozenSet2)