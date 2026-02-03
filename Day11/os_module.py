import os
'''
print(os.getcwd()) # current directory
os.chdir("../../") #change directory
print(os.getcwd()) 
os.chdir('PEP')
print(os.getcwd()) 
'''

# D:\M.Tech\placement\PEP\Day11\os_module.py absolute path
# Day11\os_module.py relative path

# os.mkdir('fullstack')
# os.mkdir('../fullstack')
# os.makedirs('fullstack/java/dsa')

# print(os.listdir())
# cwd = os.getcwd()
# dirt = "cal\ravi"
# print(os.path.join(cwd, dirt))

# print(os.name) #nt and posix
'''
nt for window
posix for macos
oS2
ce
java for android
riscois 
'''

# file = open('module.txt','w')
# file.write("im working on os module")
# file.close()

# file = open('module.txt','r')
# print(file.read())
# file.close

# print(os.path.exists('module.txt'))
# print(os.path.exists('modules.txt'))
print(os.path.getsize('module.txt'))
print(os.path.dirname('day11/module.txt'))
print(os.path.isfile('module.txt'))
print(os.path.islink('module.txt'))
print(os.path.isdir('module.txt'))