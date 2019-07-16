


def returnDigits(number):
	result = number
	digit = 0
	while result > 0:
		result = result / 10
		digit = digit + 1

	return digit


number = 52324324124
retDigit = returnDigits(number)
print'retDigit = ', retDigit