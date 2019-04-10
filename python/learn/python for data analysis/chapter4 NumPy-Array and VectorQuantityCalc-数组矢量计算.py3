# https://baike.baidu.com/item/%E7%9F%A2%E9%87%8F/12795520
'''用于物理计算、数学计算或者其他的作图计算'''
# NumPy是高性能科学计算和数据分析基础包
# 4.1 ndarray 多维数组对象，是一个快速灵活的大数据集容器
data = [[0.923, -0.888, -0.221], [0.523, 0.789, 0.0034]]
print(data)
# print(data * 2)
import numpy as np
data1 = [0.923, -0.888, -0.221, 5]
arr1 = np.array(data)  # 创建二维数组
print(arr1)
print(arr1.shape)  # arr1.shape表示各维度大小的元组
print(arr1.dtype)  # arr1.dtype 表示数据类型
data2 = [[0.923, -0.888, -0.221], [0.523, 0.789, 0.0034], [0.123, 0.189, 0.1034]]
arr1 = np.array(data2)  # 创建二维数组
print(arr1)
print(arr1.shape)  # arr1.shape表示各维度大小的元组
print(arr1.dtype)  # arr1.dtype 表示数据类型
# 4.1.1 zeros 创建指定长度的或形状是0或1的元组
print(np.zeros(10))
print(np.ones(10))
a = np.zeros(5)
print(np.zeros((10, 3)))
print(np.arange(10))
print(np.eye(10))  # 创建N*N矩阵，对角线为1，其余为0

# 4.1.2 ndarray的数据类型
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

arr2 = np.array([1, 2, 3], dtype=np.int64)  # np.float64
print(arr2)
arr21 = np.array(['object', 'numpy', '中文'], dtype=np.unicode)
print(arr21)
# 数据类型显示转换
arr23 = arr2.astype(np.int32)  # 生成一个新数组，原数组一份拷贝需要使用下面方法
print(arr23.dtype)
arr22 = np.array(arr2, dtype=np.float64)
print(arr22)
# 4.2 数组和标量之间的运算
# 不用编写循环对数据执行批量运算，通常叫矢量化（vectorization）
# 大小相等数组之间运算，都会应用到元素级
arr2 = np.array([1, 2, 3])
print(arr2 * arr2)
print(arr2 - arr2)
print(arr2 ** 2)
print(arr2 ** 0.5)
# 4.3 基本的索引和切片
# 一维数组跟python同
arr3 = np.arange(10)
print(arr3[4])
print(arr3[4: 9])
# 数组切片和列表区别：数组切片是原始数组的视图，视图上任何修改都会反映在原数组上
arr_slice = arr3[5:8]
arr_slice[1] = 123
arr3[4:7] = 0  # 切片赋值，广播到所有切片，此为了提高大数据处理性能和内存
print(arr3)
# 如要复制，需使用copy
arr31 = arr3[4:7].copy()
print(arr31)
# 二维数组，各索引位置上的元素不再是标量而是一维数组
arr32d = np.array([[0.923, -0.888, -0.221], [0.523, 0.789, 0.0034], [0.123, 0.189, 0.1034]])
print(arr32d[2])  # [0.123  0.189  0.1034]
# 选取单个元素[0][2] 或[0,2]
print(arr32d[1, 0])
# 多维数组中省略后面索引，则返回对象是一个低一点维度的数据
arr3d = np.array([[[0.923, -0.888, -0.221], [0.523, 0.789, 0.0034], [0.123, 0.189, 0.1034]],
                  [[0.823, -0.988, -0.221], [0.823, 0.789, 0.0034], [0.123, 0.189, 0.1034]]])
print(arr3d)
print(arr3d[0])
print(arr3d[0, 0])
print(arr3d[0, 0, 0])
old_values = arr3d[0, 0].copy()  # 取副本一定使用copy()
print(old_values)
arr3d[0, 0] = 0.001
print(arr3d)

