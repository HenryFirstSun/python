# 10.布尔值：几乎所有内置python类型如何定义-_nonzero_魔术方法类都能解释为true,使用bool函数确认布尔值
print(bool([]))  # false
print(bool([1, 2, 3]))  # true
# 11 类型转换
s = '3.14159'
fval = float(s)
print(fval)  # 3.14159
print(type(fval))  # float
print(int(fval))  # 3
# 12 None是空值类型,是NoneType实例
a = 5
print(a is None)  # False
# 13日期和时间
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 51)
print(dt.day)
print(dt.second)
# 13.1时间格式化成字符串
print(dt.strftime('%m/%d/%y %H:%M'))  # 10/29/11 20:30

# 13.2 字符串格式化成时间参见10-2
print(datetime.strptime('20091031', '%Y%m%d'))
print(dt.replace(minute=0, hour=0, second=0))
# 13.3 两个datetime相减
print(dt)
dt2 = datetime(2011, 10, 29, 20, 30, 21)
delta = dt - dt2
print(delta)
print(dt2 + delta)
# 14控制流if elif else
# 15异常处理 try except :
# 16 range和xrange
# range 产生一组间隔平均的整数，python3和xrange一样返回产生整数的迭代器

# 三元表达式  可以将产生一个值 if-else块写到一行或一个表达式中
x = 5
value = 'Non-negative' if x >= 0 else 'Negative'
# 17数据结构
# 17.1元组,可以使用tuple将任意序列和迭代器转换元组
tuple([4, 2, 0])  # 结果（4,2,0）
tup = tuple('string')
print(tup)  # 任何序列('s', 't', 'r', 'i', 'n', 'g')
# 通过方括号访问
tup[0]  # 's'
# 17.1.1元组拆包，对元组型变量表达式赋值，对右侧的元组值拆包
a, b, c, d, e, f = tup
print(b)
# 嵌套元组也可以拆包
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print(d)  # 7
# 拆包用途，可以交换变量名
''' 例如
tmp=a
a=b
b=tmp
'''
b, a = a, b  # a,b变量名交换
# 变量拆包功能常用对元组或列表组成的序列进行迭代
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(a)
    print(b)
    print(c)
# 17.1.2元组方法
# count 计算指定值出现的次数
a = (1, 2, 2, 2, 2, 3, 4, 3)
print(a.count(2))
# 17.2 列表
b_list = ['hello', 'Python']
# 添加append 插入
b_list.insert(1, 'red')
print(b_list)

# pop移除
b_list.pop(1)
print(b_list)
# 按值删除元素，删除第一个符合要求的值
b_list.remove('hello')
print(b_list)
# in 是判断列表中是否含有某值,线性扫描，set 和dict是哈希扫描，要快的多
print('hello' in b_list)
# 17.2.1 合并列表+
b_list = [4, 'foo'] + [7, 8, (2, 3)]
print(b_list)
# 已经定义的列表使用append,insert,pop,remove,extend方法一次性添加多个元素
# extend要比+快
b_list.extend([10, 11, (12, 13)])
print(b_list)
# 17.2.2 排序sort，None不能排序,其中一个次要排序键，级产生用于排序的函数
b_list = [4] + [7, 8, 2, 3]
b_list.sort()
print(b_list)
b_list.sort(key=str)
print(b_list)
# 17.2 二分搜索及维护有序列表bisect模块，
import bisect
b = bisect.bisect(b_list, 5)  # bisect.bisect确定将新元素插到那个位置
bisect.insort(b_list, 5)  # 确实将元素插到那个位置上
print(b_list)
# page 428
# 17.3 切片[]

# 17.4 内置序列函数
# 17.4.1 enumerate对序列迭代时，跟踪当前项目的索引，返回序列的（i,value)元组
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for i, value in enumerate(b_list):
    print('第' + str(i) + '个值：' + str(value))
# 17.4.1.1求取一个将序列值（唯一的）映射到其所在位置的字典
mapping = dict((v, i) for i, v in enumerate(b_list))
print(mapping)
# 17.4.2 sorted 返回一个有序的列表,t和set联合使用，得到唯一元素组成的有序列表
b = sorted(b_list)

