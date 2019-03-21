#8.函数
#8.1 def定义函数，参数
def greet_user(username):
	#显示问候语
	print('hello '+username)
#调用
greet_user('tom')
#8.2传参
#8.2.1位置参数：基于实参的顺序
def describe_pet(animal_type,pet_name='harry'):
	print('\n\r '+animal_type+' '+pet_name)
#describe_pet('hamster','harry') ,按照形参顺序填参数
#8.2.2关键字实参关键字和值对应输入animal_type='dog',实参顺序不固定
describe_pet(animal_type='dog',pet_name='harry')

#8.2.3默认值 def函数形参填写默认值,默认值形参放在后面，可不填
#def describe_pet(animal_type='dog',pet_name):
#8.3返回值 return
def get_formatted_name(first_name,last_name):
	full_name=first_name+' '+last_name
	return full_name
print(get_formatted_name('Henry','Sun'))
#8.3.2让实参变为可选的，使用形参默认值可使实参变成可选的
describe_pet('cat')
#8.3.3返回字典,键first_name储存first_name变量
def build_parson(first_name,last_name):
	person={'first_name':first_name,'last_name':last_name}
	return person
musician=build_parson('jimi','smith')
print(musician)
#8.3.4使用函数和while
#8.4传递列表，列表包含字符串、数字、字典
users_list={
	'login':{'name':'Henry','sex':'man','phone':'1234546'},
	'moon':{'name':'tom','sex':'man','phone':'1234546'}
}
def print_users_list(users_list): #传递列表
	for username,user_infoes in users_list.items():
		print('\nusername is '+username)
		for user_info in user_infoes.values():
			print(user_info)
print_users_list(users_list)
#8.4.2使用切片传递副本，以保持原列表不变list[:]
#8.5传递任意数量参数使用元组 a(:) ,使用*a输入任意个参数
#先定义实参，最后任意参数的元组
#**user_info建立空字典
def build_profile(first_name,last_name,**user_info):
	profile={}
	profile['first_name']=first_name
	profile['last_name']=last_name
	for key,value in user_info.items():
		profile[key]=value
	return profile
user_profile=build_profile('albert','smith',
	location='princeton',field='physics')
print(user_profile)
#8.6将函数存储在模块中
#8.6.1 导入模块import
#pizza.py为模块
#import pizza #导入模块
#pizza.make_pizza()调用模块的函数
#8.6.2导入特定函数 import
#from module_name import function0,function1..
#使用as给函数指定别名
#from pizza import make_pizza as mp
#mp(16,'pepperoni')
#模块指定别名as 
#import pizza as p
#使用*导入所有函数
#8.7函数编写：名称小写