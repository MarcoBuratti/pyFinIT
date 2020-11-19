"""
#Import packages
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

#from Stock_Functions import * 
# CAPM W/ 4 STOCKS PORTFOLIO




#Import last 5 years data (add market portfolio S&P 500)
tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL', '^GSPC']
mydata2 = pd.DataFrame()
for t in tickers:
    mydata2[t]= wb.DataReader(t,data_source='yahoo', start='2015-11-1', end = "2020-10-31")['Adj Close']





#Calculate the log return of 4 stocks
sec_returns = np.log(mydata2 / mydata2.shift(1))
#print(sec_returns)




#Calculate the covariance matrix between portfolio and the Market
cov = sec_returns.cov()*250
#Take the first row ov covariance
cov_with_market = cov.iloc[0:1]


#Compute the annualized variance of the market S&P500
market_var = sec_returns["^GSPC"].var()*250
print(market_var)




#Calculate the beta of the portfolio
beta = cov_with_market / market_var
print(beta)


#This value is x > 1. This means that is an offensive portfolio




#Install and import package
from yahoofinancials import YahooFinancials




#Import the current yield for treasury US govt bonds (no %)
yahoo_financials = YahooFinancials('^TNX')
yr_10 = yahoo_financials.get_current_price() / 100




#Calculating the expected return of the portfolio (CAPM)
er = yr_10 + beta * 0.05
print("Expected Return:")
print(er)


#Calculate the sharpe ratio of the portfolio
Sharpe = (er - yr_10) / (sec_returns[["TSLA", "AAPL", "VGT", "ORCL"]].std() * 250**0.5 )
print(Sharpe)
"""