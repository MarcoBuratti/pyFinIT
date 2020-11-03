#packages for finance and data science
#helping work with multidimensional arrays
import numpy

#organize data in tabular form and to attach descriptive labels
import pandas

# 2D plotting library
import matplotlib

#contains math modules
import math

#contains stats models
import statsmodels
import pandas_datareader

#all the arrays must be the same number of elements datatype(float/str)
import numpy as np
from pandas_datareader import data as wb

PG = wb.DataReader('PG', data_source='yahoo', start= '1995-1-1')
print(PG)

AAPL = wb.DataReader('AAPL', data_source='yahoo', start= '2010-1-1')
print(AAPL)
wb.DataReader('FCA', data_source='yahoo', start= '2010-1-1')

PG.info()

#how many entries and the time span
#calculate the rate of return(for multiple stocks overtime)
#E[x]=(earning price+ dividend return - beginning price)/beginning price

import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.DataReader('PG', data_source='yahoo',start='1995-1-1')

print(PG)

#adj close as a reference to calculate SRR
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) -1

#shift gives me the n. of lags(previous number)
print(PG['simple_return'])
PG['simple_return'].plot(figsize=(8, 5))
plt.show()

#daily returns observed duting the period

#calculate the mean daily return on period
avg_return_d = PG['simple_return'].mean()
print(avg_return_d)

#annual return on period
avg_returns_a = PG['simple_return'].mean()*250
avg_returns_a

#250 = trading days annual
str(round(avg_returns_a, 4)*100) + '%'

#round at the 4th cifre - *100 gives an entire number - % to add the simbol

#logaritms return(calcularion about a single asset overtime)

#Log(116/110) = log116$-Log110$
PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(PG['log_return'])

PG['log_return'].plot(figsize=(8,5))
plt.show()
log_return_d = PG['log_return'].mean()
print(log_return_d)
log_return_a = PG['log_return'].mean() *250
print(log_return_a)
str(round(log_return_a, 4)*100) + '%'

#Annual return = [(daily ret +1)^365]*100-1
#calculate the RR of a portfolio
tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]= wb.DataReader(t,data_source='yahoo', start='2010-1-1')['Adj Close']

print(mydata)

#normalization to 100
mydata.iloc[0]
import matplotlib.pyplot as plt

trend = (mydata/mydata.iloc[0]*100)
print(trend)

trend.plot(figsize = (16,8))
mydata.plot(figsize=(16,8))

#calculate a portfolio RR
returns = (mydata/ mydata.shift(1)) -1
print(returns.tail())

#weights portfolio's stocks
weights = np.array([0.25,0.25,0.25,0.25])

#allows to calculate vectors multiplying stocks times weights
np.dot(returns,weights)

#to have the entire return we need to calculate the average return of PF
annual_returns= returns.mean() *250
annual_returns
np.dot(annual_returns,weights)

portfolio = str(round(np.dot(annual_returns, weights),5)*100)+'%'

print(portfolio)