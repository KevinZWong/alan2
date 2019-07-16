

number = input('Please enter a number for digits: ')  

digit = 0
while number > 0:
	number = number / 10
	print number
	digit = digit + 1
	print digit

print 'digit = ', digit