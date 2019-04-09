#For this challenge, create a bank account class that has two attributes:
#owner
#balance

#and two methods:
#deposit
#withdraw
#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class bank_account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def print_info(self):
        print('Owner name: {}'.format(self.owner))
        print('Your balance: ${}'.format(self.balance))
    
    def deposit(self,deposit_amount):
        print('you deposited ${}'.format(deposit_amount))
        self.balance+=deposit_amount
        print('as of now, your account balance is ${}'.format(self.balance))
      
    def withdraw(self,withdraw_amount):
     if withdraw_amount>self.balance:
        print('funds unavialable!')
     else:
         print('you withdraw ${}'.format(withdraw_amount))
         self.balance-=withdraw_amount
         print('as of now, your account balance is ${}'.format(self.balance))

        
     

  

    
my_account=bank_account('Rea',100)
my_account.print_info()
my_account.deposit(20)
my_account.withdraw(50)

