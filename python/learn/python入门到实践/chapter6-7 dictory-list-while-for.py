#6.3遍历字典
#取字典的key和value
users={'name':'Henry','sex':'man','phone':'1234546'}
for k,v in users.items():
	print(k+" "+v)
#遍历所有键
for k in users.keys():
	print(k.title())
#遍历所有值
for v in users.values():
	print(v.title())
#判断是否存在字典里
if 'Henry' in users.values():
	print("Henry is good man.")
#6.3.3按顺序遍历字典中的所有值
for v in sorted(users.values()):
	print(v)
#6.4嵌套列表嵌套字典，字典嵌套列表，字典嵌套字典
#创建n个字典的列表
aliens=[]
#创建外星人
for x in range(1,31):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[:5]:
	print(alien)
print('.....')
print('列表字典解析式')
aliens=[{'color':'yellow','points':9,'speed':'slow'} for x in range(30)]
for alien in aliens[:5]:
	print(alien)
#全部遍历切片，修改alien
for alien in aliens[:-1]:
	if alien['color']=='yellow':
		alien['color']='red'
	else:
	 alien['color']='blue'
for alien in aliens[:-1]:
	print(alien)
#6.4.2在字典中储存列表，例如披萨饼不同属性的描述、多种配料，使用java好像有点费劲
pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],
}
print('You ordered a '+pizza['crust'])
print(pizza['toppings'])
for topping in pizza['toppings']:
	print(topping)
#喜欢多种语言
favorite_languages={
	'jen':['java','c'],
	'tom':['python','javascript'],
	'Henry':['c#','java']
}
for name,languages in favorite_languages.items():
	print('\n'+name.title()+"'s favorite languages are")
	for language in languages:
		print("\t "+language.upper())
#6.4.3字典中存储字典
users_list={
	'login':{'name':'Henry','sex':'man','phone':'1234546'},
	'moon':{'name':'tom','sex':'man','phone':'1234546'}
}
for username,user_infoes in users_list.items():
	print('\nusername is '+username)
	for user_info in user_infoes.values():
		print(user_info)

#7用户输入和while循环
#7.1 input
message=input('Tell me something, I will repeat it back to you\r\n')
print(message)
#使用int(message)将字符串转换数字
#模运算%
#7.2 while
current_number=1
while current_number<=6:
	print(current_number)
	current_number+=1
#7.2使用while选择退出输入
while current_number != 10:
	current_number=int(input('please input number: '))
	print(current_number)
#7.2.3标志，标志发生变化是指示程序执行特定代码，比如退出程序
active=True
while active:
	current_number=int(input('please input number: '))
	if current_number== 10:
		active=False

#7.2.4 break立即退出循环，不在执行下面代码
#7.2.5 continue 返回到循环开头while

#7.3使用while循环处理列表和字典
#for 和while都能遍历列表和字典，for一般只做查询，while可以修改
#7.3.1在列表之间移动元素
unconfirmed_users=['alien','Henry','tom']
confirm_users=[]
while unconfirmed_users: #while直到unconfirmed_users为空
	current_user=unconfirmed_users.pop() #pop()从末尾弹出
	print(current_user)
	confirm_users.append(current_user)
	
print(confirm_users)
''' confirm_users不为空，死循环
while confirm_users:
	print(confirm_users)
'''
#7.3.2删除特定值confirm_users. remove('tom')
#7.3.3使用用户输入填充字典
reponses={}
polling_active=True
while  polling_active:
	name=input('\nWhat is you name: ')
	reponse=input('Which mountain would you like to climb: ')
	reponses[name]=reponse
	repeat=input('would you like to let anthor person respond?')
	if  repeat=='no':
		polling_active=False
print('\n poll result')
for name,reponse in reponses.items():
	print(name+" would like to climb  "+reponse+".")
	