# 17.4.3 zip将多个序列的元素配对，得到元组数量最短序列
# 还有用法将行转列
pithers = [('n', 'z'), ('h', 'g')]
first, second = zip(*pithers)
print(first)
print(second)
# 17.4.4 reversed 逆序
b = reversed(b_list)
print(b)
# 17.5 字典 （page 431）
# 17.5 字典 （page 431）{，}
# 访问（以及插入、设置）元素和列表元组一样
# uptate字典之间合并
# 17.5.1从序列创建字典
mapping = {}
# 字典本质是一个二元元组，可以用dict类型函数处理
# 17.5.2 默认值 dict的get和pop接受可供返回的默认值
value = mapping.get(1)  # 找不到返回None
print(value)
# 例如根据首字母对一组单词进行分类，并最终产生一个列表组成的字典
words = ['apple', 'atom', 'bisect', 'class', 'diable']
by_letters = {}
for word in words:
    letter = word[0]
    if letter not in by_letters:
        by_letters[letter] = [word]
        print([word])
        print(word)
    else:
        by_letters[letter].append(word)
    pass
print(by_letters)

# 17.5.3 字典键的有效类型，（元组）
# 字典键是不可变对象，列表不能作为字典的键，列表是可变的。
# 17.6集合：唯一元素组成的无续集
# 17.6.1 创建方式 set 或{}的集合字面值
print(set([1, 2, 3, 2, 1, 4]))  # 结果：{1, 2, 3, 4}
print({1, 2, 3, 4, 3, 2, 1})  # 结果：{1, 2, 3, 4}
# 17.6.2 交，并，差运算
a = {1, 2, 3, 4}
b = {2, 3, 4, 5, 6}
# 并运算
print(a | b)  # {1, 2, 3, 4, 5, 6}
# 交运算
print(a & b)  # {1, 2, 3, 4}
# 差运算
print(a - b)  # {1}
print(b - a)  # {5, 6}
# 对称差
print(a ^ b)  # {1,5, 6}
print(b ^ a)  # {1,5, 6}
c = {1, 2, 3}
print(c.issubset(a))  # 包含子集 issubset
# 17.7 列表、集合以及字典推导式
# 用途是对一组数据过滤，定对得到的元素进行转换变形
# 格式[expr for var in collection if condition]
# 想当如下 expr=val*3
result = []
for val in b:
    if val > 3:
        result.append(val * 3)
print(result)
# 上述相当如下推导式
result = [val * 3 for val in b if val > 3]
print(result)
# 集合和字典推导式是该思想的一种自然延伸
# 格式 dict_comp={key-expr:value-expr for value in collectioin if condition}
# 集合格式 set_comp={expr for value in collention if condition}
# words=['apple', 'atom', 'bisect', 'class', 'diable']
# {}集合表示
unique_lengths = {len(x) for x in words}
print(words)
print(unique_lengths)
loc_mapping = {val: index * 2 for index, val in enumerate(words)}
print(loc_mapping)
loc_mapping1 = dict((val, idx) for idx, val in enumerate(words))
print(loc_mapping1)
# 17.8 嵌套列表推导式
all_data = [['tom', 'bill', 'jeffer', 'andrew'],
            ['susie', 'jill', 'ana', 'ada', 'eva']]
names_of_interest = []
for names in all_data:
    print(names)
    enough_es = [name for name in names if name.count('e') >= 1]
    print(enough_es)
    names_of_interest.extend(enough_es)
print(names_of_interest)
# 上述可以写成如下一个推导式,推导式for部分是按嵌套顺序排列的
# 可以记成嵌套for循环中个股for的顺序是怎样，嵌套推导式中各个for表达式顺序就是怎样的。
result = [name for names in all_data for name in names if name.count('e') >= 1]
print(result)
# 将一个由整数元组构成的列表'扁平化'为一个简单的整数列表
some_tuples = [(1, 2, 3), (4, 5), (6, 7, 8)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)
flattened = [[x for tup in some_tuples] for x in tup]
print(flattened)
# 17.8 函数
# 数据分析多使用函数


def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)


print(my_function(2, 3, 4))
# 17.9 命名空间、作用域，局部函数，函数被调用时创建的，局部命名空间实在被调用时创建的，函数参数会立即填入该命名空间，在函数执行完毕后局部命名空间会被销毁，
# 可以在任何地方声明函数


def outer_function(x, y, z):
    def inner_function(a, b, c):
        pass
    pass
# inner_function在outer_function被调用前是不存在的
# 17.9.1返回多个值


def f():
    a, b, c = 5, 4, 3
    return a, b, c
# 实际返回的元组，a,b,c=f()是拆包到各个结果变量中


