from datetime import datetime

def require_login(func):
    def wrap(is_login):
        if not is_login:
            return "access denied"
        print("Access at: ", datetime.now())
        return func(is_login)
    return wrap

@require_login
def view_dashboard(is_login):
    return "Dashboard loaded"

print(view_dashboard(True))
print(view_dashboard(False))