#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
from scipy import stats
import seaborn as sns


# Create a list of tickers and weights
tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]= wb.DataReader(t,data_source='yahoo', start='2015-1-1')['Adj Close']
print(mydata)
const_weights = [0.25,0.25,0.25,0.25]


#Calculate stocks daily return
ret_data = mydata.pct_change()[1:]


#Calculate portfolio daily return
pf_ret = (ret_data * wts).sum(axis = 1)


print(ret_data)
print(pf_ret)


#Import SP500 data and calculate daily return
SP500_p = web.get_data_yahoo('^GSPC', start = '2015-01-01')
SP500_ret = SP500_p["Adj Close"].pct_change()[1:]


#Build a regression model: pf_return vs SP500_return
sns.regplot(SP500_ret,port_ret)
plt.xlabel("SP500_return")
plt.ylabel("Pf_return")
plt.show()


#Calculate alfa & beta of the portfolio
(beta, alpha) = stats.linregress(SP500_ret.values, pf_ret.values)[0:2]
print("Beta of the portfolio:", round(beta, 5))


from yahoofinancials import YahooFinancials
yahoo_financials = YahooFinancials('^TNX')
yr_10 = yahoo_financials.get_current_price()/100
mkt_risk_prem = 0.05


#Portfolio expected return
Pf_exp_ret = yr_10 + beta * mkt_risk_prem
print("PG Expected Return:", round(Pf_exp_ret, 5))
print()


#Calculate the sharpe ratio of the portfolio
Sharpe = (Pf_exp_ret - yr_10) / (pf_ret.std()*250**0.5)
print(Sharpe)
