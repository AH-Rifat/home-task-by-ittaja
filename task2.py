class Students:
    def __init__(self, name,roll,department,mobileNumber):
        self.name = name
        self.roll = roll
        self.department = department
        self.mobileNumber = mobileNumber

    def printIdCard(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Department:",self.department)
        print("Mobile Number:",self.mobileNumber)
        print('')
        


print("List of students ID Card")
print("--------------------------")
std = Students('jabed', '41','CSE','016524254125')
std.printIdCard()

std = Students('Rejwan', '37','CSE','018664254125')
std.printIdCard()

std = Students('Shaminaj', '26','CSE','013524635125')
std.printIdCard()