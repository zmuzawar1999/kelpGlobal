#defin a BankAccount
class BankAccount:

#constructor to initialize account properties
    def __init__(self, name):
        self.name=name
        self.balance=0.0

# defin the bank
class Bank:
# dictionary of code: BankAccount
    Accounts={} 

#create an bank account    
    def create(self,code, name):
        account=BankAccount(name)
        self.Accounts[code]=account

#deposit sepecific amount in an existing bank account
    
    def deposit (self,code, amount):
        if code in self.Accounts.keys():
            self.Accounts[code].balance += amount
        else:
            print ("Account doesn't exist")

#withdraw specific amount from an existing bank account, with considerable account balance 
             
    def withdraw (self,code, amount):
        if code in self.Accounts.keys():
            if self.Accounts[code].balance > amount:
                self.Accounts[code].balance -= amount
            else :
                print ("not enough balance")
        else:
            print ("Account doesn't exist")

# display the account balance
           
    def balance (self,code):
        if code in self.Accounts.keys():
            print (self.Accounts[code].name,self.Accounts[code].balance)
            
        else:
            print ("Account doesn't exist")



             
bank=Bank()
while True:
#Read the entire command
#splits it into operator and operand
    operation=input().split()
    if operation[0]=="CREATE":
        bank.create (operation[1],operation[2])
    elif operation[0]=="DEPOSIT":
        bank.deposit (operation[1],float(operation[2]))
    elif operation[0]=="WITHDRAW":
        bank.withdraw (operation[1],float(operation[2]))
    elif operation[0]=="BALANCE":
        bank.balance (operation[1])
    else:
        print("incorrect command")