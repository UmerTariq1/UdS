'''
Exercise (3 points)

a) Using the slides & the script, put together a file containing the complete 
   class representing a bank account. The class should define the following
   methods:
   
   * __init__
   * withdraw
   * deposit
   * set_holder
   * __str__
   
b) Extend the withdraw function such that the minimum balance allowed is -1000.

c) Write a function apply_interest(self) which applies an interest rate of
   1.5% to the current balance and call it on your objects. Make sure that 
   the balance is applied only if the balance is not negative.
'''

class Account:
   def __init__(self, id, holder):
      self.id = id
      self.holder = holder
      self.balance = 0
      
   def deposit(self, amount):
      self.balance += amount
      
   def withdraw(self, amount):
      if amount > self.balance:
         amount_to_return = amount - self.balance
         temp = self.balance
         if amount_to_return > 1000:
            amount_to_return = 1000 
            self.balance = -1000
         else:
            self.balance = -amount_to_return
         return amount_to_return + temp
      self.balance -= amount
      return self.balance

   
   def set_holder(self, holder):
      if not isinstance(holder,str):
         raise TypeError
      self.holder = holder
   
   def __str__(self):
      res = "Account ID: " + str(self.id) + "\n"
      res += "Holder: " + self.holder + "\n"
      res += "Balance: " + str(self.balance) + "\n"
      return res

   def apply_interest(self, percentage=1.5):
      self.balance += (self.balance * percentage) / 100

      
        

if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    
    print("Create an account for John:")
    johnsAccount = Account(1, "John Doe")
    
    print("Create an account for Jane:")
    janesAccount = Account(2, "Jane Doe")
    
    print("John deposits $2000")
    johnsAccount.deposit(2000)
    print(johnsAccount)
    
    print("Jane deposits $500")
    janesAccount.deposit(500)
    print(janesAccount)
    
    print("Apply interest:")
    johnsAccount.apply_interest()
    print(johnsAccount)
    janesAccount.apply_interest()
    print(janesAccount)
    
    print("Set holder of John's account to Joe Average")
    johnsAccount.set_holder("Joe Average")
    print(johnsAccount)
    
    print("Joe withdraws $2500")
    print("Joe gets:", johnsAccount.withdraw(2500))
    print(johnsAccount)
    
    print("Jane withdraws $2500")
    print("Jane gets:", janesAccount.withdraw(2500))
    print(janesAccount)
    
    