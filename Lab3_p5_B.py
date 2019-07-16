# Addition:
# One common problem when prompting for numerical input occurs 
# when people provide text instead of numbers. 
# When you try to convert the input to an int, you will get a ValueError. 

# Write a program that prompts for two numbers. 
# Add them together and print the result.  

# Catch the ValueError if either input value is not a number and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.


# function definition

def add2NumbersButChar():
	inputList = []
	counter = 0
	while counter < 2:
		inputNum = raw_input('Enter a number: ')
		inputNum = unicode(inputNum, "utf-8")

		if (inputNum.isdecimal() == True):
			inputList.append(int(inputNum))
			counter = counter + 1
		else:
			print 'the input is not a number, try again!'

	return inputList[0] + inputList[1]

# function usage
retSum = add2NumbersButChar()
print 'The sum is ', retSum



