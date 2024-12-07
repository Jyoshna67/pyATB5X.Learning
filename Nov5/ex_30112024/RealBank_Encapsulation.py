class Bank:

    def __init__(self,balance,account_number):
        self.balance=balance
        self.__account_number=account_number

    def check_balance(self):
            print(self.balance)
    def deposit(self,amount):
            self.balance=self.balance+amount
    def show_me_account_number(self): #show_me function is used to display private variables.
        print(self.__account_number)

hdfc=Bank(balance=100,account_number=797474987489)
hdfc.deposit(100)
hdfc.check_balance()
print(hdfc.balance)
hdfc.show_me_account_number()

