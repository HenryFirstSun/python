
#coding=utf-8
'''
print("hello world")
message="hello world's human"
'''
#print(message)
bicyles=['honda','sukai','byd']
bicyles.sort()
print(bicyles)
#方向排序
bicyles.sort(reverse=True)
print(bicyles)
#倒序永久改变lieb
bicyles.reverse()
print(bicyles)
len=len(bicyles)
for bicyle in bicyles:
	print(bicyle)
	print('This is'+ bicyle)
print('Those are all bicyles.')
for x in range(1,10):
	print(x)
members=list(range(1,11))
print(members)
members=list(range(1,11,3))
print(members)
#4.3.2创建任何数据集
squares=[]
for value in range(1,11):
	square=value**3
	squares.append(square)
print(squares)
#4.3.3统计计算 min,max,sum
print(min(squares))
print(max(squares))
print(sum(squares))
#4.3.4列表解析 列表名=[表达式 for var in range(1,n,[step])]
squares=[square**2 for square in range(1,11)]
print(squares)
#输出一个有1百万平方列表
squares=[square**2 for square in range(1,1000001)]
#print(squares)
#使用列表一部分称作切片
print(squares[999:2000])
#省略999是从头开始，省略2000是到末尾，-1代表末尾
#显示后三位
print(squares[-3:])
#4.4.2使用切片遍历
for square in (squares[-3:]):
	print(square)
#4.4.3使用切片复制列表
squares1=squares[-5:] #如果使用squares1=squares只是使变量指向同一列表，不是复制
squares1.append(88888)
print(squares[-5:])
print(squares1)
#4.5元组创建时（）不是[],元组不能修改
dimensions=(200,50)
print(dimensions)
#4.5.3通过重新赋值修改元组的变量
dimensions=(400,50)
print(dimensions)