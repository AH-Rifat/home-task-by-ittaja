class Numbers:
    def odd(self):
        for i in range(1,101):
            if(i % 2 == 0):
                print(i)

    def even(self):
        for i in range(1,101):
            if(i % 2 != 0):
                print(i)
    
    def prime(self):
        for num in range(1,101):
           if num > 1:
               for i in range(2, num):
                   if (num % i) == 0:
                       break
               else:
                  print(num)

number = Numbers()
print("List of Odd Numbers")
number.odd()
print("List of Even Numbers")
number.even()
print("List of Prime Numbers")
number.prime()