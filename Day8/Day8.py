'''
class Students:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
    
    # def __str__(self):
    #     return f"Student Name: {self.name} & studies in {self.cls} at LPU"

    def __repr__(self): #The __repr__ method is also defined to give a more formal string representation of the object.
        return f"Student({self.name},'{self.cls}')" 

s1 = Students("Alan", "BTech")
print(s1)
# The above code defines a Students class with a custom string representation. 
# method __str__ is overridden to provide a meaningful output when an instance is printed.
# When we create an instance of Students and print it, it shows the name and class of the student.
'''
'''
class Shape:
    def __init__(self,shapes):
        self.shapes = shapes
    
    def __len__(self): # dunder method to return length of the object
        return len(self.shapes)

    def __getitem__(self, index): # dunder method to make the object subscriptable
        return self.shapes[index]
    
s = Shape(['Circle', 'Rectangle', 'Square', 'Polygon'])
# print(len(s.shapes))
# print(len(s))
print(s.shapes[2])
print(s[-1])
'''
'''
class Emp:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
    
    def __add__(self, other):
        return self.sal + other.sal
    
    def __gt__(self, other):
        return self.sal > other.sal
    
    def __lt__(self, other):
        return self.sal < other.sal

e1 = Emp("John", 50000)
e2 = Emp("Doe", 60000)
# print(e1 + e2)  # This will raise an error since Emp objects do not support addition
print(e1.sal + e2.sal)  # This will work and print the sum of salaries
print(e1 + e2)  # after defining __add__ -> This will now work and print the sum of salaries

print(e1.sal > e2.sal)  # This will work and print False
print(e1>e2) # This will raise an error since Emp objects do not support comparison -> after defining __gt__ method it will work

print(e1.sal < e2.sal)  # This will work and print True
print(e1<e2)  # This will raise an error since __lt__ is not defined -> after defining __lt__ method it will work
'''

# file = open('abc.txt', 'r')
# print(file)

# print(file.read())

# print(file.readline(), end='#') # to avoid new line
# print(file.readline())

# print(file.readline(5)) # reads only 5 characters from the line
# for f in file:
#     print(f,end='') # to avoid double new line

# print(file.name)
# print(file.mode)
# print(file.closed)

# file.close()


# f = open('moun.jpg', 'rb')
# f1 = open('moun_copy.jpg', 'wb')
# for i in f:
#     f1.write(i)
# f1.close()

# data = '''
# 101, Amit, amit@gmail.com\n102, Neha, Neha@gmail.com\n103, ravi, ravi@gmail.com
# '''


# with open('student.txt', 'w') as f:
#     f.write(data)

# with open('student.txt', 'r') as f:
#     # for line in f:
#     #     print(line, end='')
#     print(f.read())

error_log = '''
INFO: Request received
ERROR: Unable to connect to database
INFO: User logged in
ERROR: File not found
ERROR: File not found in dir
'''
# error_count = 0
# info_count = 0

# with open('log.log', 'w') as f:
#     f.write(error_log)
    
# with open('log.log', 'r') as f:
#     for line in f:
#         if "INFO" in line:
#             info_count+=1
#         elif "ERROR" in line:
#             error_count+=1


# print("error_count: ",error_count)
# print("info_count: ", info_count)



# with open("st_record.txt","a") as file:
#     cont = True
#     while cont:
#         st_id = input("Enter student ID: \n")
#         name = input("Enter Name: \n")
#         course = input("Enter course: \n")

#         file.write(f"{st_id},{name},{course}\n")
#         exit = input("Do you want to register more.\n Press y/n\n")
#         if exit.lower() == "n":
            # cont = False

# from datetime import datetime

# with open("feedback.txt","a") as file:
#     cont = True
#     while cont:
#         feedback = input("Enter feedabck\n")
#         file.write(f"{datetime.now()}: {feedback}\n")
#         exit = input("Do you want to register more.\n Press y/n\n")
#         if exit.lower() == "n":
#             cont = False




import csv

# with open("prac.csv","r") as file:
#     reader = csv.reader(file)
#     dict_reader = csv.DictReader(file)
#     # print(reader)

#     # for i,j in enumerate(reader):
#     #     print(j[2])

#     next(reader)  # to skip header row
#     for i in reader:
#         print(i[2])

# with open("prac.csv","r") as file:
#     csv_reader = csv.reader(file)

#     with open("prac_copy2.csv","w", newline='') as file1:
#         csv_writer = csv.writer(file1, delimiter="\t")
#         for row in csv_reader:
#             csv_writer.writerow(row)


with open("temp.csv","r") as file:
    csv_reader = csv.DictReader(file)

    with open("prac_copy4.csv","w", newline='') as file1:
        f = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(file1, fieldnames=f)
        csv_writer.writeheader()
        for row in csv_reader:
            # del row['last_name']
            csv_writer.writerow(row)
