'''
Iteration
Iterable
Iterate

Generator is a special type of function that return an iterator object instead of using a
return to send back a single value. It uses yield to produce a series of result over time.
The function pause its execution after yield, maintaining its state between iterations.

Features          Return      Yield
ends functions    Yes         NO
stores state      no          yes
returns           single      multiple values one by one
memory usage      high        low
'''

def data():
    for i in range(1,6):
        yield i

print(data())

for i in data():
    print(i)

def fun():
    yield 1
    yield 2
    yield 3
    yield 4


for val in fun():
    print(val)

for i in range(3):
    print(i)

obj = fun()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

def fun():
    cnt =1
    while cnt <= 5:
        yield cnt
        cnt+=1

obj = fun()
for n in obj:
    print(n)


def demo():
    a = yield "First yield"
    print("Data Received: ",a)
    b = yield "Second yield"
    print("Data Received: ",b)


g =demo()
print(next(g))
print(g.send(1000))
print(g.send(2000))

def data():
    while True:
        val = yield
        print("data is:",val)

g = data()
next(g)
g.send(10)
g.send(102)
g.send(103)
g.send(10)
g.close() #stop generator
