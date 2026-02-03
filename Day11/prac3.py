class InvalidSalaryError(Exception):
    pass


def calculate_salary(basic_salary):
    try:
        basic_salary = int(basic_salary)
    except:
        raise InvalidSalaryError("Invalid salary input")
    
    if basic_salary <= 0:
        raise InvalidSalaryError("Salary must be greater than 0")

    HRA = basic_salary * 0.2
    DA = basic_salary * 0.1
    gross_salary = HRA + DA + basic_salary
    Tax = gross_salary * 0.12
    return round(gross_salary-Tax,2)

try:
    salary = input("enter your salary: ")
    total_salary = calculate_salary(salary)
except Exception as e:
    print("Error:",e )
else:
    print('Your total salary is: ',total_salary)
finally:
    print("Salary calculated")