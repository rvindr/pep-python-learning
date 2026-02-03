#why the index start from 0? -> 
# diff b/w casefold and lower
# check center and casefold method working
# how to find all the occurence index of any substring -> we need to use regex
# list vs array
# if we have multiple values in a string but we want to replace a specific substring then?
# append vs extend method in list
# deep and shallow copy
# types of recursion
# what is function
# ** we use for folding and unfolding?
#-------------------------------------------------------------------------------------
# String

# abc = "LPU"
# print(abc)
# print(type(abc))

# n = 'university'
# print(abc)
# print(type(abc))

#print char 
# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

#slicing
a = "take an email id from"
# print(a[::2])
# print(a[::-1])

# take an email id from the user and print the username from that email id and the username will be before @
# email = input("enter email\n")
# print(email.split('@')[0]) 

# print(email[0:len(email)-10])
# print(email[:email.index('@')])

# index = 0
# for i in range(len(email)):
#     if email[i]=='@':
#         index = i
#         break
# print(index)
# print(email[:index])


# name, city = 'rvi', 'sirsa'
# print('My name is ', name, 'and belongs from ',city)
# print(f'My name is {name} and belongs from {city}')
# print("My name is {} and belongs from {}".format(name, city))
# print("My name is %s and belongs from %s"%(name, city))

#escape character
# print('My name is:\travinder\nI am from:\tsirsa')

# print("C:\\Users\\rvind\\Downloads")
# print(r"C:\Users\rvind\Downloads")

a = 'lpu'
# print(a[2])
# print(dir(str))
# print(f'len(): {len(a)}')
# print(f"capitalize() {a.capitalize()}")
# print(f'casefold(): {a.casefold()}')
# print(f'center: {a.center(16,"*")}')
# print(a.startswith('Uni')) # case sensitive
# print(a.endswith('ity')) # case sensitive
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.find('L')) # if substring not found then return -1, return first matched string index
# print(a.index('L')) # if substring not found then raise value error

# print(a.replace('l','r')) # string is immutable, replace method return new string
# print(a)

name = 'My name is,ravinder'
# print(name.split(',')) # by default split by sapce

# r ='    ndj     '
# print(r.strip())
# print(r.rstrip())
# print(r.lstrip())

# greet = 'Hey! How can i help you?'
# import re
# print(re.findall('H',greet))  # return list of all occurences 
#-------------------------------------------------------------------------------------

# list

items = ['apple']
# print(type(items))

items.append('banana')

# print(items)

# for item in items:
#     print(item, end = "\t\t")

# for index, item in enumerate(items):
#     print(f'Index: {index} and item {item}')

# student  = ['ravi', 'mohit']
# roll_no = [1, 2]

# for st, roll in zip(student, roll_no):  # index matching
#     print(st, roll)

items1 = ['teachers', 'instructors']
# items1.append(items)
# print(items1)
# print(items1[2][1])
# # items1.extend(items)
# # print(items1)

# items.insert(0,200)
# print(items)

# # items.pop(0)
# items.remove('apples') # raise value error if value not found
# print(items)


# num = [10, 2, 30]
# print(num)
# num[1] = 20
# # num[2] = ['LPU']
# print(num)

# a = [10, 20, 30]
# b = a #reference of a 
# print(a)
# print(b)
# a[1] = 800
# print(b)

# a = [10, 20, 30]
# # b = a.copy() #copy of a 
# b = a[:]
# print(a)
# print(b)
# a[1] = 800
# print(b)
# print(a)
#-------------------------------------------------------------------------------------
'''
- Task1 : Create an empty list for storing the items to buy in Shopping list
- Task2 : Now store the number of items to the shopping list: Watch, laptop, shoes, pen, clothes
- Task3: Add a new item to the shopping list
- Task4: 
'''


# print('--------------------------------------------')

# shopping_list = ['watch', 'laptop', 'shoes', 'pen', 'clothes']
# print(shopping_list)

