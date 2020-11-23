from pandas_datareader import data as wb
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time

from Stock_Functions import * 

class Stock:

    def __init__(self):
        self.mydata = None
        self.tickers = None
        self.weights = None

    # Selezione dei ticker da mettere su file JSON
    def initData(self):
        #self.tickers = ['ACN', 'AMZN', 'AIG', 'BLK','TSLA','TRI','VGT','EZJ','MA', 'BABA']
        #self.weights = np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
        self.tickers = ['ACN', 'TSLA', 'EZJ', 'BLK','IBM','VGT']
        self.weights = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
        #self.tickers = ['AMZN', 'TRI', 'VGT', 'TSLA']
        #self.weights = np.array([0.25,0.25,0.25,0.25])
        self.mydata = portfolio(self.tickers)

    def getMydata(self):
        return self.mydata

    def getWeights(self):
        return self.weights
    
    def getTickers(self):
        return self.tickers

    # Pesi delle singole azioni, ritorno annuale, ritorno annuale pesato e volatilità
    def recapPortfolio(self):
        annual_returns = pf_return(self.mydata)
        annualReturnW = weigthedReturn(annual_returns, self.weights)
        x, y = dailyReturn(self.mydata)
        volatility = pfRisk(annual_returns, self.tickers)
        #disegna grafico
        recap(x,y)
        return annualReturnW, volatility
        

    def recapStock(self):
        ### singole azioni stock
        annual_returns = pf_return(self.mydata)
        annualReturnW = weigthedReturn(annual_returns, self.weights)
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
        #generate a for loop which gives back 1000 pf weights
        #sum of these random number must be equal to 1(sum of pf assets)
        #w /= sum.(w) is equivalent to w = w / sum.(w)->w1/(w1+w2) + w2/(w1+w2..) + wn/(sum.wn)=1
        for x in range(10000):
            weights_m = np.random.random( num_assets )
            weights_m /= np.sum( weights_m )
            weig_list.append( weights_m )
            pf_returns.append(np.sum( np.dot(weights_m, appendPfRet) ) )
            pf_vol.append(np.sqrt(np.dot( weights_m.T, np.dot( covRetLog, weights_m ))))


        weig_list = [np.round(num, 4) for num in weig_list]
        pf_returns = np.array(pf_returns)
        pf_vol = np.array(pf_vol)

        #create a dataframe containings three features
        portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_vol, 'weig_list': weig_list})
        # Find our 3 best porfolios

        maxReturnPf = portfolios['Return'].argmax()
        minVolatilityPf = portfolios['Volatility'].argmin()
        pfpuntoMaxRet = portfolios.iloc[maxReturnPf]
        pfpuntoMinVol  = portfolios.iloc[minVolatilityPf]
        #plot efficient frontier 
        stockMarkovitz(portfolios, pfpuntoMaxRet, pfpuntoMinVol)

        return  pfpuntoMaxRet, pfpuntoMinVol, self.tickers
    
