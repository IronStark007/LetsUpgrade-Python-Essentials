"""
Name:Ansari Mohammed Ali Nasim
Date:10/09/2020
Purpose-Python Essentials-Batch 7 Day 6 Assignment 1
"""


class BankAcc:

    def __init__(self, ownername, balance):
        self.ownername = ownername
        self.balance = balance

    def bankdetails(self):
        return f"WELCOME = {self.ownername}"

    def deposit(self):
        deposited = int(input("Enter the amount to deposit\n"))
        self.balance = self.balance + deposited
        return f"You have successfully deposited {deposited} Rs\nThe updated balance is {self.balance} Rs"

    def withdraw(self):
        withdrawal = int(input("Enter the amount to withdraw\n"))
        if withdrawal < self.balance:
            self.balance = self.balance - withdrawal
        else:
            raise ValueError("You dont have sufficient balance\nThank You for Banking with us")
        return f"You have successfully withdraw the {withdrawal} Rs\nThe updated balance is {self.balance} Rs"


if __name__ == '__main__':
    Ali = BankAcc("Ansari Mohd. Ali", 100000)
    print("Welcome to the XYZ bank")
    while True:
        acc = int(input("Enter your Acc No.\n(Hint:-please enter = 12345)\n"))
        if acc == 12345:
            print(Ali.bankdetails(), "\n")
            inp = int(input("What do you want to do:-\nEnter : 1 for Balance\n      : 2 for Withdawal\n      : 3 for Deposit\n"))
            if inp == 1:
                print(f"Your Availabe Balance is {Ali.balance} Rs")
            elif inp == 2:
                print(Ali.withdraw())
            elif inp == 3:
                print(Ali.deposit())
            else:
                print("Please Enter Only 1, 2, 3, 4")
        else:
            print("please enter 12345 to do enter your bank account")
        con = int(input("Do you want to continue\nType:1 for YES\n    :2 for NO\n"))
        if con == 1:
            continue
        elif con == 2:
            print("Thank You for Banking with us")
            break
        else:
            print("Please enter only 1 or 2")
