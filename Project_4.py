

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

fileObj = open('Output_04.txt', 'w')

fileObj.write('Car is accelerating: \n')
carObject.accelerate()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')


carObject.accelerate()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.accelerate()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.accelerate()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.accelerate()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')


fileObj.write('Car is braking: \n')
carObject.brake()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.brake()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.brake()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.brake()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

carObject.brake()
curSpeed = carObject.get_speed()
fileObj.write('Current speed:' + str(curSpeed) + '\n')

fileObj.close()