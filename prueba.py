import mplfinance
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web

start = dt.datetime(2020, 12, 1)
end = dt.datetime(2020, 12, 31)

a = web.get_data_fred('GS10')

print(a)
