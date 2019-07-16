#!/usr/bin/python
import os

def aReadFunction(nameOfFile):
	numList = []
	try:
		fileObj = open(nameOfFile, 'r')
		numFromFile = fileObj.read()
		numList = numFromFile.split(',')
		fileObj.close()

	except IOError:
		print 'Error: can\'t find file or read data'
		
	return numList

def findPrimeNumNFactors(aNum):
	isPrimeNum = True
	factors = [1]
	for num in range(2, aNum, 1):
		if (aNum % num) == 0:
			isPrimeNum = False
			factors.append(num)

	factors.append(aNum)
	return isPrimeNum, len(factors)

def writeToTextFileFunction(fileName, originalNum, factorCounts, isPrimeNum):
	fileObj = open(fileName, 'a')
	fileObj.write(str(originalNum) + " has " + str(factorCounts) + " factors \n") 
	if isPrimeNum == True:
		fileObj.write(str(originalNum) + " is a prime number \n\n") 
	else:
		fileObj.write(str(originalNum) + " is not a prime number \n\n")
	fileObj.close()



#Starts
os.remove("Output_03.txt")
retList = aReadFunction('numbers.txt')
print retList

for num in retList:
	isPrime, factorCounts = findPrimeNumNFactors(int(num))
	writeToTextFileFunction('Output_03.txt', num, factorCounts, isPrime)


'''
ret1, ret2 = findPrimeNumNFactors(24)
print ret1
print ret2

writeToTextFileFunction('Output_03.txt', 24, 8, False)
'''
