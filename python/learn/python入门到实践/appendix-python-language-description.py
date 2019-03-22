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
# 14控制流