# print('--------------------------------------------')

# shopping_list.append('wallet')
# print(shopping_list)

# print('--------------------------------------------')

# print(shopping_list[0])

# print('--------------------------------------------')

# print(shopping_list[-1])

# print('--------------------------------------------')

# for item in shopping_list:
#     print(item)

# print('--------------------------------------------')

# print(shopping_list[1:3])


# shopping_list[3] = 'Notebook'
# shopping_list.remove('clothes')
# # shopping_list.pop(-2)

# print('--------------------------------------------')

# print(shopping_list)
#-------------------------------------------------------------------------------------
#tuples

# shopping_list = ['watch', 'laptop', 'shoes', 'pen', 'clothes']
# print(shopping_list, type(shopping_list))

# shopping_tuple = ('watch', 'laptop', 'shoes', 'pen', 'clothes')
# print(shopping_tuple, type(shopping_tuple))


#-------------------------------------------------------------------------------------
#dict

a = {
    "name":['ravi', 'mohit'],
    "course":"python"
}
# print(a)
# print(type(a))
# print(a['course'])
# print(a['name'][0])
# print(a.keys())
# print(a.values())
# print(a.items())
# print('name' in a)
# print('ravis' in a['name'])
# a['roll'] = [10,13]

# for key, value in a.items():
#     print(f'Key: {key} Value: {value}')

# del a['roll']
# print(a)



# inventory = {}
# inventory['product1'] = {
#     "name": "mobile phone",
#     "quantity":5,
#     "price":20000,
#     "release_year":"2020"
# }
# inventory['product2'] = {
#     "name": "laptop",
#     "quantity":10,
#     "price":50000,
#     "release_year":"2023"
# }


# print(inventory)

# print('release_year' in inventory['product1'])
# print('release_year' in inventory['product2'])

# del inventory["product1"]['release_year']
# del inventory["product2"]['release_year']

# print(inventory)

#-------------------------------------------------------------------------------------
#set 

# se = {}
# print(type(se)) # dic

# s = {7,14,5,6,7,3,2,1}  # set first sort the elements then remove duplicate
# print(s)

# lst = ['lpu', 'cu', 'ILM', 'SRMU', 'cu']
# set_lst = set(lst)
# print(set_lst)

# set_lst.add('cdlu')
# set_lst.remove('lpu')
# print(set_lst)
# print('cdlu' in set_lst)

# a = {2,4,6,8,10}
# b = {1,2,3,4,5,6}
# print(a&b)
# print(a.intersection(b))
# print(a.difference(b))
# print(a.union(b))

# li = [i for i in range(1,11)]
# print(li)


# a=[x for x in li if x%2==0]
# print(a)

# b=[5*x for x in range(1,11)]
# print(b)

# c =[x for x in range(5,51,5)]
# d =[x for x in range(1,51) if x%5==0]
# print(c)
# print(d)


# student= [1,2,3]
# roll_no = [4,5,6]

# for st, roll in zip(student, roll_no):
#     print(st*4, roll)

# break continue pass

#-------------------------------------------------------------------------------------
#function
# def greet(name='ravi'): #default argument
#     print("Kya haal hai" , name)
# greet()

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum+=num
#     return sum

# print(add(1,2,3,4))

# def odd(num):
#     return [i for i in range(num+1) if i%2 != 0]

# print(odd(9))


# def calculate_salary(basic_salary):
#     '''Return net salary'''
#     HRA = basic_salary * 0.2
#     DA = basic_salary * 0.1
#     gross_salary = HRA + DA + basic_salary
#     Tax = gross_salary * 0.12
#     return round(gross_salary-Tax,2)


# print(calculate_salary(75000))

def calculate_bill(amount, gst=18, discount=0):
    gst_amount = amount + (amount*(gst/100))
    return gst_amount-(gst_amount*discount/100)


print(calculate_bill(1000, discount=10))