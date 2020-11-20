#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as wb
from scipy import stats
import seaborn as sns
from yahoofinancials import YahooFinancials


# Create a list of tickers and weights
tickers = ['ACN', 'IBM', 'AIG', 'BLK','C','TRI','VGT','QQQJ','MA']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]= wb.DataReader(t,data_source='yahoo', start='2019-1-1')['Adj Close']
    
const_weights = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]


#Calculate stocks daily return
# DA TENERE
def dailyPercReturn(mydata):
    ret_data = mydata.pct_change()[1:]
    return (ret_data * const_weights).sum(axis = 1)

#Calculate portfolio daily return
pf_ret = dailyPercReturn(mydata)


#Import SP500 data and calculate daily return
def benchmark():
    return wb.get_data_yahoo('^GSPC', start = '2015-01-01')["Adj Close"].pct_change()[1:]

SP500_ret = benchmark()


#Build a regression model: pf_return vs SP500_return
def capm(SP500_ret, pf_ret):
    sns.regplot(SP500_ret, pf_ret)
    plt.xlabel("SP500_return")
    plt.ylabel("Pf_return")
    plt.savefig('../img/capm.png')
    return stats.linregress(SP500_ret.values, pf_ret.values)[0:2]

beta, alpha = capm(SP500_ret, pf_ret)

# Import ten yield bonds
yahoo_financials = YahooFinancials('^TNX')
yr_10 = yahoo_financials.get_current_price()/100

#Portfolio expected return
def expectedReturn(yr_10, beta):
    mkt_risk_prem = 0.05
    Pf_exp_ret = yr_10 + beta * mkt_risk_prem
    #print("PG Expected Return:", round(Pf_exp_ret, 5))
    Sharpe = (Pf_exp_ret - yr_10) / (pf_ret.std()*250**0.5)
    #print(Sharpe)
    #portfolio expected return, sharpe = indice del portafoglio
    return Pf_exp_ret, Sharpe


Pf_exp_ret, Sharpe = expectedReturn(yr_10, beta)