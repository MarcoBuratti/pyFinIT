from pandas_datareader import data as wb
import pandas as pd
#from matplotlib import pyplot as pl
import numpy as np

from Stock_Functions import pf_return, weigthedReturn, portfolio, pfRisk, pfCov, returns, pfCorr

# Selezione dei ticker da mettere su file JSON
tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL']
mydata = portfolio(tickers)

#ordinary check
#print(mydata.info())
#print(mydata.head())
#print(mydata.tail())

#normalization to 100
#print('indexing by position: ', mydata.iloc[0])
#trend = (mydata/mydata.iloc[0]*100)

#plot standardized trend
#pl.plot(trend)
#pl.ylabel('Standardize Stock Price')
#pl.show()
#trend.plot(figsize = (16,8))

# Plot normal trend
#def recap(mydata):
    #mydata.plot(figsize=(16,8))
    #pl.plot(mydata)
    #pl.ylabel('Stock Price')
    #pl.savefig('../img/recap.png')


# Pesi delle singole azioni, ritorno annuale, ritorno annuale pesato e volatilità
weights = np.array([0.25,0.25,0.25,0.25])
annual_returns = pf_return(mydata)
annualReturnW = weigthedReturn(annual_returns, weights)
volatility = pfRisk(annual_returns, tickers)

#print(pfCov(annual_returns,tickers))

pfCovMatrix = pfCov(mydata)

pfCorrMatrix = pfCorr(mydata)
 
'''



#.T transposes the value in vector
portfolio_var = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) 
#print('tot pf var: ', portfolio_var)

portfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
#print('tot pf vol"sdv" :', portfolio_vol)

#print('pf vol rounded: ', str(round(portfolio_vol, 5)*100) +'%')

# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

#diversifiable risk = port_var - weighted annual variances

dir_risk = portfolio_var - (weights[0]**2*TSLA_var_a) - (weights[1]**2*AAPL_var_a)- (weights[2]**2*VGT_var_a)- (weights[3]**2*ORCL_var_a)

#print('pf diversificable risk: ', dir_risk)

#print('pf rounded div risk: ', str(round(dir_risk*100,3))+'%')

non_dir_risk = portfolio_var - dir_risk

#print('pf non div risk: ', non_dir_risk)

#print('rounded pf non div risk: ', str(round(non_dir_risk*100,3))+'%')





#Markowitz Portfolio Optimization

assets = ['TSLA', 'AAPL', 'VGT', 'ORCL']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a]= wb.DataReader(a, data_source='yahoo', start='2010-1-1')['Adj Close']



#calculating general features-> mean, var, corr
log_returns = np.log(pf_data / pf_data.shift(1))

log_returns.mean() *250

log_returns.cov() *250

log_returns.corr()

#counting the number of assets in pf
num_assets = len(assets)

#print('number of assets in pf', num_assets)

#generate random pf weights
#sum of these random number must be equal to 1(sum of pf assets)
#in other words (w1/(w1+w2)+(w2/(w1+w2)

weights_m = np.random.random(num_assets)
weights_m /= np.sum(weights_m)
#print('random generated pf weights', weights_m)

#expected portfolio return
np.sum(weights_m*log_returns.mean()) *250

#expected portfolio variance
np.dot(weights_m.T,np.dot(log_returns.cov() *250, weights_m))

#print('rounded var',str(round(np.dot(weights_m.T,np.dot(log_returns.cov() *250, weights_m))*100))+'%')

#expected portfolio volatility

#print('rounded pd volat',str(round(np.sqrt(np.dot(weights_m.T,np.dot(log_returns.cov() *250, weights_m)))*100)) +'%')

#simulating 1000 portfolio combination with the assets taken into account
#create an empty list and fill it up with randomical pf generation

#generate two rdm weights 
#append add the new random generate pf to the list pf 

pf_returns= []
pf_vol= []
weig_list = []
for x in range(1000):
    weights_m = np.random.random(num_assets)
    weights_m /= np.sum(weights_m)
    weig_list.append(weights_m)
    pf_returns.append(np.sum(weights_m*log_returns.mean()) *250)
    pf_vol.append(np.sqrt(np.dot(weights_m.T,np.dot(log_returns.cov() *250, weights_m))))
#generate 1000 random return and vol

pf_returns = np.array(pf_returns)

#print('random 1000pf return',pf_returns)

pf_vol = np.array(pf_vol)

#print('random 1000 pf vol',pf_vol)

#create a dataframe containings two features
portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_vol})

#quick check
portfolios.head()

portfolios.tail()

#plot efficient frontier
#pl.plot(x=portfolios['Volatility'], y=portfolios['Return'], kind='scatter', figsize=(10,6)
#pl.show() 
#display(portfolios.iloc[97])


#def funzione ed estrazione del pf con return massimo e vol  minima
def bestMarkPf(portfolios):
    maxRet = portfolios['Return'].argmax()
    minVol = portfolios['Volatility'].argmin()
    return maxRet, minVol


maxReturnPf,minVolatilityPf = bestMarkPf(portfolios)

portfolios.iloc[maxReturnPf]

portfolios.iloc[minVolatilityPf]



'''
