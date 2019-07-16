#class definition
class BankAccount:   
	# class constructor method  
	def __init__(self):              
		self.balance = 0    

	# class method to withdraw money from BankAccout
	def withdraw(self, amount):             
		self.balance -= amount              
		return self.balance

	# class method to deposit money into BankAccout	
  	def deposit(self, amount):  
  		self.balance += amount
  		return self.balance



#Usage:
# To creat an object of BankAccount, called: a
a = BankAccount()

# To creat an object of BankAccount, called: b
b = BankAccount()

# To deposit 100 dollar into object: a
# accout balance = 100
print a.deposit(100) 

# To deposit 50 dollar into object: b
# accout balance = 50
print b.deposit(50) 

# To withdraw 10 dollar into object: b
# accout balance = 40
print b.withdraw(10) 

# To withdraw 10 dollar into object: a
# accout balance = 90
print a.withdraw(10)


