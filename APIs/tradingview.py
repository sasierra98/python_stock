import pandas as pd
from tvDatafeed import TvDatafeed,Interval
import mplfinance as mpf
from bokeh.plotting import figure, show

username = 'sa_sierra@hotmail.com'
password = 'joseandres24'

tv = TvDatafeed(username, password, chromedriver_path=None)

# nifty_data = tv.get_hist(symbol='ADAUSDT', exchange='BINANCE', interval=Interval.in_daily, n_bars=5000)
ecopetrol = tv.get_hist(symbol='AAPL', exchange='NASDAQ', interval=Interval.in_daily, n_bars=5000)

#print(nifty_data)

print(ecopetrol)

mpf.plot(ecopetrol, type = 'candle', style = 'yahoo', volume=True)




