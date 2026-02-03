#Problem Statement: (Authentication System)
# create an authentication abstraction
# requirements: abstract class authenticator
#               abstract method: authenticate(credentials), credentials is a dictionary
# implement: PasswordAuth, if user is admin and having password admin1234 then return only "password Authentication Successful" otherwise "Password Authentication Failed"
#            OTPAuth, get an OTP and check in this function if OTP matches with 123456 then return 'Successful' otherwise 'Failed'

from abc import ABC, abstractmethod
class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credentials):
        pass

class PasswordAuth(Authentication):
    def authenticate(self, credentials):
        # if credentials.get("username") == "admin" and credentials.get("password") == "admin1234":
        #     return "Password Authentication Successful"
        # else:
        #     return "Password Authentication Failed"
        username = credentials.get("username")
        password = credentials.get("password")
        if username == "admin" and password == "admin1234":
            return "Password Authentication Successful"
        else:
            return "Password Authentication Failed"

class OTPAuth(Authentication):
    def authenticate(self, credentials):
        # if credentials.get("otp") == "123456":
        #     return "OTP Authentication Successful"
        # else:
        #     return "OTP Authentication Failed"
        otp = credentials.get("otp")
        if otp == "123456":
            return "OTP Authentication Successful"
        else:
            return "OTP Authentication Failed"
 
pa = PasswordAuth()
print(pa.authenticate({"username":"admin","password":"admin1234"}))
otp_auth = OTPAuth()
print(otp_auth.authenticate({"otp":"123456"})) 