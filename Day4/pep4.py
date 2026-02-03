'''
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input(parameter) and returns a new function(same function with some modification).
def check(func):
    def wrap(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return wrap

def log(fun):
    def wrap(a,b): 
        print("The values are:",a,b)
        return fun(a,b)
    return wrap

@check #decorator
def div(a,b):
    # if a<b:
    #     a,b = b,a
    return a/b

def sub(a,b):
    # if(a<b):
    #     a,b = b,a
    return a-b

@log
def add(a,b):
    return a+b

res = add(5,7)
print(res)

res = div(2,4)
print(res)

sub = check(sub) #decorator
res1 = sub(7,1)
print(res1)
'''

'''
import math
a = 25
print(a**(0.5))
print(math.sqrt(a))
print(math.pow(4,2))
print(math.ceil(2.7))
print(math.floor(2.7))
'''

'''
import random as r #aliasing(giving a short name to random as 'r')
print(r.random())
print(r.randint(2,9)) #includes both endpoints
print(r.randrange(2,9)) #doesn't include endpoint
lst = ['HP', 'Dell', 'Apple', 'ASUS', 'SONY']
r.shuffle(lst)
print(lst)
print(r.sample(lst,k=3)) #returns any 3 values from lst
'''
'''
import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date(2026,1,30))
print(datetime.time(10,30,45))

now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
'''


# def check(func):
#     def wrap(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return wrap

# @check
# def div(a,b):
#     if a<b:
#         a,b = b,a
#     return a/b

# import parentD4 #concept: module (in the same folder) and packages
# # if in folder named 'cal' -> import cal.parent or from cal import parent; if done using cal.parent call using cal.parent i.e., 
# # print(cal.parent.add(4,5)) -> here cal will be the package and parent will be the module
# # from parentD4 import add #name 'parentD4' is not defined : wrong way

# '''
# The __pycache__ folder in Python is a directory where the interpreter stores compiled bytecode files (.pyc files) for modules that have been 
# imported. This mechanism helps speed up the loading of modules by avoiding the need to recompile the source code every time the module is
#  imported. When you run a Python program, the interpreter compiles the source code into bytecode, which is an intermediate representation of 
#  the code. This bytecode is then stored in the __pycache__ folder. The next time the module is imported, Python can skip the compilation step 
#  and load the precompiled bytecode directly, which speeds up the startup time of the program.
# '''

# from functools import reduce #why does this work?
# print(parentD4.add(4,5))
# print(parentD4.sub(10,9))

# from cal import logic as p
# print(p.factorial(5))

# # or

# # import cal.logic
# # print(cal.logic.factorial(5))


# def addition(func):
#     def check(a, b):
#         if a < b:
#             a, b = b, a
#         return  func(a,b)
#     return check

# @addition
# def add(a,b):
#     return a-b

# print(add(4,2))

