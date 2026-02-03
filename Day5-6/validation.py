import re

def is_valid_email(email):
    if not re.match(r"^[a-zA-Z._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
        #"[^@]+@[^@]+\.[^@]+"
        return False
    return True

def is_valid_mobile(num):
    # return len(num==10) and num.isdigit()
    if not re.match(r"^[6-9]\d{9}$", str(num)):
        return False
    return True

def is_strong_password(pwd):
    return len(pwd) > 8 and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd)