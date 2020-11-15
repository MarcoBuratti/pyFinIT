from pandas_datareader import data as wb
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from Stock_Functions import * 

# Selezione dei ticker da mettere su file JSON
tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL']
weights = np.array([0.25,0.25,0.25,0.25])
mydata = portfolio(tickers)



# Pesi delle singole azioni, ritorno annuale, ritorno annuale pesato e volatilità
def recapKey():
    recap(mydata)
    annual_returns = pf_return(mydata)
    annualReturnW = weigthedReturn(annual_returns, weights)
    volatility = pfRisk(annual_returns, tickers)
    return annual_returns, annualReturnW, volatility
 
# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

#diversifiable risk = port_var - weighted annual variances

#dir_risk = (print(volatility) - (weights[0]**2*sing_var('TSLA')) - (weights[1]**2*sing_var('AAPL'))- (weights[2]**2*sing_var('VGT')) - (weights[3]**2*sing_var('ORCL'))

#print( dir_risk)

#print('pf rounded div risk: ', str(round(dir_risk*100,3))+'%')

#non_dir_risk = portfolio_var - dir_risk

#print('pf non div risk: ', non_dir_risk)

#print('rounded pf non div risk: ', str(round(non_dir_risk*100,3))+'%')


#Markowitz Portfolio Optimization

covRetLog = pfCov(mydata)
corrRetLog = pfCorr(mydata)
num_assets = len(tickers)

pf_returns= []
pf_vol= []
weig_list = []
#generate a for loop which gives back 1000 pf weights
#sum of these random number must be equal to 1(sum of pf assets)
#w /= sum.(w) is equivalent to w = w / sum.(w)->w1/(w1+w2) + w2/(w1+w2..) + wn/(sum.wn)=1
for x in range(1000):
    weights_m = np.random.random( num_assets )
    weights_m /= np.sum( weights_m )
    weig_list.append( weights_m )
    pf_returns.append(np.sum( weights_m * returns(mydata).mean() ) * 250)
    pf_vol.append(np.sqrt(np.dot( weights_m.T, np.dot( covRetLog, weights_m ))))


weig_list = [np.round(num, 4) for num in weig_list]
pf_returns = np.array(pf_returns)
pf_vol = np.array(pf_vol)

#create a dataframe containings three features
portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_vol, 'weig_list': weig_list})
# Find our 3 best porfolios
def bestMarkPf(portfolios):
    maxRet = portfolios['Return'].argmax()
    minVol = portfolios['Volatility'].argmin()
    avgRet = (portfolios['Return'].argmax()//3)
    return maxRet, minVol, avgRet

maxReturnPf, minVolatilityPf, avgReturnPf = bestMarkPf(portfolios)  
pfpuntoMaxRet = portfolios.iloc[maxReturnPf]
pfpuntoMinVol  = portfolios.iloc[minVolatilityPf]
pfpuntoAvgRet = portfolios.iloc[avgReturnPf]
print(portfolios.iloc[maxReturnPf])
#plot efficient frontier 
portfolios.plot( x = 'Volatility', y = 'Return', kind = 'scatter', figsize = (10,6) )
plt.scatter( x = pfpuntoMaxRet['Volatility'], y = pfpuntoMaxRet['Return'], c = 'r')
plt.scatter( x = pfpuntoMinVol['Volatility'], y = pfpuntoMinVol['Return'], c = 'r')
plt.scatter( x = pfpuntoAvgRet['Volatility'], y = pfpuntoAvgRet['Return'], c = 'r')
plt.savefig('../img/frontier.png')
