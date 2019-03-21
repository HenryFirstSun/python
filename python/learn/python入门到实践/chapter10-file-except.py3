# chapter10 读文件和异常
# 从文件读取数据
'''
with open('telephon.csv', 'rb', 'gbk') as file_object:
    contents = file_object.read()
    print(contents)
    contents = contents.decode('gbk')
    print(contents)
'''
import os
import io
import chardet
import sys

filename = 'telephon.csv'

bytes = min(32, os.path.getsize(filename))
raw = open(filename, 'rb').read(bytes)
result = chardet.detect(raw)
encoding = result['encoding']
print(encoding)
'''
infile = open(filename, 'r', encoding=encoding)
data = infile.read()
infile.close()
data = data.encode('gbk', 'ignore').decode('gbk')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print(data)

import csv
# 10.1.3.1逐行读取（csv.DictReader）
# 读取csv，按照orderedDict方式，很棒的类
with open(filename, 'r', encoding=encoding, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    for row in reader:
        print(row['序号'], row['证券代码'], row['证券简称'])
        print(row)
'''
'''
# 10.1.3.2逐行读取（csv.DictReader）,以shenzhen.csv 9万数据为例花费1.3s,
# 读取csv，按照orderedDict方式，很棒的类
import csv
filename = 'stock_analysis/shenzhen.csv'

bytes = min(32, os.path.getsize(filename))
raw = open(filename, 'rb').read(bytes)
result = chardet.detect(raw)
encoding = result['encoding']
print(encoding)
stock_infoes = []
with open(filename, 'r', encoding=encoding, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    for row in reader:
        if((len(row['证券代码']) == 6) and ('12/31') in row['报告期']) and ('--' not in row['净利润增长率%']):  # 去掉非法的数据，比如下一行的数据
            stock_infoes.append(row)

    for stock_info in stock_infoes[:1]:
        print(stock_info)

nums = []
rt1s = ['a', 'b']
rt2s = [{'a': 3, 'b': 4, 'c': 5}, {'a': 2, 'b': 2, 'c': 2}]
# 高手写的代码
result = [dict([(k, item[k]) for k in rt1s]) for item in rt2s]
# result = [(k, [x[k] for x in rt2]) for k in rt1]
print(result)

# 使用
stock_statistics = ['证券代码', '净利润增长率%']
results = [dict([(k, item[k]) for k in stock_statistics]) for item in stock_infoes[:2]]
print(results)

result1 = [{result['证券代码']:result['净利润增长率%']} for result in results]
print(result1)

result_sum = {}


def func(dict1, dict2):
    for i, j in dict2.items():
        if i in dict1.keys():
            dict1[i] = float(dict1[i]) + float(j)
        else:
            dict1.update({f'{i}': dict2[i]})
    return dict1


for dict2 in result1:
    func(result_sum, dict2)
print(result_sum)
'''
# 10.1.3.3使用padas读取shenzhen.csv 9万数据，分组聚类
# https://www.cnblogs.com/wkslearner/p/5930760.html 分组聚类
# pandas groupby 详解 https://blog.csdn.net/u011462357/article/details/78377411
# Python数据聚合和分组运算(1)-GroupBy Mechanics
# pandas使用例子
import pandas as pd
import numpy as np
import io
# df定义
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
print(df)
# 读csv文件
filename = 'stock_analysis/shenzhen.csv'
bytes = min(32, os.path.getsize(filename))
raw = open(filename, 'rb').read(bytes)
result = chardet.detect(raw)
encoding = result['encoding']
print(encoding)
stock_infoes = []
# with open(filename, 'r', encoding=encoding, newline='') as csvfile:


def file_reader(filename, encoding):
    with open(filename, 'r', encoding=encoding) as f:
        for line in f:
            if ('--' not in line and '上一页1下一页' not in line) or '证券代码' in line:
            #if ('12/31' in line and '--' not in line and '上一页1下一页' not in line ) or '证券代码' in line:
                yield line


