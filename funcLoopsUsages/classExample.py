class Person:
    def __init__(self, name=None, midName=None, surName=None, id=-1):
        print("Person init")

        if name is not None:
            self.name = name
        if midName is not None:
            self.midName = midName
        if surName is not None:
            self.surName = surName

        self.personID = id

    def functionInClass(self):
        print("This is a function belongs to person Class")
        print("Name: ", self.name)
        print("midName: ", self.midName)
        print("surName: ", self.surName)


people = Person("this ", "is", "Class", 102)

people.functionInClass()
print(">Name   : ", people.name)
print(">midName: ", people.midName)
print(">surName: ", people.surName)

print()


class PhysicalProperty:
    def __init__(self, hairColor=None, height=None, weight=None):
        print("physicalProperty init")
        if hairColor is not None:
            self.hairColor = hairColor
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight

    def myProperty(self):
        print("This is a function belongs to physicalProperty Class")
        print("hairColor: ", self.hairColor)
        print("height   : ", self.height)
        print("weight   : ", self.weight)


class student(Person, PhysicalProperty):
    def __init__(self, inName=None, inMidName=None, inSurName=None, inId=-1
                 , inHairColor=None, inHeight=None, inWeight=None):
        Person.__init__(self,inName, inMidName, inSurName, inId)
        PhysicalProperty.__init__(self,inHairColor, inHeight, inWeight)
        print("physicalProperty init")


myStudent = student("this ", "is", "inherited Class", 101,
                    "red", 180, 108)
myStudent.functionInClass()
myStudent.myProperty()
