#calculate a portfolio RR
def pf_return(tickers):
    mydata = pd.DataFrame()
    for t in tickers:
        mydata[t]= wb.DataReader(t,data_source='yahoo', start='2010-1-1')['Adj Close']
    return (mydata/ mydata.shift(1)) -1

    