data = io.StringIO(''.join(file_reader(filename, encoding)))
df = pd.read_csv(data, dtype={'证券代码': str})  # 得到年报告
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print(df['证券代码'])
# print(df['净利润增长率%'])
# 分组
df['报告期'] = pd.to_datetime(df['报告期']) #将数据类型转换为日期类型
df=df.loc[(df['报告期']> '2014/12/31')] 
print(df)
combine = df.groupby(['证券代码', '证券简称'])  # combin是df
# 使用pd.read_csv完成mysql stock查询.sql的#净利润增长率统计
# .sort_index(axis=1, ascending=False)对轴排序，轴是列名称排序
# print(combine.mean().sort_index(axis=1, ascending=False))
# pandas 之 to_csv 保存数据出现中文乱码问题及解决办法,https://blog.csdn.net/zhuzuwei/article/details/80890007
# combine.mean().sort_index(axis=1, ascending=False).to_csv('stock_analysis/增长率平均值.csv', header=True, encoding='utf_8_sig')
combine.mean().sort_index(axis=1, ascending=False).to_excel('stock_analysis/增长率平均值.xls')

# pandas 之 to_csv 保存数据出现中文乱码问题及解决办法,https://blog.csdn.net/zhuzuwei/article/details/80890007
# Sort by multiple columns
sort_increase = combine.mean().sort_values(by=['净利润增长率%', '营业收入增长率%'], ascending=False)
# loc多并列条件索引，根据条件选取数据loc[(sort_increase['净利润增长率%'] > 400) & (sort_increase['营业收入增长率%'] > 400)]

sort_increase.loc[(sort_increase['净利润增长率%'] > 50) & (sort_increase['营业收入增长率%'] > 10)].to_csv(
    'stock_analysis/增长率平均值100以上.csv', header=True, encoding='utf_8_sig')
filename1 = 'stock_analysis/增长率平均值100以上.csv'
with open(filename1, 'r', encoding=encoding) as f1:
    df1 = pd.read_csv(f1, dtype={'证券代码': str})  # 得到年报告
print(df1)
sort_increase_stockes = df1['证券代码'].tolist()
print(sort_increase_stockes)
df[df["证券代码"].isin(sort_increase_stockes)].to_csv('stock_analysis/增长率平均值100以上详细.csv', header=True, encoding='utf_8_sig')
# 使用to_excel要按照pip3.7 install xlwt
df[df["证券代码"].isin(sort_increase_stockes)].to_excel('stock_analysis/增长率平均值100以上详细.xls')
# sort_increase_stockes = sort_increase_stock['证券代码']
# print(sort_increase_stockes)
# print(combine.mean().to_json(orient='table'))
# 10.3 异常try except esle finally,多个except (ZeroDivisionError, FileNotFoundError)
try:
    5 / 0
except (ZeroDivisionError, FileNotFoundError):
    print('ZeroDivisionError')
else:
    print("don't run")
finally:
    pass
# 10.4 存储数据,JSON pandas.DataFrame.to_json按行转json https://blog.csdn.net/huanbia/article/details/72674832
import json
filename = 'stock_analysis/stock_analysis_net_profile.json'
'''
with open(filename, 'w', encoding='utf_8_sig') as file_obj:
    json.dump(combine.sum().to_json(orient='table'), file_obj)
with open(filename, 'r', encoding='utf_8_sig') as file_obj:
    df = pd.read_json(file_obj, orient='table')

print
'''
# to_json和read_json配对使用
with open(filename, 'w', encoding='utf_8_sig') as file_obj:
    combine.sum().to_json(file_obj, orient='table')
print(df)
with open(filename, 'r', encoding='utf_8_sig') as file_obj:
    df = pd.read_json(file_obj, orient='table')
df.to_csv('stock_analysis/stock_analysis_net_profile.csv', encoding='utf_8_sig')
'''
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])
print(df)
'''
