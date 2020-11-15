from pandas_datareader import data as wb
import pandas as pd
import numpy as np

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

