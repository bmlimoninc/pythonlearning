################ Read File ###############
f = open("readwritefilesDir/textFile", "r")
print(f.read())
f.close()

# Partial reading
# read only 5 character
f = open("readwritefilesDir/textFile", "r")
print(f.read(5))
f.close()

# read line by line
f = open("readwritefilesDir/textFile", "r")
print(f.readline())
print(f.readline())

f.close()

# Iterate on file
f = open("readwritefilesDir/textFile", "r")
for line in f:
    print(line)

f.close()
print()
################ Write File ###############
f = open("readwritefilesDir/writeTextFile", "w")
f.write("This is Write File Example\n This is a way of adding line by line data")
f.write("\nOr simply add new line like this")
f.write("\nDont forget to add new line at the beginning ....")

f.close()

f = open("readwritefilesDir/writeTextFile", "r")

print(f.read())
print()
f.close()

################ Append File ###############

f = open("readwritefilesDir/writeTextFile", "a")
f.write("\nNow we append this line to file ")
f.close()


f = open("readwritefilesDir/writeTextFile", "r")
print(f.read())
print()
f.close()

