from random import randint

class bank_account:

    def __init__(self,name,ac_type,balance=0):

        self.name = name
        self.ac_type = ac_type
        self.balance = balance
        self.acc_no = randint(1111111111,9999999999)

    def deposit(self):

        amount = int(input("Enter amount : "))
        self.balance += amount
        print(f"New balance is {amount}.\n")

    def withdraw(self):

        amount = int(input("Enter amount : "))

        if(self.balance == 0 or self.balance-amount <= 0):

            print("Insufficient balance to withdraw this amount.\n")

        else:
            
            self.balance -= amount
            print("Withdrawal successfull. New balance is {self.balance}.\n")

    def check_balance(self):

        print(f"Balance is {self.balance}.\n") 

name = input("Enter account holder's name : ")

ac_type = input("Enter aacount type : ")

obj = bank_account(name,ac_type)

print("\nAccount created...\n")

print(f"Account holder's name : {obj.name}")

print(f"Account type : {obj.ac_type}")

print(f"Account Number : {obj.acc_no}")

print(f"Balance : {obj.balance}.") 

while True:

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    option = int(input("\nEnter option : "))

    if(option == 1):

        obj.deposit()

    elif(option ==2 ):

        obj.withdraw()

    elif(option == 3):

        obj.check_balance()

    elif(option == 4):

        exit()

    else:

        exit()
    
