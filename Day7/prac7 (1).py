'''#Problem Statement: Combined Placement Challenge
class AppConfig:
    app_name = "spotify"

    def __init__(self,config):
        self.config = config
    
    @classmethod
    def load_defaults(cls):
        return cls({"testing":"done","version":"1.3"})

    @staticmethod
    def validate_config(config):
        return "version" in config and "testing" in config
        
    def display_config(self):
        return self.config

con = AppConfig.load_defaults()
print(AppConfig.validate_config(con.config))
print(con.display_config())
'''
'''
#Problem Statement: Notification Service
class Notification:
    def send(self,message):
        return f"notification recieved: {message}"

class EmailNotification(Notification):
    def send(self,message):
        return f"email notification recieved: {message}"

class SMSNotification(Notification):
    def send(self,message):
        return f"SMS notification recieved: {message}"
    
e = EmailNotification()
s = SMSNotification()

print(e.send("Today is JAVA class"))
print(s.send("class aaega?"))
'''
'''
#Problem Statement: Shape Area Calculator
import math

class Shape:
    def area(self):
        pass
        
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b 

    def area(self):
        print("Area of Rectangle is",self.l*self.b)
    
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    
    def area(self):
        print("Area of Circle is",math.pi*self.r**2)

shapes = [Rectangle(5,4),Circle(4)]
for s in shapes:
    s.area()
    '''
'''
#Probem Statement: User Account Balance
#requirements: attribute is balance
#               @property balance -> getter
#               @balance.setter -> prevent negative balance
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return f"Balance is {self._balance}"    
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative.")
        else:
            self._balance = amount

account = BankAccount(1000)
print(account.balance)  # 1000
account.balance = 500   # Update balance
print(account.balance)  # 500   
account.balance = -200  # negative balance : Error: Balance cannot be negative.
print(account.balance)  # 500
'''
'''
#Problem Statement: Employee Salary Protection
#requirements: salary is an attribute; setter: salary must be >= minimum wage; deleter: prevent deleting salary directly
class Employee:
    MIN_SAL = 20000

    def __init__(self, salary):
        self.salary = salary
    
    @property
    def salary(self):
        return self.amount
    
    @salary.setter
    def salary(self, val):
        if val < Employee.MIN_SAL:
            print("Salary Below Minimum wage.")
            return
        else:
            self.amount = val

e1 = Employee(30000)
print(e1.salary)
e1.salary = 18000
print(e1.salary)
'''
'''
#Problem Statement: Product Pricing System
class Product:
    def __init__(self, price):
        self.price = price
    
    @property
    def final_price(self):
        return self.price
    
class DiscountedProduct(Product):
    def __init__(self,price,discount):
        super().__init__(price)
        self.discount = discount
    
    @property
    def final_price(self):
        return self.price - (self.price * self.discount / 100)

p1 = DiscountedProduct(1000,30)
print(p1.final_price)
'''
#Problem Statement:  (Database Layer Abstraction[Backend Favorite])
#design an abstract database layer
#requirements: abstract class database; abstract methods: connect(),fetch(),close(); implementations: MySQLDatabse, MongoDatabse
from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def fetch(self):
        pass
    @abstractmethod
    def close(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL Database")
    
    def fetch(self):
        print("Fetched data from MySQL Database")
    
    def close(self):
        print("Closed MySQL Database connection")

class MongoDatabase(Database):
    def connect(self):
        print("Connected to MongoDB Database")
    
    def fetch(self):
        print("Fetched data from MongoDB Database")
    
    def close(self):
        print("Closed MongoDB Database connection")         

mysql_db = MySQLDatabase()
mongo_db = MongoDatabase()
mysql_db.connect()
mysql_db.fetch()
mysql_db.close()
mongo_db.connect()
mongo_db.fetch()
mongo_db.close()