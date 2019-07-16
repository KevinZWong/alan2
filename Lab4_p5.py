
# Write a Python class named Circle constructed by a radius 
# and two methods which will compute the area and the 
# perimeter of a circle

# class definition
class circle:
	def __init__(self, radius):
		self.radius = radius

	def computeAreaOfCircle(self):
		areaOfArea = 3.14 * self.radius * self.radius
		return areaOfArea

	def computePerimeterOfCircle(self):
		perimeterOfCircle = 3.14 * 2 * self.radius
		return perimeterOfCircle


#Usage:
circleObj = circle(10)
print circleObj.computeAreaOfCircle()
print circleObj.computePerimeterOfCircle()
