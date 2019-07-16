# Write a Python class which has two methods get_String 
# and print_String. get_String accept a string from 
# the user and print_String print the string in upper case


# class definition
class getNprintString:
	def __init__(self):
		self._stringStorage = ''

	def get_String(self, stringFromUser):
		self._stringStorage = stringFromUser
		return self._stringStorage

	def print_String(self):
		print self._stringStorage


#Usage:
# create the class-object from getNprintString
stringObject = getNprintString()

# Input a string a class-object
print stringObject.get_String('input a string')

# To call class-object function to print out the stored string
stringObject.print_String()
