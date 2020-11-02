from pandas_datareader import data as wb
import pandas as pd

tickers = ['AAPL', 'MSFT', 'XOM', 'BP']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='2015-1-1')['Adj Close']
    print(new_data)
    
