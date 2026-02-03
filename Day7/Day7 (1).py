# In Python, name mangling is a mechanism used within classes to automatically modify the name of any identifier that starts with two 
# or more leading underscores and does not end with two or more trailing underscores. 
# The primary purpose is to prevent accidental name conflicts (collisions) when a class is subclassed, not to enforce strict privacy. 
'''
class abc:
    def __show(self):
        print("Class ABC")

class xyz(abc):
    def __show(self):
        print("Class XYZ")

obj1 = xyz()
obj1._abc__show()
'''
'''
class Animal:
    def sound(self):
        return "animal sounds"    

class dog(Animal):
    def sound(self):
        return "woof woof"

class cat(Animal):
    def sound(self):
        return "meowww"

pet = [dog(),cat(),Animal()]
for i in pet:
    print(i.sound())
'''
'''
# class abc:
#     def area(self,r):
#         return r*r

# class xyz(abc):    
#     def area(self,l,b):
#         return l*b

class Calculator:
    def multiply(self, a=1, b=3, *args):
        result = a*b
        for n in args:
            result *= n
        return result  

cal = Calculator()

print(cal.multiply())
print(cal.multiply(3,5))
print(cal.multiply(2,3,5))
'''
'''
# class Emp:
#     def __init__(self, fname, lname, sal):
#         self.fname = fname
#         self.lname = lname
#         self.sal = sal
#         self.email = fname +"." +lname+"@gmail.com"

# johan = Emp('Johan','David',98000)
# ritik = Emp("Ritik",'Kumar',7689)
# print(ritik.email) #Ritik.Kumar@gmail.com
# ritik.lname = 'singh' 
# print(ritik.email) #Ritik.Kumar@gmail.com

class Emp:
    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
    
    @property
    def email(self):
        return self.fname +"."+self.lname+"@gmail.com"
    
    @email.setter
    def email(self, old_email):
        name_lst = old_email.split('@')[0].split(".")
        self.fname, self.lname = name_lst[0],name_lst[1]

johan = Emp('Johan','David',98000)
ritik = Emp("Ritik",'Kumar',7689)
# print(ritik.email()) #Ritik.Kumar@gmail.com : without property decorator
print(ritik.email)
ritik.lname = 'singh' 
ritik.email = "kumar.ritik@gmail.com" #AttributeError: property 'email' of 'Emp' object has no setter : this error is prior to adding email.setter component to this code
# print(ritik.email()) #Ritiksingh@gmail.com : without property decorator
print(ritik.email)
'''
'''
#DUCK TYPING:  if it looks like a duck and quacks like a duck then it's a duck
class Car:
    def fuel(self):
        print("Petrol, CNG, EV, Diesel")
class Bike :
    def fuel(self):
        print("Petrol, EV")
class Bicycle:
    def fuel(self):
        print("No fuel type")
class vehicle:
    def start(self, fuel_type:Car):
        print("Vehicle run on:")
        fuel_type.fuel()

creta = Car()
bullet = Bike()
ranger = Bicycle()
v1 = vehicle()
v1.start(creta)
v1.start(bullet)
v1.start(ranger)
'''
from abc import ABC , abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class PhonePay(PaymentGateway):
    def pay(self):
        print("Payment done by PhonePay")

class PayPal(PaymentGateway):
    def pay(self):
        print("Payment done by PayPal")

class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway
    
    def checkout(self):
        print("Checked Out")
        self.gateway.pay()

p1 = PhonePay()
p2 = PayPal()
pur = Purchase(p1)
pur2 = Purchase(p2)
pur.checkout()
pur2.checkout()