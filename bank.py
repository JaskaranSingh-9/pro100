class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        new_amount = 100000
        print("Your balance is :"+str(new_amount))

    def withdrawl1(self,amount):
        new_amount = 100000 - amount
        print("amount widthdraw is "+str(amount) + ". Your remaining balance is "+ str(new_amount))
        main()


def main():
    
    Account = input("Please enter your acount number: ")
    Card_number = input("Insert your card number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("enter amount to withdraw")
        amount = int(input("Enter the amount:- "))
        new_user.withdrawl1(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()