'''
class emp:


    # Member function: normal function
    # data member : variable

    dept = "CSE" # class variable

    def __init__(self, name, salary): # Dunder method
        self.name = name # instance variable
        self.salary = salary # instance variable

    def print_detail(self):
        print(f'Employee Name: {self.name}')
        print(f'Employee Salary: {self.salary}')
        print(f'Employee Department: {emp.dept}')

emp.dept = "Data science"
ravi = emp("Ravinder",36000) # object creation
ravi.print_detail()
'''

# method overloading
'''
class comparision:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        return self.a < other
    
obj1 = comparision(25)
obj2 = comparision(15)
print(obj1 < obj2)


# types of constructor
# 1. default
# 2. parameterized 
# 3. copy constructor

# Types of Constructors in Python:
# 1. Default Constructor - No parameters, just self
# 2. Parameterized Constructor - Accepts parameters to initialize object
# 3. Constructor with Default Values - Parameters have default values
class abc:
    #data members = variables
    #member function = normal function

    #Dunder method __init__ :  always executed when the class is being initiated
    #The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

    # def __init__(self):       #default constructor
    #     print("Constructor called") 
    company_name = 'LPU' #class variable : Shared by all instances of the class
    no_emp = 0
    increment = 1.6
    def __init__(self, fname, lname, sal):
        #instance variable : a variable that is unique to each specific object (instance) of a class. 
        #It stores data that defines the state of an individual object and is not shared across other instances of the same class. 
        self.fname = fname
        self.lname = lname
        self.sal = sal
        self.company_name = "IBM" #instance variable
        # self.no_emp+=1 #instance
        abc.no_emp+=1 #class
        # abc.increment = 1.5

    def info(self):
        print(f"Employee {self.fname} {self.lname} having {self.sal} salary.")
        print(f"works in {self.company_name}") #instance
        print(f"works in {abc.company_name}") #class

    def hello(self):
        print("Good Afternoon")

    def increase(self):
        self.sal = self.sal * abc.increment

# obj = abc() #object creation
# abc.hello(obj)  #TypeError: abc.hello() takes 0 positional arguments but 1 was given -> hello() to hello(self) -> Good Afternoon
# obj.hello() #Good Afternoon
# obj1 = abc()

obj1 = abc('abc','xyz',65678) #object creation
obj2 = abc('johan','dravid',65678)
obj1.increase()
obj3 = abc('james','bond',65678)
# obj.info()
# print(obj.no_emp)
# print(abc.no_emp)

# abc.increment = 2.5
obj3.increment = 2.5
obj3.increase()
obj2.increase()
print(obj2.sal)
print(obj1.__dict__)
print(obj3.__dict__)



'''

# class emp:
#     company_name = "LPU"
#     np_emp = 0
#     increment = 1.6
#     def __init__(self, fname, lname, sal):
#         #instance variable
#         self.fname= fname
#         self.lname = lname
#         self.sal = sal
#         emp.np_emp +=1

#     def increase(self):
#         self.sal = self.sal * emp.increment

#     # class methods are useful when you need to work rather than any particular instance of it.
#     @classmethod
#     def from_str(cls, emp_string):  # cls -> emp
#         fname,lname,sal =emp_string.split("-")
#         return cls(fname,lname,sal) # emp/cls calling constructor
    
#     # static method
#     '''
#     Static methods are essentially utility functions that are grouped within a class for 
#     organizational purposes (namespacing) but do not access or modify the class's or instance's state. 
#     '''
#     @staticmethod
#     def is_working(day):
#         if day.lower() == "sunday":
#             return False
#         return True

# ravi = emp("ravi","verma",60000)
# john = emp("john","david",50000)
# ravi.increase()
# print(ravi.__dict__)

# amit = emp("amit","david",20000)
# amit.increment = 3
# amit.increase()
# print(amit.__dict__)
# john = emp.from_str("john-david-6000")
# john.__dict__["fname"] = "rav" 
# '''
# You can inspect, modify, add, or delete attributes dynamically by
# interacting with the __dict__ dictionary, which makes it a powerful tool for metaprogramming.
# '''
# print(john.__dict__)

# print(emp.is_working("sundAy"))

'''
class BankUtils:
    @staticmethod
    def is_valid_account(acc_num):
        if not (len(str(acc_num))==12 and acc_num.isdigit()):
            return "Invalid account number"
        return "Valid account number"
    

print(BankUtils.is_valid_account(987654321321))
'''
'''
class User:

    def __init__(self, username, role):
        self.username = username
        self.role = role

    @classmethod
    def create_admin(cls, username):
        return cls(username, "Admin")
    
    
admin = User.create_admin("rvindr")
print(admin.__dict__)
#and isinstance(price, (int, float))
'''

# class Product:
#     tax_rate = 10 #10%

#     def __init__(self, price):
#         self.price = price

#     @staticmethod
#     def is_valid_price(price):
#         return price > 0 
    
#     @staticmethod
#     def is_valid_tax(tax):

#         if tax >= 0:
#             return True
#         else:
#             raise ValueError("Invalid tax rate") 
    
    
#     @classmethod
#     def update(cls, new_tax_rate):
#         cls.is_valid_tax(new_tax_rate)
#         cls.tax_rate = new_tax_rate

#     def final_price(self):
#         if not self.is_valid_price(self.price):
#             return "Invalid price"

#         return self.price + (self.price * Product.tax_rate/100)
    
# item1 = Product(100)
# print(item1.final_price())
# Product.update(20)
# print(item1.final_price())



# class Cart:
    
#     discount = 00

