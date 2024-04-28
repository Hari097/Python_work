class ATM:
    actual_amount = 1000
    def __init__(self,pin,name):
        self.pin = pin 
        self.name = name 
    def Balance(self):
        bank_balance = ATM.actual_amount
        return f"hi {self.name} your balance {bank_balance}"

    def deposite(self,new_amount,pin):
       

        if pin == 4400:
        
            add_amount = new_amount
            ATM.actual_amount += add_amount 
            return self.Balance()
        else:
            return "your pin wrong"
    @classmethod    
    def wirthdraw(cls,withdraw_amount):

       
        if cls.actual_amount > withdraw_amount:
            cls.actual_amount -= withdraw_amount 
            return f"your account balance {cls.actual_amount}"
        else:
            return "insufficient balance account" 
        
    @staticmethod
    def greeting():
        print(
            "welcom HHM Bank" 

        )

        

        

atm_mechine = ATM(4400,"hariharan")
atm_mechine.greeting()
print(atm_mechine.Balance())
name = input("Enter you name : ")
atm_pin = int(input("Enter you 4 digit ATM pin: "))
deposite_amount = int(input("Enter you deposite amount : "))
deposite = atm_mechine.deposite(deposite_amount,atm_pin)
print(deposite)
cash_withdraw = int(input("enter the withdraw amount: "))
witdraw_amount = atm_mechine.wirthdraw(cash_withdraw)
print(witdraw_amount)

