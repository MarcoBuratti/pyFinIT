#Predict stock prices
#price (today) = price (yesterday)*e^r
#where r is the log return (share price of today / share price of yesterday)

#Brownian motion

#DRIFT = (average return - 1/2*variance)
#The drift is the expected dailyreturn of the stock

#VOLATILITY: random variable = st.dev*Z(Rand(0;1))

#Repeat this calculation 1000 times
#Price(today) = price(yesterday)*e^((mean-1/2*variance) + st.dev * Z[Rand(0;1)])


#Import libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')




#Import data
ticker = "PG"
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = "yahoo", start = "2007-1-1")["Adj Close"]




#Calculate log returns
log_returns = np.log(1 + data.pct_change())




#Check
log_returns.tail()




#Plot prices
data.plot(figsize=(10, 6))




#Plot of log return (data normally distributed)
log_returns.plot(figsize=(10, 6))




#Compute the mean of log returns
u = log_returns.mean()
print(u)




#Compute the mean of log returns
var = log_returns.var()
print(var)




#Compute the drift component
drift = u - (0.5 * var)
print(drift)




#Compute st dev
stdev = log_returns.std()
print(stdev)




#REM. r = drift + stdev * e^r




#Check if drift is a pandas series
type(drift)




#Check if drift is a pandas series
type(stdev)




#Convert value into a np array
drift.values
stdev.values




#REM. The second component of the Brownian motion is a random variable, a number corresponding
#to the distance between the mean and the events, expessed as the number of st. dev.




#Norm distribution function with 95%
norm.ppf(0.95)




#Probabilities
x = np.random.rand(10, 2)
print(x)




#Values
norm.ppf(x)




#Expression corresponding to Z
#Array which uses the probabilities generated the random function and convert into distances 
#from mean 0 (in terms of st dev)
Z = norm.ppf(np.random.rand(10, 2))
print(Z)




#Number of upcoming days for which we make forecasts
t_intervals = 1000




#Number of iterations of series stock price predictions
iterations = 10




#COmpute future daily returns
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
print(daily_returns)




#We need to create a price list
#Each price must be equal to: St = S0 * daily_return
S0 = data.iloc[-1]
print(S0)




#Obtain an array with the same number of elements  of previous matrix
price_list = np.zeros_like(daily_returns)
print(price_list)




#S0 would be the new initial price for each of the ten iterations
price_list[0] = S0
print(price_list)




#Compute price list over the number of t_intervals
for t in range (1, t_intervals):
    price_list[t] = price_list[t-1]*daily_returns[t]
print(price_list)



#Plot 
plt.figure(figsize=(10, 6))
plt.plot(price_list)

