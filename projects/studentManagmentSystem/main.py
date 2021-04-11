from SBSystem import *

bmlimonincSBS = SBSystem()


def addStudent():
    newStudentName = input("Enter Your Student Name:  ")
    newStudentMidName = input("Enter Your Student MidName:  ")
    newStudentSurName = input("Enter Your Student SurName:  ")
    newStudentID = bmlimonincSBS.getStudentID()

    newStudent = student(newStudentName, newStudentMidName, newStudentSurName, 1)

    newStudentDepartmentName = input("Enter Your Student Program:  ")
    newStudentDepartment = bmlimonincSBS.getDepartmentFromName(newStudentDepartmentName)

    if newStudentDepartment is None:
        print("\nNo Department does not exist\n")
        return

    newStudentMentorID = int(input("Enter Your Student Mentor ID:  "))
    newStudentMentor = bmlimonincSBS.getInstructorFromID(newStudentMentorID)

    if newStudentMentor is None:
        print("\nInstructor does not exist\n")
        return

    newStudent.addMentorInfo(newStudentMentor, newStudentDepartment)
    newStudent.registerStudent2Program(newStudentID)

    bmlimonincSBS.addStudent(newStudent)


def listStudent():
    if len(bmlimonincSBS.studentList) == 0:
        print("\nNo Student registered yet. Please register student\n")

    for std in bmlimonincSBS.studentList:
        std.printClass()


def addInstructor():
    newInstructorName = input("Enter Your Instructor Name:  ")
    newInstructorMidName = input("Enter Your Instructor MidName:  ")
    newInstructorSurName = input("Enter Your Instructor SurName:  ")

    newInstructorDepartmentName = input("Enter Your Instructor Department Name:  ")

    newInstructorDepartment = bmlimonincSBS.getDepartmentFromName(newInstructorDepartmentName)

    if newInstructorDepartment is None:
        print("\nDepartment Does not Exist\n")

        print(len(bmlimonincSBS.instructorList))

        return

    newInstructorID = bmlimonincSBS.getInstructorID()
    newInstructor = instructor(newInstructorName, newInstructorMidName, newInstructorSurName,
                               1, newInstructorDepartment, newInstructorID)

    bmlimonincSBS.addInstructor(newInstructor)


def listInstructor():
    if len(bmlimonincSBS.instructorList) == 0:
        print("\nNo Instructor Added Yet. Please Add Instructor\n")

    for inst in bmlimonincSBS.instructorList:
        inst.printClass()


def addDepartment():
    newDepartmentName = input("Enter Your DepartmentName Name:  ")
    newDepartmentID = bmlimonincSBS.getNewDepartmentID()

    newDepartment = department(newDepartmentName, newDepartmentID)
    bmlimonincSBS.addDepartment(newDepartment)


def listDepartments():
    if len(bmlimonincSBS.departments) == 0:
        print("\nNo Department Added yet. Please Add Department\n")
    for prg in bmlimonincSBS.departments:
        prg.printClass()



switch = {
    1: addStudent,
    2: addInstructor,
    3: listStudent,
    4: listInstructor,
    5: addDepartment,
    6: listDepartments,
}


def menuDisplay():
    print("################################")
    print("This is Basic Console Student Management System")
    print("Please enter your choice.       ")
    print("1. Add Student                  ")
    print("2. Add Instructor               ")
    print("3. List Students                ")
    print("4. List Instructors             ")
    print("5. Add Department               ")
    print("6. List Departments             ")
    print("0. Exit                         ")
    choice = input("Enter Your choice:  ")

    return choice


def choice2Function(argument):
    # Get the function from switcher dictionary
    func = switch.get(argument, "nothing")
    # Execute the function
    return func()


def menu():
    choice = int(menuDisplay())
    if choice == 0:
        return False

    choice2Function(choice)
    input("Press enter to continue")

    return True


def SRSystem():
    while menu():
        pass




SRSystem()
exit()

newProgram1 = department("Comp", 0)
newProgram2 = department("Eng",  1)
newProgram3 = department("Ceng", 2)
bmlimonincSBS.addDepartment(newProgram1)
bmlimonincSBS.addDepartment(newProgram2)
bmlimonincSBS.addDepartment(newProgram3)

newInstructor1 = instructor("ali", "muhittin", "topalak",
                            1, newProgram1, "1")
newInstructor2 = instructor("halil", "", "Multu",
                            2, newProgram2, 2)
newInstructor3 = instructor("basri", "", "mumcu",
                            3, newProgram3, 3)

bmlimonincSBS.addInstructor(newInstructor3)
bmlimonincSBS.addInstructor(newInstructor2)
bmlimonincSBS.addInstructor(newInstructor1)