#     def __init__(self, *prices):
#         self.prices = [price for price in prices]

#     def add_item(self, price):
#         self.prices.append(price)

#     def total_price(self):
#         total_price = sum(self.prices)
#         return  total_price - (total_price * Cart.discount/100)
    
#     @classmethod
#     def update_discount(cls, new_discount):
#         cls.discount = new_discount

    
# items = Cart(10,30,50)
# print(items.total_price())
# items.update_discount(10)
# print(items.total_price())
# items.add_item(10)
# items.update_discount(0)
# print(items.total_price())


'''
Design a class AuthSystem

Req:
    - Static method:
        validate_passoword(pwd)
    - instance method:
        - login(pwd)
    - logic:
        - pwd must be strong:
            must be a greater than 8 char and one uppercase and one digit must be there, one char upper and one lower
        - store login status

'''

'''
class AuthSystem:
    
    def __init__(self, username, pwd):
        self.username = username
        AuthSystem.validate_password(pwd)
        self.pwd = pwd
        self.is_login = False
    @staticmethod
    def validate_password(pwd):
        if not ((len(pwd) >=8 
                and any(char.isupper() for char in pwd))
                and any(char.islower() for char in pwd) 
                and any(char.isdigit() for char in pwd)):
            raise ValueError("!not a strong password")
        

    
    def login(self, username, pwd):
        if username == self.username and pwd == self.pwd:
            self.is_login = True
            return "Logged in successfully"
        return "Invalid username or password"
    
ravi = AuthSystem("rvindr", "vedhkdh@993Arma")
print(ravi.__dict__)
print(ravi.login("rvindr", "vedhkdh@993Arma"))
print(ravi.__dict__)

'''

'''
class Student:
    def enroll_course(self, *course_name):
        self.course_name = [name for name in course_name]

class Faculty:
    def assign_course(self, *course_name):
        self.assign_course_name.append(name for name in course_name)

class College:

    college_name = "LPU"

    @classmethod
    def update(cls, new_name):
        cls.college_name = new_name

ravi = Student()
ravi.enroll_course("Python","dbk")
print(ravi.__dict__)

sachin = Faculty()
sachin.assign_course("Data science with python", "java full stack")
print(sachin.__dict__)

College.college_name = "CDLU"
print(College.college_name)

'''
'''

class College:
    college_name = "LPU"
    
    @classmethod
    def change_name(cls, name):
        cls.college_name = name

class Student:
    def __init__(self, n):
        self.name = n 
        self.course = []

    def enroll_course(self, *course):
        self.course.extend([c for c in course])

class Faculty:
    def __init__(self, n):
        self.name = n
        self.courses = []

    def assign_course(self, *courses):
        self.courses.extend([course for course in courses])

s1 = Student("ravi")
s1.enroll_course("Python", "SQL")
s1.enroll_course("Python", "SQL")

College.change_name("RVI")

f1 = Faculty("Sachin")
f1.assign_course("Python Full Stack", "Java")

print(s1.__dict__)
print(f1.__dict__)
print(College.college_name)

'''

'''
# inheritance - types of inheritance
class emp:
    def __init__(self):
        self.company = "ABC"
    def show(self):
        print("I am from emp class")

class staff(emp):
    def __init__(self,name):
        self.name = name
        super().__init__()
    
    def info(self):
        print("My name is",self.name,"working in ",self.company)
        self.show()

s1 = staff("Amit")
s1.info()

'''

'''   create three class a,b,c , class a have one function display

class b have one function display 1
with the help of object c class you have to call display 1 and display function and class c have one show function that is called 
'''

# class A:
    
#     def display(self):
#         print("Displaying result from class a")

# class B:
#     def display1(self):
#         print("Displaying result from class b")

# class C(A, B):
#     def show(self):
#         print("Displaying result from class a")

# c1 = C()
# c1.display()
# c1.display1()
# c1.show()

'''
class A:
    
    def display(self):
        print("Displaying result from class a")

class B(A):
    def display1(self):
        print("Displaying result from class b")

class C(B):
    def show(self):
        print("Displaying result from class a")'''


# class Person:
#     def __init__(self, name):
#         self.name = name


# class EMP(Person):
#     def role(self):
#         print(self.name, "works as an employee")


# class Intern(Person):
#     def role(self):
#         print(self.name, "is an intern")

# e1 = EMP("ravi")
# e1.role()

# i1 = Intern("edm")
# i1.role()


'''
class Person:
    def __init__(self, name):
        self.name = name


class EMP(Person):
    def role(self):
        print(self.name, "works as an employee")


class Intern(Person):
    def role(self):
        print(self.name, "is an intern")

class Project:
    def __init__(self, name):
        self.project_name = name

class TempLeas(EMP, Project): #hybrid
    def __init__(self, name, pr_name):
        EMP.__init__(self, name)
        Project.__init__(self, pr_name)

    def info(self):
        print(self.name, "leads project", self.project_name)

lead = TempLeas("ravi","python" )
lead.info()


'''

'''
#ambiguity or diamond problem in inheritance

method resolution order to solve ambiguity in python, interface in java

mro is the sequence in which the python search for the attributes or methods in the class inheritance it means
its an important with the multiple inheritance where a class inherits from multiple parent classes and conflicts 
can come up if methods with the same name exist into the different parent classes

'''
'''
class A:
    def display(self):
        print("A class")
class B:
    def display(self):
        print("B class")

class C(B, A):
    def __init__(self):
        super().display()

obj = C()

'''

class EMP:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary():
        pass

class FullTimeEMP(EMP):
    pass

class ContractEMP(EMP):
    pass