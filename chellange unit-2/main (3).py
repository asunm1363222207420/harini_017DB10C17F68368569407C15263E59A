class BankAccount:
 def _init_(self,name,no,abalance):
     self.__account_name=name
     self.__account_no=no
     self.__acccount_balance=abalance
 def deposit(self,deposit):
  b.BankAccount_account_balance=
b.BankAccount_account_balance+deposit   
 def withdraw(self,withdraw):
  b.BankAccount_account_balance=
b.Bankaccount_account_balance-withdraw
 def accountbalance(self):
      print('The balace amount is ',b.BankAccount_account_balance)
b=BankAccount("harini",123456789,50000)
print("The account holder name:",b.Bankaccount_account_name)
print("The account number:",b.BankAccount_account_no)
DA=int(input("Enter deposit amount:"))
b.deposit(DA)
WD=int(input("Enter with drawmount:"))
b.withdraw(WD)
b.accountbalance()