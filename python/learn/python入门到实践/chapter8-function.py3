#9类
#9.1类定义鱼使用，self为函数的第一参数
class Car():
	"""docstring for car"""
	def __init__(self, make,model,yare,color,speed):
		super(car, self).__init__()
		self.make = make
		self.model = model
		self.yare = yare
		self.color = color
		self.speed = speed
	def get_descriptive(self):
		long_descriptive=self.make+''+self.model+''
		+self.color+''+char(self.yare)+''+char(self.speed)
		return long_descriptive
my_car=Car('Audi','a4',5,'red',300)
print(my_car.get_descriptive())

		