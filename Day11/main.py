# raising custom exception
def print_num(num):
    if num > 0:
        print('positive number')
    else:
        raise ValueError("negative number")
try:
    print_num(-10)
except ValueError as e:
    print("error: ",e)


class AgeError:
    pass

def check_age(age):
    if age < 0:
        print('age never be negative')
    print('Age is: ', age)

check_age(-19)