# Student Data
# Create a sample file using a text editor like notepad with the following data:
# joe 10 15 20 30 40
# bill 23 16 19 22
# sue 8 22 17 14 32 17 24 21 2 9 11 17
# grace 12 28 21 45 26 10
# john 14 32 25 16 89
# Using that text file write a program that prints out the names of students 
# that have more than six quiz scores.

fileObj = open('Student_data.data', 'r')
#print fileObj.readlines()

for line in fileObj:
	#print line
	subList = line.split()
	#print subList
	numOfElements = len(subList)
	if numOfElements > 6:
		print subList[0], ' has more than 6 quiz scores'



