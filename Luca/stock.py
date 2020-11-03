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
print('indexing by position: ', mydata.iloc[0])
trend = (mydata/mydata.iloc[0]*100)

#plot standardized trend
pl.plot(trend)
pl.ylabel('Stock price')
pl.show()
#trend.plot(figsize = (16,8))

#plot normal trend
mydata.plot(figsize=(16,8))

#calculate a portfolio RR
returns = (mydata/ mydata.shift(1)) -1
print('last returns value:', returns.tail())

#weights portfolio's stocks
weights = np.array([0.25,0.25,0.25,0.25])
annual_returns= returns.mean() *250
print('the annual stocks return: ', annual_returns)

print('annual return pf weighted ',np.dot(annual_returns,weights))
portfolio = str(round(np.dot(annual_returns, weights),5)*100)+'%'

print('portfolio return: ',portfolio)

#calculating single stocks risk
sec_returns= np.log(mydata/mydata.shift(1))
print('log pf return: ' , sec_returns)

sec_returns['TSLA'].mean() * 250
sec_returns['AAPL'].mean() * 250
sec_returns['VGT'].mean() * 250
sec_returns['ORCL'].mean() * 250

#annualize standard deviation(**0.5 stands for root square)
sec_returns['TSLA'].std()*250 **0.5
sec_returns['AAPL'].std()*250 **0.5
sec_returns['VGT'].std()*250 **0.5
sec_returns['ORCL'].std()*250 **0.5

#shows the tab
sec_returns[['TSLA','AAPL','VGT','ORCL']].mean() * 250

sec_returns[['TSLA','AAPL','VGT','ORCL']].std() * 250 **0.5

#calculating covariance and correlation between securities
#variance of the single assetS
TSLA_var_a= sec_returns['TSLA'].var() * 250 
print('TSLA var: ', TSLA_var_a)

AAPL_var_a= sec_returns['AAPL'].var() * 250 
print('AAPL var: ', AAPL_var_a)

VGT_var_a= sec_returns['VGT'].var() * 250 
print('VGT var: ', VGT_var_a)

ORCL_var_a= sec_returns['ORCL'].var() * 250 
print('ORCL var: ', ORCL_var_a)

#calculate covar matrix(annual)
cov_matrix_a=sec_returns.cov() * 250
print('pf cov matrix: ', cov_matrix_a)

#calculate corr matrix
corr_matrix= sec_returns.corr()
print('pf corr matrix: ', corr_matrix)



#calculating portfolio risk

weights = np.array([0.25,0.25,0.25,0.25])

#portfolio variance

#.T transposes the value in vector
portfolio_var = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) 
print('tot pf var: ', portfolio_var)

portfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
print('tot pf vol"sdv" :', portfolio_vol)

print('pf vol rounded: ', str(round(portfolio_vol, 5)*100) +'%')

# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

#diversifiable risk = port_var - weighted annual variances

dir_risk = portfolio_var - (weights[0]**2*TSLA_var_a) - (weights[1]**2*AAPL_var_a)- (weights[2]**2*VGT_var_a)- (weights[3]**2*ORCL_var_a)

print('pf diversificable risk: ', dir_risk)

print('pf rounded div risk: ', str(round(dir_risk*100,3))+'%')

non_dir_risk = portfolio_var - dir_risk

print('pf non div risk: ', non_dir_risk)

print('rounded pf non div risk: ', str(round(non_dir_risk*100,3))+'%')
