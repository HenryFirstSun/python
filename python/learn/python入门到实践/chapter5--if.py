#5.if语句
#格式 if else 条件表达式：
#大写bmw，其他第一个字母大写
cars=['audi','bmw','bens']
for car in cars:
	if car =='bmw':
		print(car.upper())
	else:
		print(car.title())
print('audi' in cars)
#5.3.3If :elif:else:

#5.4.2确认列表不是空的
if cars:
	print(cars)
#5.4.3使用多个列表判断是否包含
cars1=['audi','bmw','bens','honda']
if cars1 in cars:
	print(cars1)
else:
	print(cars)