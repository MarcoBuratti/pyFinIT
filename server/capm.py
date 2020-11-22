#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as wb
from scipy import stats
import seaborn as sns
from yahoofinancials import YahooFinancials


def CAPM(mydata):
    const_weights = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    #Calculate stocks daily return
    # DA TENERE
    #Calculate portfolio daily return    
    ret_data = mydata.pct_change()[1:]
    pf_ret = (ret_data * const_weights).sum(axis = 1)

    #Import SP500 data and calculate daily return
    SP500_ret = wb.get_data_yahoo('^GSPC', start = '2019-11-19')["Adj Close"].pct_change()[1:]

    #Build a regression model: pf_return vs SP500_return
    sns.regplot(x=SP500_ret, y=pf_ret)
    #plt.plot(SP500_ret, pf_ret)
    plt.xlabel("Return of SP500")
    plt.ylabel("Portfolio Return")
    plt.savefig('../img/capm.png')
    plt.close('all')
    beta, alpha = stats.linregress(SP500_ret.values, pf_ret.values)[0:2]

    # Import ten yield bonds
    yahoo_financials = YahooFinancials('^TNX')
    yr_10 = yahoo_financials.get_current_price()/100

    #Portfolio expected return
    mkt_risk_prem = 0.05
    Pf_exp_ret = yr_10 + beta * mkt_risk_prem

    Sharpe = (0.4168 - yr_10) / (0.6841)
    #print('Beta: ', beta)
    #print('Alpha: ', alpha)
    #print('Sharpe: ', Sharpe)
    #print('Pf ecp: ', Pf_exp_ret)
    #portfolio expected return, sharpe = indice del portafoglio

    return alpha, beta, Sharpe