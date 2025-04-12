
d = {123: [1234, 5000], 451: [4321, 10000], 120: [9876, 50000], 100: [7890, 100000]}
class Atm:
    __counter = 0
    def __init__(self,card_number:int):
        Atm.__counter+=1
        self.card = card_number # instance variable
        self.__balance = d.get(card_number)[1] # instance variable ( incapsulated variable )
        self.__pin = d.get(card_number)[0] # instance variable  ( incapsulated variable )
        # print('balance:',self.balance, 'pin:', self.pin)
        c=0
        while True:
            p = int(input('Enter your pin: '))
            if p == self.__pin:
                self.__menu()
                break
            elif c>2:
                print('Your account is blocked for 24 hours')
                break
            else:
                print('Wrong Pin Please Enter the correct Pin')
            c+=1
    def __menu(self):
        n = int(input('''
            Enter 1 withdraw the amount: 
            Enter 2 to deposit the amount:
            Enter 3 to check the balance
            Enter 4 to change the pin
            '''))
        if n ==1:
            self.__withdraw()
        elif n== 3:
            self.__check_balance()
        elif n==2:
            self.__deposit()
        elif n==4:
            self.__change_pin()
        else:
            print('Thank you')
            
    def __withdraw(self):
        amount = int(input('Enter the Amount: '))
        fetched_amount = d.get(self.card)[1]
        if amount <= fetched_amount:
            d.get(self.card)[1]-=amount
            print('Amount withdrwal successful ')
        else:
            print("Insuffient Balance")
        self.__menu()
    def __check_balance(self):
        print('Your account balance is: ', d.get(self.card)[1])
        self.__menu()
    def __deposit(self):
        amount = int(input('Enter the Amount: '))
        d.get(self.card)[1] += amount
        print('Amount deposit successful ')
        self.__menu()
    def __change_pin(self):
        n = int(input('Enter your old pin: '))
        if n== self.__pin:
            n = int(input('Enter your new pin: '))
            d.get(self.card)[0]=n
        else:
            print('Incorrect Pin')
        self.__menu()
