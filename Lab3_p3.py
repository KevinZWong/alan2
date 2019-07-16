#City Names:
#Write a function called city_country() that takes in the name of a city and its country.
#The function should return a string formatted like this: London, England
#Call your function with at least three city-country pairs, and print the value that returned.

# function definition
def city_country(city, country):
	#print '', city, country
	retValue = city + ', ' + country
	return retValue


# function usage:
returnValue = city_country('London', 'England')
print returnValue

