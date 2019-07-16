# print('hello world!')

input_test = raw_input('Enter somethings eaten in last 24 hours: ')
print(input_test)
input_test = input_test.lower()
print(input_test)

#if (-1 != input_test.find('dairy')):
if 'dairy' in input_test:
	print('It is True that "seafood, dairy, nuts, and chocolate cake" conatains "dairy"')
#elif (-1 != input_test.find('nuts')):
elif 'nuts' in input_test: 
	print('It is True that "seafood, dairy, nuts, and chocolate cake" conatains "nuts"')
#elif (-1 != input_test.find('seafood')):	
elif 'seafood' in input_test:
	print('It is True that "seafood, dairy, nuts, and chocolate cake" conatains "seafood"')
#elif (-1 != input_test.find('chocolate cake')):	
elif 'chocolate cake' in input_test:	
	print('It is True that "seafood, dairy, nuts, and chocolate cake" conatains "chocolate cake"')
else:
	print('It is Not True that "seafood, dairy, nuts, and chocolate cake" contains: ', input_test)