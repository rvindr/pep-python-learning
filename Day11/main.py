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