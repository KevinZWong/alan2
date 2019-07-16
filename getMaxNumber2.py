listNums = [5, 3, 8, 123, 456, 32, 24, 23, 45, 21]

maxNum = 0
for index, value in enumerate(listNums):
	if listNums[index] > maxNum:
		maxNum = listNums[index]

print maxNum