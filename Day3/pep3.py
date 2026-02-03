'''
lst = [1,2,3,4,5,6,7,8,9,10]
lst1 = []
lst2 = []

def split_list(input_list):
    for i in input_list:
        if i % 2 == 0:
            lst1.append(i)
        else:
            lst2.append(i)
    return lst1, lst2

split_list(lst)
print("Even List:", lst1)
print("Odd List:", lst2)
'''

'''
a = 10 #global variable
def add():
    # global a
    a = 20 #local variable
    print(globals())
    globals()['a'] = 900
    print("Inside ",a)

add()
print("Outside ", a)
'''

'''
def info(**val): #keyword variable length arguments
    for k,v in val.items():
        print(k," : ",v)

info(name='Mohit', city='ldh', tech='py', clg='lpu', clss='mtechcse')
'''

'''
def func (num): #normal function
    return num * num
print(func(5))

func1 = lambda num: num * num #anonymous function:  a function that is defined without a name
print(func1(7))

add = lambda x,y: x + y
print(add(5,10))

sub = lambda x,y: x - y
print(sub(5,4))
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even = [x for x in numbers if x % 2 == 0] #list comprehension
print(even)

def check(num):
    #return num % 2 == 0
    if num % 2 == 0:
        return True
even_numbers = filter(check, numbers) #filters elements from a list based on a condition
print(list(even_numbers)) 

even_numbers1 = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers1))
'''

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = map(lambda x: x * 2, numbers) #applies a function to all items in an input list
print(list(doubled_numbers))
'''

'''
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0

for i in numbers:
    sum += i
print(sum)

def add(a,b):
    return a + b
final_sum = reduce(add, numbers) #applies a function of two arguments cumulatively to the items of a sequence
print(final_sum)

fsum = reduce(lambda a,b: a + b, numbers)
print(fsum)
'''

# def fun(n):
#     if n<5:
#         return fun(n+1)
#     print(n)
#     return
# fun(2)

# def rec(n):
#     if n>0:
#         print(n)
#         rec(n-1)
#     return
# rec(5)

# def fun(n):
#     if n<=0:
#         return
#     else:
#         #print(n) # for printing in decreasing order - Tail Recursion
#         fun(n-1)
#         print(n) # for printing in increasing order - Head Recursion
# fun(5)

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) 
    
# for i in range(10):
#     print(fibonacci(i), end=" ")

# n = 10
# count = 0
# a,b,c = 0,1,0
# while count < n:
#     print(a, end=" ")
#     c = a+b
#     a = b
#     b = c
#     count += 1

# high order functions: functions that can take other functions as arguments or return functions as results
def cube(n):
    return n*n*n

def operate(value, func):
    #return func(value) #cube(value) 5*5*5 = 125
    for i in value:
        result = func(i)
        print(result)

val = [1,2,3,4,5]
operate(val, cube)
#val = 5
#res = operate(val, cube)
#print("Cube of", val, "is", res)

def square(n):
    return n*n
operate(val, square)

