import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt


Ticker = "BTC"
currency = "USD"

start = dt.datetime(2021,1,1)
end = dt.datetime.now()

data = web.DataReader(f"{Ticker}-{currency}","yahoo",start,end)

mpf.plot(data, type="candle", volume=True,style="yahoo")
