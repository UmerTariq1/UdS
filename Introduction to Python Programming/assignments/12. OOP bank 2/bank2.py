'''
Exercise: 6 points

Fill out the missing parts in the code below.

HINTS:

* You will have to replace the 'pass' statements with some
  meaningful code. Pay attention to the comments which
  describe what is expected.

* You may want to comment out parts of the main application
  while coding! If you just run this, you will get errors at first!


'''

#######################################
# CLASSES FOR THE BANKING APPLICATION #
#######################################

class Customer:
    ''' objects of this class represent customers.
    The customer ID is supposed to be assigned automatically
    when a new customer object is created. The first ID should
    be 0, the next 1, and so on.
    Attributes:
    - first name
    - last name
    - age
    '''
    current_customer_id = 0
    # CONSTRUCTOR
    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age
        self.cust_id = Customer.current_customer_id

        Customer.current_customer_id += 1
        
    # INSTANCE METHODS
    def increment_age(self):
        ''' increases the age by 1 year '''
        self.age += 1

    def __str__(self):

        # res = "First name : " + self.first_name + "\n"
        # res += "Last name : " + self.last_name + "\n"
        # res += "Age : " + str(self.age) + "\n"
        # return res
        return "[Customer ID=" + str(self.cust_id) \
              + ", Fist name=" + str(self.first_name) \
              + ", Last name=" + str(self.last_name) \
              + ", Age=" + str(self.age)+ "]"


    # SETTERS
    def set_lastname(self, ln):
        ''' sets the last name of a customer '''
        self.lastname = ln

    # STATIC METHODS
    ''' write a method called print_info here that prints
    out how many customers have been created so far '''
    @staticmethod
    def print_info():
        print("Number of customers created so far : ", Customer.current_customer_id)


class Account:
    ''' Objects created from this class
    represent accounts.
    Account ID is assigned automatically when creating
    an account object.
    Attributes:
    - number
    - holder (object of class 'Customer')
    - balance '''

    current_account_id  = 0
    # CONSTRUCTOR
    def __init__(self, holder):
        ''' the initialization method is called right after
        an object has been created. used to initialize attributes'''

        self.holder = holder

        self.acc_id = Account.current_account_id
        Account.current_account_id += 1

        self.balance = 0

    # INSTANCE METHODS
    def withdraw(self, amount):
        ''' withdraw an amount of money from an account object:
        subtract the amount from the balance, does not allow a
        negative balance. Returns the amount that was actually
        withdrawn from the account. '''
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount
        return amount
        
    def deposit(self, amount):
        ''' deposit an amount of money into an account:
        add the amount of money to the balance '''
        self.balance += amount

    def set_holder(self, new_holder):
        ''' change the account holder.
        We could validate, whether new_holder is 
        a Customer object, as required. '''
        self.holder = new_holder
        
    def __str__(self):
        ''' returns a string describing the account object '''
        return "[Account: ID=" + str(self.acc_id) \
              + ", BALANCE=$" + str(self.balance) \
              + ", HOLDER=" + str(self.holder)+ "]"


class Bank:
    ''' class for objects that represent a bank
    Attributes:
    - name
    - accounts (dictionary, listed by account ID)
    - customers (dictionary, listed by customer ID) '''
    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.customers = {}

    # INSTANCE METHODS
    def print_accounts(self):
        ''' print out all accounts of the bank '''

        print("\n** ACCOUNTS **")
        for each_account in self.accounts.keys():
            print(self.accounts[each_account])


    def print_customers(self):
        ''' prints out all the customers of the bank '''
        print("\n** CUSTOMERS **")
        for each_customer in self.customers.keys():
            print(self.customers[each_customer])

    def add_customer(self, customer):
        ''' adds a customer object to the bank's customers '''
        self.customers[customer.cust_id] = customer

    def add_account(self, account):
        ''' adds an account object to the bank's accounts '''
        self.accounts[account.acc_id] = account

    def deposit(self, acc_id, amount):
        ''' deposit money into the account '''
        self.accounts[acc_id].deposit(amount)

    def withdraw(self, cust_id, acc_id, amount):
        ''' withdraw money from the account with the given ID,
        but only if its holder has the given customer ID.
        Returns the amount of money (=cash)'''
        if cust_id == self.accounts[acc_id].holder.cust_id:
            return self.accounts[acc_id].withdraw(amount)
        else:
            print("Customer ID does not match with the holder id.")
            return 0


    def __str__(self):
        ''' returns a descriptive string for the bank '''
        res = "Name : " + self.name + "\n"
        res += "** ACCOUNTS ** \n"
        for each_account in self.accounts.keys():
            res = res + print(self.accounts[each_account]) + "\n"
        for each_customer in self.customers.keys():
            res = res + print(self.customers[each_customer]) + "\n"
        
        return res
        


##############################
# BANKING APPLICATION - MAIN #
##############################

if __name__ == "__main__":
    # Create a new bank object
    bank = Bank("PYTHON-BANK")
    print(bank)

    # Create a few customers and add them to the bank object
    marc = Customer("Marc", "Schulder", 85)
    bank.add_customer(marc)
    stefan = Customer("Stefan", "Thater", 76)
    bank.add_customer(stefan)
    maja = Customer("Maja", "Biene", 2)
    bank.add_customer(maja)

    # Print out all the customers of the bank
    bank.print_customers()
    
    # Create a few accounts and add them to the bank object
    marcsAcc1 = Account(marc)
    bank.add_account(marcsAcc1)
    marcsAcc2 = Account(marc)
    bank.add_account(marcsAcc2)
    stefansAcc = Account(stefan)
    bank.add_account(stefansAcc)
    majasAcc = Account(maja)
    bank.add_account(majasAcc)

    # # Print out all the accounts of the bank
    bank.print_accounts()

    # Deposit money into accounts
    print("\nMarc deposits $400 into account with ID 1.")
    bank.deposit(1, 400)
    print("Stefan's customer ID:", stefan.cust_id)
    print("Stefan deposits $1000 into account with ID 2.")
    bank.deposit(2, 1000)

    # Print out all the accounts of the bank
    bank.print_accounts()

    # Withdraw money from some accounts
    print("\nMarc tries to withdraw from Stefan's account.")
    cash = bank.withdraw(0, 2, 100)
    print("Marc got:", cash)
    print("Now Marc tries to withdraw from his own account.")
    cash = bank.withdraw(0,1,100)
    print("Marc got:", cash)

    # Number of customers
    print("")
    Customer.print_info()
    print("Number of customers that have been added to the bank:", len(bank.customers.keys()))   
    