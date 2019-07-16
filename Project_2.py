
#userInputList = [2, 5, 45, 25, 100, 9, 63, 55, 11, 78, 41, 47, 28, 21, 10, 65, 39, 14, 60, 99]


userInputList = []

for i in range(20):
	displayString = 'Enter ' + str(i+1) + ' of 20: '
	input_num = raw_input(displayString)
	if input_num.lstrip('-').isdigit():
		userInputList.append(int(input_num))
	else:
		print 'user input "' + str(input_num) + '" is not a number.'

#print userInputList

userInputList.sort()

lowestNum = userInputList[0] * 1.00

print 'Low : ' + str(lowestNum)

#print userInputList

userInputList.sort(reverse = True)

#print userInputList

highestNum = userInputList[0] * 1.00
print 'High : ' + str(highestNum)

total = 0.00
for num in userInputList:
	total = total + num

total = total * 1.00

print 'Total: ' + str(total)

print 'Average: ' + str(total / 20.00)