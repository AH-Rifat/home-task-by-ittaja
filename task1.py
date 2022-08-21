class Students:

    def setMarks(self):
        self.name1 = int(input("Enter Jabed Marks: "))
        self.name2 = int(input("Enter Rejwan Marks: "))
        self.name3 = int(input("Enter Shaminaj Marks: "))
        print('')
        self.average(self.name1,self.name2,self.name3)
        self.highest(self.name1,self.name2,self.name3)
        self.lowest(self.name1,self.name2,self.name3)
        

    def average(self,name1,name2,name3):
        return print("Their Average Marks is: ",self.name1+self.name2+self.name3/3)

    def highest(self, name1,name2,name3):

        if(self.name1 < self.name2):

            if(self.name2 < self.name3):
                print("Highest marks in OS is Shaminaj: ",self.name3)
            else:
                print("Highest marks in OS is Rejwan: ",self.name2)

        else:
            print("Highest marks in OS is Jabed: ",self.name1)

    def lowest(self, name1,name2,name3):
        if(self.name1 > self.name2):

            if(self.name2 > self.name3):
                print("Lowest marks in DBMS is Shaminaj: ",self.name3)
            else:
                print("Lowest marks in DBMS is Rejwan: ",self.name2)

        else:
            print("Lowest marks in DBMS is Jabed: ",self.name1)


s = Students()
s.setMarks()
