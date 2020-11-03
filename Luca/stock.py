from pandas_datareader import data as wb
import pandas as pd
from matplotlib import pyplot as pl
import numpy as np

tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]= wb.DataReader(t,data_source='yahoo', start='2010-1-1')['Adj Close']
print(mydata)

#ordinary check
print(mydata.info())
print(mydata.head())
print(mydata.tail())

#normalization to 100
print(mydata.iloc[0])
trend = (mydata/mydata.iloc[0]*100)

#plot standardized trend
trend.plot(figsize = (16,8))

#plot normal trend
mydata.plot(figsize=(16,8))

#calculate a portfolio RR
returns = (mydata/ mydata.shift(1)) -1
print(returns.tail())

#weights portfolio's stocks
weights = np.array([0.25,0.25,0.25,0.25])
annual_returns= returns.mean() *250
print(annual_returns)

print(np.dot(annual_returns,weights))
portfolio = str(round(np.dot(annual_returns, weights),5)*100)+'%'

print(portfolio)