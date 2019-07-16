

class Car:
	def __init__(self, yrModel, mk, spd=0):
		self.year_model = yrModel
		self.make = mk
		self.speed = spd

	def accelerate(self):
		self.speed += 5

	def brake(self):
		self.speed -= 5

	def get_speed(self):
		return self.speed


#Usage:
carObject = Car(2000, 'toyato')

print 'Car is accelerating: '
carObject.accelerate()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed


carObject.accelerate()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.accelerate()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.accelerate()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.accelerate()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed


print 'Car is braking: '
carObject.brake()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.brake()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.brake()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.brake()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed

carObject.brake()
curSpeed = carObject.get_speed()
print 'Current speed:', curSpeed
