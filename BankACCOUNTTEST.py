print("FirstFinance")

class bankAccount(object):

    def __init__(self, Name, Acc_no, sort_code, Balance):
        self.name = Name
        self.acc_no = Acc_no
        self.sort_code = sort_code
        self.Balance = Balance

    def Deposit(self, amt):
        print("The currect Balance is", self.Balance)
        print("I have deposited {} in my account".format(amt))
        self.Balance =self.Balance + amt
        print("My new account balance is", self.Balance)

    def withdraw(self, amt):
        if self.Balance < 0:
            print("Insufficient Balance")
            print("Add credits to withdraw")


        print("The current balance is", self.Balance)
        print(" I am withdrawing {} from my account".format(amt))
        self.Balance = self.Balance - amt
        if (self.Balance < 0):
            print("Operation not allowed")

    def getbalance(self):
        print("The current balance is", self.Balance)

    def info(self):
        print(" The account holder is", self.name)
        print(" The account number {} and sort code {}".format
              (self.acc_no, self.sort_code))
        print("The account balance is: ",self.Balance)

    def creatATM(self):
        print("card Number: 1234 5678 9101 2131")
        print("EXP {} {}". format(10,2030))
        print("CVV 345")
        print("NAME", self.name)

    def regaddress(self, addr):
        print("Current address is:", addr)
    def phonenumber(self, NUM):
        print("My phone number is", NUM)

        

u1 = bankAccount("Arda Guler", 200515, "05-15-16", 0)
u1.Deposit(50)
u1.withdraw(60)
u1.getbalance()
u1.info()

print ("===BUILDING A PROMPT FOR THE BANK ACCOUNT")

name = input("Enter your name: ")
acct_no = input("Enter your Account Number: ")
sort_code = input("Enter your sort code: ")
balance = float(input("Enter your balance: "))

u2 = bankAccount(name, acct_no, sort_code, balance)

while True:
    print("\n ======= Bank Menu =======")
    print("1. deposit")
    print("2. withdraw")
    print("3. Check Balance")
    print("4. Account Info")
    print("5. Create ATM Card")
    print("6. register Address")
    print("7. register Phone Number")
    print("Exit")

    choice = input("Choose an option from (1-8): ")

    if choice == "1":
        Amount = float(input("Enter Deposit amount: £"))
        u2.Deposit(Amount)

    elif choice == "2":
        Amount = float(input("Enter Withdraw Amount"))
        u2.withdraw(Amount)

    elif choice == "3":
            u2.getbalance()

    elif choice == "4":
        u2.info()

    elif choice == "5":
        u2.creatATM()

    elif choice == "6":
        addr = input("Enter your address")
        u2.regaddress(addr)

    elif choice == "7":
        phone = input("Enter your phone number")
        u2.phonenumber(phone)

    else:
        print("Thank you for using our bank")
        exit() #123123


        