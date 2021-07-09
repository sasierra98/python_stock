import datetime as dt
import json
import requests
import pandas as pd
from pymongo import MongoClient
import ast
from pprint import pprint
import mplfinance as mpf

url = 'https://api.binance.com/api/v3/klines'
symbol = 'BTCUSDT'
interval = '1d'
# startTime = str(int(dt.datetime(2021, 7, 5).timestamp() * 1000))
# endTime = str(int(dt.datetime(2020, 2, 1).timestamp() * 1000))
limit = '1000'

# req_params = {'symbol': symbol, 'interval': interval, 'startTime': startTime, 'limit': limit}
req_params = {'symbol': symbol, 'interval': interval, 'limit': limit}

btcusdt_ = requests.get(url, params=req_params)

btcusdt = json.loads(btcusdt_.text)

print(btcusdt[0])

# client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
#
# db = client['Trading']
#
# collection = db['Crytomonedas']
#
# url = 'https://api.binance.com/api/v3/klines'
# symbol = 'BTCUSDT'
# interval = '1d'
# # startTime = str(int(dt.datetime(2021, 7, 5).timestamp() * 1000))
# # endTime = str(int(dt.datetime(2020, 2, 1).timestamp() * 1000))
# limit = '1000'
#
# # req_params = {'symbol': symbol, 'interval': interval, 'startTime': startTime, 'limit': limit}
# req_params = {'symbol': symbol, 'interval': interval, 'limit': limit}
#
# bb = json.loads(requests.get(url, params=req_params).text)
#
#
# btc = pd.DataFrame(json.loads(requests.get(url, params=req_params).text))
#
# btc = btc.iloc[:, 0:6]
#
# btc.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']
#
# openx = dict(btc['open'])
# openx['open'] = openx.pop(0)
# high = dict(btc['high'])
# high_str = str(high)
# high['high'] = high.pop(0)
# low = dict(btc['low'])
# low['low'] = low.pop(0)
# close = dict(btc['close'])
# close['close'] = close.pop(0)
# volume = dict(btc['volume'])
# volume['volume'] = volume.pop(0)
#
# btc.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in btc.datetime]
#
# # date = {"datetime": btc.index[0]}
# #
# # all_btc.update(date)
# # all_btc.update({'symbol': symbol})
# # pprint(all_btc)
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)
# pd.set_option('display.expand_frame_repr', False)
#
# #
#
# with open("D:\python_stock\price.txt", "w+", encoding="utf-8") as f:
#     f.write(str(btc))
#
#
#
# # daily = pd.read_csv('D:\python_stock\price.txt', index_col=0, parse_dates=True)
# # daily.index.name = 'Date'
# # daily.shape
# # daily.head(3)
# # daily.tail(3)
# #
# # mpf.plot(daily)
#
#
#
# # qgrid.show_grid(btc)f
#
#
# # btc['close'].astype('float').plot()
