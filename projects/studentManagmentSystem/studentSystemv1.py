import datetime


class person(object):
    def __init__(self, inName, inMidName, inSurName, inPersonId=-1):
        self.name = inName
        self.midName = inMidName
        self.surName = inSurName

        self.personID = inPersonId

    def printClass(self):
        print("\tIdentity: " + self.name + " " + self.midName + " " + self.surName)


class instructor(person):
    def __init__(self, inName, inMidName, inSurName, inPersonId, inDepartment, inInstructorId=-1):
        super().__init__(inName, inMidName, inSurName, inPersonId)
        self.department = inDepartment
        self.instructorId = inInstructorId

    def printClass(self):
        print("Instructor : ")
        super().printClass()
        print("\tInstructor ID:" + str(self.instructorId))
        self.department.printClass()


class department(object):
    def __init__(self, departmentName, departmentId=-1):
        self.departmentName = departmentName
        self.departmentId = departmentId

    def printClass(self):
        print("Department : ")
        print("\tDepartment Name:" + self.departmentName + " - Program ID:" + str(self.departmentId))
        print()


class student(person):
    def __init__(self, inName, inMidName, inSurName, inPersonId=-1):
        super().__init__(inName, inMidName, inSurName, inPersonId)
        self.studentID = -1
        self.studentMentor = None
        self.studentDepartment = None
        self.term = None

        self.registrationDate = datetime.datetime.now()

    def addMentorInfo(self, inInstructor, inProgram):
        self.studentMentor = inInstructor
        self.studentDepartment = inProgram

    def registerStudent2Program(self, inStudentID, inTerm=1):
        self.studentID = inStudentID
        self.term = inTerm

    def printClass(self):
        print("\nStudent : ")
        super().printClass()

        print("\n\tStudent Term:" + str(self.term))
        print("\tRegisteration Date:" + str(self.registrationDate))

        self.studentDepartment.printClass()
        self.studentMentor.printClass()
