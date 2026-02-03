class AgeError(Exception):
    pass
class WeakPasswordError(Exception):
    pass


def validate_data(age,pwd):
    if not isinstance(age,int):
        raise ValueError('age must be numeric')
    if age<18:
        raise AgeError("Age must be greater than or equal to 18")
    if len(pwd) <8:
        raise WeakPasswordError("Password must contain atleast 8 character")

try:
    validate_data(18,'12345678')
    validate_data(17,'12345678') #Error:  Age must be greater than or equal to 18
    validate_data('ab','12345678') #Error:  age must be numeric
    validate_data(19,'2345678') #Error:  Password must contain atleast 8 character
except Exception as e:
    print('Error: ', e)
else:
    print('else block') # if no exception occurs then only execute
finally:
    print('finally block') #always execute