arr3d[0, 0] = old_values
print(arr3d)
# 4.3.1切片索引
# ndarray的切片跟python列表一维对象差不多
print(arr3[4:8])
print(arr32d)
# 高维数组可以在一个或多个轴上进行切片
# 沿着第一个轴切片
print(arr32d[:1])
# 沿着第一二个轴切片,轴之间用逗号分隔，相同维数的数组
print(arr32d[:2, 2:])
# 通过整数索引和切片混合，可以得到低维度的切片
print(arr32d)
print(arr32d[1, 1:])
print(arr32d[0, 1:])
print(arr3d)
print(arr3d[0, 0, :2])
print(arr3d[1, 2, :2])
# 4.3.2 布尔型索引
names = np.array(['bob', 'joe', 'bob', 'will', 'joe', 'tom', 'ada'])
data = np.random.randn(7, 4)
print(names)
print(data)
print(names == 'bob')
print(data[names == 'bob'])
print(data[names == 'bob', 2:])
# 选择除bob以外的其他值(!= 或-)
print(data[names != 'bob'])
# 选取组合应用多个布尔值 & |
mask = (names == 'bob') | (names == 'ada')
print(mask)
# 通过布尔型数组设置是常用的手段，将data中的所有负值设为0
data[data < 0] = 0
print(data)
# 通过一维数组布尔值设置整行列值
data[names == 'joe'] = 7
print(data)
# 4.3.3花式索引：利用整数数组进行索引
arr433 = np.empty([8, 4])
print(arr433)
for i in range(8):
    arr433[i] = i
print(arr433)
# 特定顺序选取子集,传入指定顺序列表或ndarray,负数索引从末尾取
print(arr433[[4, 3, 2, 1]])
# 传入多个索引，会转换对应的元组索引，再通过索引取对应的元素
arr433n = np.arange(40).reshape((8, 5))
print(arr433n)
print(arr433n[[4, 3, 2, 1], [4, 3, 2, 1]])  # 对应的索引元组是(4,4)
# 选取子集需要使用：[[4, 3, 2, 1]][:, [4, 3, 2, 1]]
print(arr433n[[4, 3, 2, 1]][:, [4, 3, 2, 1]])
# 花式索引与切片不同，他复制数据到新数组
# 使用ix函数
print(arr433n[np.ix_([4, 3, 2, 1], [4, 3, 2, 1])])
# 4.4 数组转置和轴对换 p107
# 转置(transpose)是重塑，返回原数据视图，有transpose方法，特殊的T属性
arr44 = np.arange(15).reshape((3, 5))
print(arr44)
print(arr44.T)
print(arr44)
# 计算矩阵內积,不知道怎么用
print(np.dot(arr44.T, arr44))
# 高维数组，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
arr441 = np.arange(16).reshape((2, 2, 4))
print(arr441)
print(arr441.transpose())
'''转置特例'''
arr442 = np.arange(4).reshape((2, 2))
# 参考文章https://blog.csdn.net/u012762410/article/details/78912667
print(arr442)  # 第一个[]是0轴，第二个[]是1轴
print(arr442.T)  # 等同arr442.transpose((1,0)) 交换0轴和1轴
# 三维
print('三维')
arr443 = np.arange(16).reshape((2, 2, 4))
print(arr441)
# 下面好理解
print('保持不变')
arr443.transpose((0, 1, 2))
print('0轴1轴交换')
print(arr443.transpose((1, 0, 2)))
print('1轴2轴交换')
print(arr443.transpose((0, 2, 1)))
print('0轴2轴交换')
print(arr443.transpose((2, 1, 0)))
print('0轴1轴2轴交换')
print(arr443.transpose((2, 0, 1)))
# 4.5 通用函数：快速的元素级数组函数
# 是对ndarray中数据执行元素级运算的函数，即接受一个或多个值，产生一个或多个值
# 比如sqrt,exp
arr45 = np.arange(10)
print('平方根sqrt,一元接受一个数组')
print(arr45)
print(np.sqrt(arr45))
arr45 = np.arange(10)
print('最大值maximum,2元接受2个数组')
arr45x = np.random.randn(8)
print(arr45x)
arr45y = np.random.randn(8)
print(arr45y)
print(np.maximum(arr45x, arr45y))
print(np.add(arr45x, arr45y))
print('最大值maximum,2元接受2个数组')
#4.6利用数组进行数据处理