
# class definition
class SimpleCounter:
	# contructor of the class SimpleCounter
	def __init__(self):
		self._count = 0   

	# class method to increament the _count value
	def increment(self):        
		self._count += 1   

	# class method to clear the _count value	
	def clear(self):        
		self._count = 0   

	# class method to get the _count value	
	def get_value(self):        
		return self._count

# class usage:
# object => my_counter

# to create an class-object from class: SimpleCounter
# and calls the __init__() contructor method
my_counter = SimpleCounter()

# Use the object: my_counter to call it's method:
# my_counter.get_value() to get the value of self._count
ret = my_counter.get_value()
print ret

# Use the object: my_counter to call it's method:
# my_counter.increment(), and increase it value by 1
my_counter.increment()

# Use the object: my_counter to call it's method:
# my_counter.increment(), and increase it value by 1
my_counter.increment()

# Use the object: my_counter to call it's method:
# my_counter.get_value() to get the value of self._count
ret = my_counter.get_value()
print ret

# Use the object: my_counter to call it's method:
# my_counter.clear() to reset the value of self._count back to 0
my_counter.clear()

# Use the object: my_counter to call it's method:
# my_counter.get_value() to get the value of self._count
ret = my_counter.get_value()
print ret