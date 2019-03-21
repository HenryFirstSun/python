# 9类
# 9.1类定义鱼使用，self为函数的第一参数
# 长代码换行使用\


class Car():

    def __init__(self, make, model, yare, color, speed):
        self.make = make
        self.model = model
        self.yare = yare
        self.color = color
        self.speed = speed
        self.odometer_reading = 0  # 属性设定默认值，无需提供初始值形参

    def get_descriptive(self):
        long_descriptive = self.make + ' ' + self.model\
            + ' ' + self.color + ' ' + str(self.yare) + ' ' + str(self.speed)
        return long_descriptive

    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        pass


my_car = Car('Audi', 'a4', 5, 'red', 300)
print(my_car.get_descriptive())
# 9.2.3修改属性,属性直接修改，函数修改
my_car.odometer_reading = 23
my_car.update_odometer(23)
# 9.3继承class ElectricCar(Car):


class ElectricCar(Car):
    """docstring for ElectricCar"""

    def __init__(self, make, model, yare, color, speed, endurance):
        super().__init__(make, model, yare, color, speed)
        self.make = make
        self.model = model
        self.yare = yare
        self.color = color
        self.speed = speed
        self.endurance = endurance

    def update_endurance(self, miles):
        self.endurance = miles

    # 9.3.4重写父类方法get_descriptive(self)
    def get_descriptive(self):
        long_descriptive = self.make + ' ' + self.model\
            + ' ' + self.color + ' ' + str(self.yare) \
            + ' ' + str(self.speed) + ' ' + str(self.endurance)
        return long_descriptive


my_tesla = ElectricCar('tesla', 'model 3', 2016, 'red', 300, 1000)

print(my_tesla.get_descriptive())
print(my_tesla.endurance)


class Battery(object):
    """docstring for Battery"""

    def __init__(self, battery_size=70):
        super(Battery, self).__init__()
        self.battery_size = battery_size

    def describe_battery(self):
        print('this car has a ' + str(self.battery_size) + '-kwh battery')


class ElectricCar(Car):
    """docstring for ElectricCar"""

    def __init__(self, make, model, yare, color, speed, endurance):
        super().__init__(make, model, yare, color, speed)
        self.endurance = endurance
        # 9.3.5使用实例作为属性

        self.battery = Battery()

    def update_endurance(self, miles):
        self.endurance = miles

    # 9.3.4重写父类方法get_descriptive(self)
    def get_descriptive(self):
        long_descriptive = self.make + ' ' + self.model\
            + ' ' + self.color + ' ' + str(self.yare) \
            + ' ' + str(self.speed) + ' ' + str(self.endurance)
        return long_descriptive


my_tesla = ElectricCar('tesla', 'model 10', 2018, 'blue', 300, 1000)
print(my_tesla.get_descriptive())
print(my_tesla.endurance)
my_tesla.battery.describe_battery()
