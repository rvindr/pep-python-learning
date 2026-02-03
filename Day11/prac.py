class InsufficientBalanceError(Exception):
    pass
class NegativeAmountError(Exception):
    pass
class InvalidAmount(Exception):
    pass

class account:

    def __init__(self, account, name):
        self.account = account
        self.name = name
        self.balance = 0

    def add_balance(self, amt):
        self.balance += amt

    def transfer(self,acc_num, amt):
        if not str(amt).isdigit():
            raise InvalidAmount("Please enter valid amount")
        if amt < 0:
            raise NegativeAmountError("Transfer amount can not be negative")
        if self.balance < amt:
            raise InsufficientBalanceError("Insufficient amount")
        print("Funds transerferred")
        
ravi = account(1250335, 'ravi')
ravi.add_balance(1000)
try:
    # ravi.transfer(12316,-122)
    ravi.transfer(12316,'ddd23')
    ravi.transfer(12316,1200)
except Exception as e:
    print("Error: ",e )