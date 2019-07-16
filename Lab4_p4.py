# Write a Python class named Rectangle constructed 
# by a length and width and a method which will compute 
# the area of a rectangle

# class definition
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def computeAreaOfRectangle(self):
		areaOfRectangle = self.length * self.width
		return areaOfRectangle


#Usage
RectangleObject = Rectangle(10, 5)

print RectangleObject.computeAreaOfRectangle()