a, b, c = f()
print(a + b + c)
print(f())
# 返回字典


def f():
    a, b, c = 5, 4, 3
    return {'a': a, 'b': b, 'c': c}


# 17.9.2函数也是对象
states = [' Alabama', 'Georgia!', 'angl*', 'south  carolina##', 'west virginia?']
import re


def remove_punctuation(value):
    return re.sub('[!#?*]', '', value)


clean_option = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


print(clean_strings(states, clean_option))
# 17.9.3 匿名(lambda)函数，简单函数，简单语句组成，结果是返回值，通过lambda定义


def equiv_annon(x): return x * 2  # x是参数
# 使用数据转换用函数作为参数，少输很多字，逻辑更清晰


def apply_to_list(some_list, f):
    return[f(x) for x in some_list]


ints = [4, 5, 6, 2, 1]
print(apply_to_list(ints, lambda x: x * 2))
print(list('param'))
print(len(set(list('param'))))
strings = ['foo', 'card', 'bar', 'ada', 'aaaaa', 'abab', 'hello']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)
# 17.9.4 闭包：返回函数的函数，很棒的方法
print('%.4f' % 1.756)
# 用途：编写带有大量选项的非常一般的函数，在组装更简单专门化的函数，比如创建一个字符串格式化函数


def format_and_pad(template, space):
    def formatter(x):
        return(template % x).rjust(space, '0')
    return formatter


fmt = format_and_pad('%.4f', 15)
a = fmt(1.756)
print(a)
# 证券代码前用零补足6位
fmt = format_and_pad('%s', 6)
a = fmt(233)
print(a)
# 17.9.5扩展用语法和*args,**kwares
# 17.9.6 柯里化：部分参数应用 从现有函数派生出新函数的技术


def add_numbers(x, y):
    return x + y


def add_five(y): return add_numbers(5, y)


print(add_five(6))
# 计算时间序列x的60日移动平均
# 17.9.7 生成器 函数中使用yield替换return，他可以以延迟的方式返回一个值序列，及返回一个值之后暂停，直到下一个值被请求时在继续


def squares(n=10):
    for i in range(1, n + 1):
        yield i**2


gen = squares()
for x in gen:
    print(x)
# 生成器表达式，把列表推导式[]改成（）
gen = (x**2 for x in range(1, 11))
for x in gen:
    print(x)
# 17.9.8 utertools模块 P459
# 常见的数据算法生成器
import itertools


def first_letter(x): return x[0]  # lambda first_letter= lambda x: x[0]


names = ['tom', 'bill', 'alan', 'ada' 'jeffer', 'andrew']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))
# 17.9.8.1 itertools.imap 等同于python map
# map详解： https://blog.csdn.net/xu_xiaoxu/article/details/83339856
'''根据提供的函数对指定序列映射，map()是 Python 内置的高阶函数，
它接收一个函数 f 和一个 list，
并通过把函数 f 依次作用在 list 的每个元素上，
得到一个新的 map 并返回,需使用list(map)返回list
'''
print(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
# 提供了两个列表，对相同位置的列表数据进行相加
print(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
# 17.9.8.2  itertools.ifilter 同python3 filter
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# http://www.runoob.com/python3/python3-func-filter.html
# 过滤出列表中的所有奇数：
tmplist = filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)
# 过滤出1~100中平方根是整数的数
# http://www.runoob.com/python3/python3-func-filter.html
import math
tmplist = filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101))
newlist = list(tmplist)
print(newlist)
# 过滤出列表中所有男生等
# 数据清洗时使用过滤器
# 17.9.8.3 itertools.combinations 和permutations
# 用于概率发现，火车购票 https://wenku.baidu.com/view/c4615c30cbaedd3383c4bb4cf7ec4afe05a1b16b.html
# 火车时刻表，每条线路，每辆火车的时间线路等，时间是否能够赶上换车过滤。自动化工作替换人参与
# combinations方法重点在组合,实现组合
test_data = ['a', 'a', 'a', 'b']
for i in itertools.combinations(test_data, 2):
    print(i)
# 组合更清晰的是a,b,c
test_data = 'efg'
for i in itertools.combinations(test_data, 2):
    print(i)
# permutations方法重在排列
# https://blog.csdn.net/specter11235/article/details/71189486
test_data = 'opq'
for i in itertools.permutations(test_data, 3):
    print(i)
#17.10文件读写，参照chapter10