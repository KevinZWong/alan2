# Message:
# Write a function called display_message() that prints a simple greeting.  Call the function, and make sure the message displays correctly.

# function definition
def display_message(name):
	var1 = 8
	print 'Hello World! ', name
	print 'hhh', var1
	print 'testing'

# function usage:
#display_message('alan', firstName, lasName)
var1 = 5
print var1
display_message('kevin')

print display_message('guo')


#Relationship between variable and function




#fileObj = open('Student_data.data', 'r')   #/Users/gwong/Sources22/alan/Student_data.data
fileObj = open('/Users/gwong/Sources22/alan/Student_data.data', 'r')
#print fileObj.readlines()
print fileObj.tell()
print fileObj.seek(19)
print fileObj.tell()

print fileObj.readline()
print fileObj.tell()
print fileObj.readline()
print fileObj.tell()
print fileObj.readline()
print fileObj.tell()












class AlanClass:
	def __init__():
		self.firstName = 'alan'
		self.lastName = 'wong'
		self.grade = '10th'

	def getFirstName()
		return self.firstName

	def getLastName()
		return self.lastName

	def setFirstName(firstName)
		self.firstName = firstName

	def setLastName(lastName)
		return self.lastName = lastName	


alanObj = AlanClass()
print alanObj.getFirstName()
print alanObj.getLastName()



# class or object definition
class ClassStudent:
	def __init__(firstName, lastName, grade):
		self.firstName = firstName
		self.lastName = lastName
		self.grade = grade

	def getFirstName()
		return self.firstName

	def getLastName()
		return self.lastName

	def setFirstName(firstName)
		self.firstName = firstName

	def setLastName(lastName)
		return self.lastName = lastName	

Usage:

alanObj = ClassStudent('alan', 'wong', '10th')
print alanObj.getFirstName()
print alanObj.getLastName()

kevinObj = ClassStudent('kevin', 'wong', '7th')
print kevinObj.getFirstName()
print kevinObj.getLastName()


johnObj = ClassStudent('john', 'he', '10th')
print johnObj.getFirstName()
print johnObj.getLastName()

