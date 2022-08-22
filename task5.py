class Student():
    # constructor without parameters
    def __init__(self):
        self.firstName = "Ittaja"
        self.lastName = "Rahman"

    def showName(self):
        print('Student Name:',self.firstName,'', self.lastName)


class Department():
    # constructor with parameters
    def __init__(self, department):
        self.department = department

    def showDepartmentName(self):
        print('Department Name:', str(self.department))

std = Student()
std.showName()

departmentName = Department("CSE")
departmentName.showDepartmentName()