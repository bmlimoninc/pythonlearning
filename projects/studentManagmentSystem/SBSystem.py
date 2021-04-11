from studentSystemv1 import *

class SBSystem(object):
    def __init__(self):
        self.lastID = -1
        self.studentList = []
        self.instructorList = []
        self.departments = []

    def getStudentID(self):
        self.lastID += 1
        return self.lastID

    def addStudent(self, newStudent):
        self.studentList.append(newStudent)

    def listStudent(self):
        print(self.studentList)

    def addInstructor(self, newInstructor):
        self.instructorList.append(newInstructor)

    def listInstructor(self):
        print(self.instructorList)

    def getInstructorFromID(self, ID):
        for inst in self.instructorList:
            if inst.instructorId == ID:
                return inst

        return None

    def getInstructorID(self):
        return len(self.instructorList)

    def addDepartment(self, newPrograms):
        self.departments.append(newPrograms)

    def listDepartments(self):
        print(self.departments)

    def getNewDepartmentID(self):
        return len(self.departments)

    def getDepartmentFromName(self, departmentName=""):
        for dept in self.departments:
            if departmentName.__eq__(dept.departmentName):
                return dept

        return None

