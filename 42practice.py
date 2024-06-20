# Create Account class with 2 attributes balance and account_number. Create methods for debit, credit  and printing the balance.

class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_number = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "has been debited from your account")
        print("Your remaining balance is: Rs.", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "has been credited to your account")
        print("Your updated balance is: Rs.", self.balance)
    
    def print_balance(self):
        return self.balance
    
acc1 = Account(10000, 123456)
acc1.debit(500)
acc1.credit(2000)

print("Your current balance is: Rs.", acc1.print_balance())


            