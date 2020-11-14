from pandas_datareader import data as wb
import pandas as pd
#from matplotlib import pyplot as plt
import numpy as np

from Stock_Functions import * 

# Selezione dei ticker da mettere su file JSON
tickers = ['TSLA', 'AAPL', 'VGT', 'ORCL']
mydata = portfolio(tickers)



# Plot trend
#def recap(mydata):
    #mydata.plot(figsize=(16,8))
    #plt.plot(mydata)
    #plt.ylabel('Stock Price')
    #plt.savefig('../img/recap.png')


# Pesi delle singole azioni, ritorno annuale, ritorno annuale pesato e volatilità
weights = np.array([0.25,0.25,0.25,0.25])
annual_returns = pf_return(mydata)
annualReturnW = weigthedReturn(annual_returns, weights)
volatility = pfRisk(annual_returns, tickers)

#print(pfCov(annual_returns,tickers))

pfCovMatrix = pfCov(mydata)

pfCorrMatrix = pfCorr(mydata)
 

#single stock variance
def sing_var(tickers):
    return returns(mydata).std() * 250
    

print(sing_var(mydata['AAPL'])


# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio


#diversifiable risk = port_var - weighted annual variances

#dir_risk = (print(volatility) - (weights[0]**2*TSLA_var_a) - (weights[1]**2*AAPL_var_a)- (weights[2]**2*VGT_var_a)- (weights[3]**2*ORCL_var_a)

#print('pf diversificable risk: ', dir_risk)

#print('pf rounded div risk: ', str(round(dir_risk*100,3))+'%')

#non_dir_risk = portfolio_var - dir_risk

#print('pf non div risk: ', non_dir_risk)

#print('rounded pf non div risk: ', str(round(non_dir_risk*100,3))+'%')




#Markowitz Portfolio Optimization


#log_returns = np.log(mydata / mydata.shift(1))

#log_returns.cov() *250

#log_returns.corr()

#num_assets = len(tickers)

#generate a for loop which gives back 1000 pf weights
#sum of these random number must be equal to 1(sum of pf assets)
#in other words (w1/(w1+w2)+(w2/(w1+w2)

#pf_returns= []
#pf_vol= []
#weig_list = []

#for x in range(1000):
 #   weights_m = np.random.random(num_assets)
  #  weights_m /= np.sum(weights_m)
   # weig_list.append(weights_m)
    #pf_returns.append(np.sum(weights_m*log_returns.mean()) *250)
    #pf_vol.append(np.sqrt(np.dot(weights_m.T,np.dot(log_returns.cov() *250, weights_m))))

#pf_returns = np.array(pf_returns)

#pf_vol = np.array(pf_vol)

#create a dataframe containings three features
#portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_vol, 'weig_list': weig_list})


#plot markoviz frontieer

#plt.plot(portfolios)



#generate a function which gives back the three best pf for three different risk avversion class(Low,Avg,High risk avv.)

#def bestMarkPf(portfolios):
 #   maxRet = portfolios['Return'].argmax()
  #  minVol = portfolios['Volatility'].argmin()
   # avgRet = (portfolios['Return'].argmax()//3)
    #return maxRet, minVol, avgRet



#attach three values to the three pf

#maxReturnPf, minVolatilityPf, avgReturnPf = bestMarkPf(portfolios)  


#print low risk adversion pf

#print('Max return-risk pf', portfolios.iloc[maxReturnPf])


#print avg risk adversion pf

#print('Avg return-risk pf',portfolios.iloc[avgReturnPf])


#print high risk adversion pf

#print('min return-risk pf',portfolios.iloc[maxReturnPf])