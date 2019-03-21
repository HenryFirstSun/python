import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import sys
import io
filename = 'stock_analysis/xhc.csv'
with open(filename, 'r', encoding='UTF-8-SIG') as f:
    df = pd.read_csv(f)  # 得到年报告
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print(df)
# df = pd.DataFrame(np.random.randn(4,4),index = list('ABCD'),columns=list('OPKL'))
#print(df)
df.plot('报告期','净利润增长率%',kind='line',title='xhc')
plt.show()