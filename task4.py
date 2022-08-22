class Number:
    def sum(self,a = None,b = None, c = None):
        if a!=None and b!=None and c!=None:
         print("Sum of numbers:", a+b+c)
        else:
         print("Sum of numbers:",a+b)

getNum = Number()
print('@method overloading')
getNum.sum(20,20)
print('')
getNum.sum(20,20,20)