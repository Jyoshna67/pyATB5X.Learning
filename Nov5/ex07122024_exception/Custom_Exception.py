class LowBalanceCustom(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(message)
balance=100
withdraw=int(input("Enter the withdraw amount"))
if withdraw>balance:
    raise LowBalanceCustom("Balance is low")
else:
    print("Remaining Balance",balance-withdraw)