from pandas_datareader import data as wb
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time
from yahoofinancials import YahooFinancials

from Stock_Functions import * 

class Stock:

    def __init__(self):
        self.mydata = None
        self.tickers = None
        self.weights = None
        self.sp500 = None
        self.yr_10 = None

    # Selezione dei ticker da mettere su file JSON
    def initData(self):
        #self.tickers = ['ACN', 'AMZN', 'AIG', 'BLK','TSLA','TRI','VGT','EZJ','MA', 'BABA']
        #self.weights = np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
        self.tickers = ['ACN', 'TSLA', 'EZJ', 'BLK','IBM','VGT']
        self.weights = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
        #self.tickers = ['FCAU', 'HSBC', 'JUVE.MI', 'FB', 'AAPL', 'AMZN']
        #self.weights = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
        self.mydata = portfolio(self.tickers)
        self.sp500, self.yr_10 = SP500()

    def getMydata(self):
        return self.mydata

    def getWeights(self):
        return self.weights
    
    def getTickers(self):
        return self.tickers

    def getSP500(self):
        return self.sp500

    def getYR10(self):
        return self.yr_10

    # Pesi delle singole azioni, ritorno annuale, ritorno annuale pesato e volatilità
    def recapPortfolio(self):
        annual_returns = pf_return(self.mydata)
        annualReturnW = weigthedReturn(annual_returns, self.weights)
        x, y = dailyReturn(self.mydata)
        volatility = pfRisk(annual_returns, self.tickers)
        #disegna grafico
        recap(x,y)
        return annualReturnW, volatility, y[-1]
        

    def recapStock(self):
        ### singole azioni stock
        annual_returns = pf_return(self.mydata)
        volatility = pfRisk(annual_returns, self.tickers)
        stockRecap(self.mydata, self.tickers)
        return annual_returns, self.tickers
        
    
    #Markowitz Portfolio Optimization
    def markovitz(self):
        covRetLog = pfCov(self.mydata)
        corrRetLog = pfCorr(self.mydata)
        num_assets = len(self.tickers)
        appendPfRet = returns(self.mydata).mean() * 250

        pf_returns= []
        pf_vol= []
        weig_list = []
        sharpe_list = []
        
        #generate a for loop which gives back 5000 pf weights
        #w /= sum.(w) is equivalent to w = w / sum.(w)->w1/(w1+w2) + w2/(w1+w2..) + wn/(sum.wn)=1
        for x in range(5000):
            weights_m = np.random.random( num_assets )
            weights_m /= np.sum( weights_m )
            weig_list.append( weights_m )
            singleReturn = np.sum( np.dot(weights_m, appendPfRet) )
            singleVol = np.sqrt(np.dot( weights_m.T, np.dot( covRetLog, weights_m )))
            pf_returns.append( singleReturn )
            pf_vol.append( singleVol )
            sharpe_list.append( (singleReturn - self.yr_10) / singleVol )
        
        weig_list = [np.round(num, 4) for num in weig_list]
        pf_returns = np.array(pf_returns)
        pf_vol = np.array(pf_vol)

        #create a dataframe containings three features
        portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_vol, 'weig_list': weig_list, 'sharpe': sharpe_list})
        
        # Find our 3 best porfolios
        maxReturnPf = portfolios['Return'].argmax()
        minVolatilityPf = portfolios['Volatility'].argmin()
        sharpeMax = portfolios['sharpe'].argmax()
        pfpuntoMaxRet = portfolios.iloc[maxReturnPf]
        pfpuntoMinVol  = portfolios.iloc[minVolatilityPf]
        pfpuntoSharpe = portfolios.iloc[sharpeMax]
        #plot efficient frontier 
        stockMarkovitz(portfolios, pfpuntoMaxRet, pfpuntoMinVol, pfpuntoSharpe)

        return  pfpuntoMaxRet, pfpuntoMinVol, pfpuntoSharpe, self.tickers
    
