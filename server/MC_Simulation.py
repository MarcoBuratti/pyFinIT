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
    meanRet = log_returns.mean()
    #Compute the var of log returns
    variance = log_returns.var()
    #Compute the drift component
    drift = meanRet - (0.5 * variance)
    #Compute st dev
    stdev = log_returns.std()

    #Check if drift is a pandas series and covert
    #cast of dataset to pandas series
    l = pd.Series(drift)
    drift = l
    l = pd.Series(stdev)
    stdev = l


    #Number of upcoming days for which we make forecasts
    time_range = 750
    #Number of iterations of series stock price predictions
    iterations = 5

    #Compute future daily returns
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(time_range, iterations)))

    #We need to create a price list
    #Each price must be equal to: St = S0 * daily_return
    Y0 = dailyPortfolio[-1]

    #Obtain an array with the same number of elements  of previous matrix
    price_list = np.zeros_like(daily_returns)

    #S0 would be the new initial price for each of the ten iterations
    price_list[0] = Y0
    #Compute price list over the number of t_intervals
    for t in range (1, time_range):
        price_list[t] = price_list[t-1]*daily_returns[t]

    #Plot 
    plt.figure(figsize=(10, 6))
    plt.plot(price_list)
    plt.ylabel("Return in $ of portfolio")
    plt.xlabel("Days")
    plt.annotate( str(round(price_list[0][0], 2) ), (0, price_list[0][0]) )
    plt.annotate( str(round(price_list[-1][0], 2) ), (750, price_list[-1][0]) )
    plt.annotate( str(round(price_list[-1][1], 2) ), (750, price_list[-1][1]) )
    plt.annotate( str(round(price_list[-1][2], 2) ), (750, price_list[-1][2]) )
    plt.annotate( str(round(price_list[-1][3], 2) ), (750, price_list[-1][3]) )
    plt.annotate( str(round(price_list[-1][4], 2) ), (750, price_list[-1][4]) )
    plt.savefig('../img/mc_sim.png')
    plt.close('all')

    tot = 0
    lastValue = []
    for i in range(iterations):
        tot += price_list[-1][i]
        lastValue.append(price_list[-1][i])

    avg = tot / iterations
    maxVal = max(lastValue)
    minVal = min(lastValue)
    stdVal = np.std(lastValue)

    return round(avg, 2), round(maxVal, 2), round(minVal, 2), round(stdVal, 2)
