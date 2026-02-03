'''
#user will enter one number and system will guess a number, if both numbers match  print "WOW" and do it until the numbers match and also count the no. of times
import random as r
count = 0
secret_num = r.randint(1,10)

def check():
    global count
    num = int(input("Enter any number between 1 and 10: "))
    if num != secret_num:
        count = count+1
        check()
    else:
        print("WOW!, you guessed it in",count,"tries.")        

check()
'''

'''
#Problem Statement: EMI Calculator for Loan Portal
import math
def calculate_emi(principal, rate, tenure):
    r = rate/(12*100)
    n = tenure
    emi = principal*r*math.pow(1+r,n)/(math.pow(1+r,n)-1)
    return emi

print(calculate_emi(10000, 10, 24))
'''

'''
#Problem Statement: Secure OTP Generator
#Requirements: generate 6-digit numeric OTP; should be random every time; simulate 5 OTP generations
import random as r
otp = set()
def generate_otp():
    while True:
        val = r.randint(100000,999999)
        if val not in otp:
            otp.add(val)
            return val

for _ in range(5):
    generate_otp()

print(otp)
'''

'''
#Problem Statement: Bank Transaction Authorization
def bank_transaction(user_role):
    def authorize(amount):
        if user_role == 'admin':
            return "Transaction Approved"
        elif user_role == 'user' and amount <= 50000:
            return "Transaction Approved"
        else:
            return "Request Denied"
    return authorize

txn = bank_transaction("user")
print(txn(70000))    
'''

#Problem Statement: Employee Login Tracker
import datetime
def calculate_Work_hours(login_time, logout_time):
    time_format = "%Y-%m-%d %H:%M"
    login = datetime.datetime.strptime(login_time, time_format)
    logout = datetime.datetime.strptime(logout_time, time_format)

    work_duration = logout - login
    hrs, rem = divmod(work_duration.seconds,3600)
    minutes = rem//60
    
    if hrs >= 8:
        extra = "Overtime Worked"
    else:
        extra = "Regular Hours Worked" 

    return f"{hrs}h {minutes}m",extra  
    
login_time = "2026-01-20 09:30"
logout_time = "2026-01-20 18:45"

print(calculate_Work_hours(login_time, logout_time))



# 