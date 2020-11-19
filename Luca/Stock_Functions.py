from pandas_datareader import data as wb
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Select data from database
def portfolio(tickers):
    mydata = pd.DataFrame()
    for t in tickers:
        mydata[t]= wb.DataReader(t,data_source='yahoo', start='2015-1-1')['Adj Close']
    return mydata    
    
#calculate a portfolio annual return
def pf_return(mydata):
    returns = (mydata/ mydata.shift(1)) -1
    annual_returns= returns.mean() * 250
    return annual_returns

#ritorna rendimenti giornalieri
def returns(mydata):
    return np.log((mydata/ mydata.shift(1)))
    
    
# Ritorna portfolio pesato
def weigthedReturn(annual_returns, weights):
    return round(np.dot(annual_returns, weights),4)*100
    
# Ritorna il rischio del portafoglio    
def pfRisk(annual_returns, tickers):
    return annual_returns[tickers].std() 


#calcola cov portafoglio
def pfCov(mydata):
    return returns(mydata).cov() * 250


#calcola corr portafoglio
def pfCorr(mydata):
    return returns(mydata).corr() 

# Plot trend
def recap(x, y):
    #mydata.plot(figsize=(16,8))
    plt.plot(x, y)
    plt.ylabel('Equity Line')
    plt.xlabel('Days')
    plt.savefig('../img/recap.png')

def returnsLog(mydata):
    return np.log(mydata / mydata.shift(1))


#calculate a portfolio annual return
def dailyReturn(mydata):
    daily = (mydata/ mydata.shift(1)).mean(axis = 1) - 1
    lenght = daily.size
    new_list=[] 
    day_list=[]
    i=0
    j=0
    for i in range(1, lenght):
        j+=daily.iloc[i]
        new_list.append(j)
        i+=1
        day_list.append(i)
    l = [10000 + (x * 10000) for x in new_list]
    return day_list, l