# Mini Bank Application

class Customer():
    '''
    This Class Developed By Arjun and Describes Bank Operators
    '''
    bankname = 'MASTER BANK'

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('After deposit balance: ', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Funds, cannot perform this transaction')
        else:
            self.balance = self.balance - amount
            print('After wthdraw, balance: ', self.balance)

print('Welcome to', Customer.bankname)
name = input('Enter Your Name: ')
c = Customer(name)
while True:
    print('D - Deposit \n W - Withdrawal \n E - Exit')
    option = input('Choose your option')
    if option.lower() == 'd':
        amount = float(input('Enter amount to deposit: '))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdraw: '))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for banking with us')
        break
    else:
        print('Your option is invalid, please chose valid option to proceed.')


