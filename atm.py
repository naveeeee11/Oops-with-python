class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def get_pin(self):
        returnself.pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin changed")
        else:
            print("not allowed")
            
    def menu(self):
        user_input=input("""
              hello, how would you like to proceed ?
              1.Enter 1 to create pin
              2.Enter 2 to deposit
              3.Enter 3 to withdraw
              4.Enter 4 to check balance
              5.Enter 5to exit
""")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Bye")
            
        
    def create_pin(self):
        self.pin=input("Enter your pin")
        print("Pin set successfully")
    def deposit(self):
        temp=input("Enter your pin")
        if temp ==self.pin:
            amount=int(input("Enter the amount "))
            self.balance=self.balance+amount
            print("Deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        temp=input("Enter your pin")
        if temp ==self.pin:
            amount=int(input("Enter the amount "))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation successful")
            
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
                 
    def check_balance(self):
        temp=input("Enter your pin")
        if temp ==self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        
