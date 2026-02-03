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


class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError('age never be negative')
    print('Age is: ', age)

try:
    check_age(-19)
except AgeError as e:
    print("age error: ", e)