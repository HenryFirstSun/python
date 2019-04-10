import tushare as ts
# print(tushare.__version__)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#df = ts.get_tick_data('601633', date='2019-04-08', src='tt')
df = ts.get_realtime_quotes('601633')  # Single stock symbol

df.head(10)
print(df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']])
