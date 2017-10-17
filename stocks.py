import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2010, 10, 10)
end = dt.datetime(2017, 10, 16)

df = web.DataReader('MSFT', "yahoo", start, end)

#print(df.head())
df.to_csv("MSFT.csv")

df = pd.read_csv("MSFT.csv", parse_dates=True, index_col=0)
df[["High", "Low"]].plot()  #creates a graphical plot
plt.show() #shows that plot
