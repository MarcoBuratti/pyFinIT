#Import libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
from IPython import get_ipython
from Stock_Functions import *

def MC_Simulation(mydata):

    daily = (mydata/ mydata.shift(1)).mean(axis = 1) - 1
    log_returns = np.log( 1 + daily)

    lenght = daily.size
    new_list=[] 
    j=0
    #cumulated return
    for i in range(1, lenght):
        j+=daily.iloc[i]
        new_list.append(j)
    dailyPortfolio = [10000 + (x * 10000) for x in new_list]

    #Compute the mean of log returns
    avgReturn = log_returns.mean()
    #Compute the var of log returns
    var = log_returns.var()
    #Compute the drift component
    drift = avgReturn - (0.5 * var)
    #Compute st dev
    stdev = log_returns.std()

    #Check if drift is a pandas series and covert
    #select values from drift
    l = pd.Series(drift)
    drift = l
    l = pd.Series(stdev)
    stdev = l


    #Number of upcoming days for which we make forecasts
    t_intervals = 1850
    #Number of iterations of series stock price predictions
    iterations = 5

    #Compute future daily returns
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))

    #We need to create a price list
    #Each price must be equal to: St = S0 * daily_return
    S0 = dailyPortfolio[-1]

    #Obtain an array with the same number of elements  of previous matrix
    price_list = np.zeros_like(daily_returns)

    #S0 would be the new initial price for each of the ten iterations
    price_list[0] = S0
    #Compute price list over the number of t_intervals
    for t in range (1, t_intervals):
        price_list[t] = price_list[t-1]*daily_returns[t]

    #Plot 
    plt.figure(figsize=(10, 6))
    plt.plot(price_list)
    plt.ylabel("Return in $ of portfolio")
    plt.xlabel("Days")
    plt.annotate( str(round(price_list[0][0], 2) ), (0, price_list[0][0]) )
    plt.annotate( str(round(price_list[-1][0], 2) ), (1750, price_list[-1][0]) )
    plt.annotate( str(round(price_list[-1][1], 2) ), (1750, price_list[-1][1]) )
    plt.annotate( str(round(price_list[-1][2], 2) ), (1750, price_list[-1][2]) )
    plt.annotate( str(round(price_list[-1][3], 2) ), (1750, price_list[-1][3]) )
    plt.savefig('../img/mc_sim.png')
    plt.close('all')

