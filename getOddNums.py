listNums = [5, 3, 8, 123, 456, 32, 24, 23, 45, 21]

oddNumCount = 0
for index, value in enumerate(listNums):
	if (listNums[index] % 2)  != 0 :
		oddNumCount = oddNumCount + 1

print oddNumCount