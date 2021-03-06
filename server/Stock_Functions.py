from pandas_datareader import data as wb
from yahoofinancials import YahooFinancials
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Select data from database
def portfolio(tickers):
    print('Downloading data....')
    mydata = pd.DataFrame()
    for t in tickers:
        mydata[t]= wb.DataReader(t,data_source='yahoo', start='2014-01-01', end='2016-12-30')['Adj Close']
    return mydata    
    
def SP500():
    SP500_ret = wb.get_data_yahoo('^GSPC', start = '2019-11-19')["Adj Close"].pct_change()[1:]
    yahoo_financials = YahooFinancials('^TNX')
    yr_10 = yahoo_financials.get_current_price()/100  
    return SP500_ret, yr_10
      
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
    return round(np.dot(annual_returns, weights), 4)*100
    
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
    plt.plot(x, y)
    plt.annotate( str( int(y[-1]) ), (250, y[-1]) )
    plt.ylabel('Equity Line')
    plt.xlabel('Days')
    plt.savefig('../img/recap.png')
    plt.close('all')

def stockRecap(mydata, tickers):
    #mydata.plot(figsize=(16,8))
    plt.plot(mydata)
    for t in tickers:
        plt.annotate( str( t ), ('2019-11-19', mydata.get(t)[0]) )
    plt.ylabel('Stock prices')
    plt.xlabel('Days')
    plt.savefig('../img/stock.png')
    plt.close('all')

def stockMarkovitz(portfolios, pfpuntoMaxRet, pfpuntoMinVol, sharpeMax):
    portfolios.plot( x = 'Volatility', y = 'Return', kind = 'scatter', figsize = (10,6) )
    plt.scatter(portfolios['Volatility'], portfolios['Return'], c=portfolios['sharpe'], cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.scatter( x = pfpuntoMaxRet['Volatility'], y = pfpuntoMaxRet['Return'], c = 'r')
    plt.scatter( x = sharpeMax['Volatility'], y = sharpeMax['Return'], c = 'r')
    plt.scatter( x = pfpuntoMinVol['Volatility'], y = pfpuntoMinVol['Return'], c = 'r')
    plt.savefig('../img/frontier.png')
    plt.close('all')

#calculate a portfolio annual return
def dailyReturn(mydata):
    daily = (mydata/ mydata.shift(1)).mean(axis = 1) - 1
    lenght = daily.size
    new_list=[] 
    day_list=[]
    i=0
    j=0
    # Cumulated return
    for i in range(1, lenght):
        j+=daily.iloc[i]
        #aggiungi elemento j in coda alla lista
        new_list.append(j)
        i+=1
        day_list.append(i)
    l = [10000 + (x * 10000) for x in new_list]
    return day_list, l