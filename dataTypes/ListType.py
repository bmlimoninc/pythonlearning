print("Output : ")
# Sequence Type List
myList = [21, 1, 2, 3, 4]
print("List", type(myList), " value:", myList)

myList2 = ["item1", "item2", "item3", "item4"]
print("List2", type(myList2), " value:", myList2)

myList3 = [1 + 2j, 2 + 2j, 3 + 2j, 4 + 2j, ]
print("List3", type(myList3), " value:", myList3)

myList4 = ["item1", 2, 1 + 2j, "item4", 5, 6, 7 + 2j]
print("List4", type(myList4), " value:", myList4)

myListofList = [["inlist1", "inlist2"], [1, 2, 3], "item3"]
print("ListofList", type(myListofList), " value:", myListofList)

###################################################################
# List Tips

print()
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# how to access elements of list
print("myList[3]: " + str(myList[3]))

myList[3] = 11  # how to change list item
print("List : " + str(myList))

myList.append(12)  # how to add item to list
print("List : " + str(myList))

myList.remove(5)  # how to remove item from list
print("List : " + str(myList))

myList.sort()  # how to sort List
print("List : " + str(myList))

# how to concatanete two list
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

list3 = list1 + list2
print("List3:" + str(list3))

#  how to get sub list from 2 till 5
subList = myList[1:4]
print("Sublist : " + str(subList))
# Remark! myList[f]
# List slicing
myList = [1, 2, 3, 4]
print("Sublist : " + str(myList[1:]))
print("Sublist : " + str(myList[:2]))
print("Sublist : " + str(myList[1:3]))

# how to use Lists as Stack
myList = [1, 2, 3]
myList.append(33)  # stack.push(33)
print("myList as Stack: " + str(myList))

poped = myList.pop()  # stack.pop()
print("myList as Stack: " + str(myList) + " poped:" + str(poped))
myList[-1]  # stack.peek()
print("myList as Stack: " + str(myList[-1]))

# how to use Lists as Queue
myList = [1, 2, 3]
myList.append(33)  # queue.push(33)
print("myList as Queue: " + str(myList))
poped = myList.pop(0)  # queue.pop()
print("myList as Queue: " + str(myList) + " poped:" + str(poped))
myList[0]  # queue.peek()
print("myList as Queue: " + str(myList[0]))

# how to reverse a list
list1 = [1, 2, 3]
print("Reversed list:" + str(list1[::-1]))

# how to iterate on List
myList = [1, 2, 3]
for i in range(len(myList)):
    print(" myList[" + str(i) + "] : " + str(myList[i]))

for i in myList:
    print(" myList element : " + str(i))

# List Comprehension
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# find odd numbers in List
oddList = []
for i in myList:
    if i % 2 == 1:
        oddList.append(i)
print("Odd List: " + str(oddList))

oddList = [i for i in myList if i % 2 == 1]
print("Odd List: " + str(oddList))

# easy access to keys and Values
myList = [1, 2, 3]

key1, key2, key3 = myList
print("Key1:", str(key1))
print("Key2:", str(key2))
print("Key3:", str(key3))

# List slicing slice [start:stop:step]
myList = [1, 2, 3, 4,5,6,7,8]
print("Sublist : " + str(myList[1:]))
print("Sublist : " + str(myList[:2]))
print("Sublist : " + str(myList[1:3]))
print("Sublist : " + str(myList[1:6:2]))
print("Sublist : " + str(myList[1::2]))
print("Sublist : " + str(myList[:]))
print("Sublist : " + str(myList[::-1]))

