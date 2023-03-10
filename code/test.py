import akshare as ak
import matplotlib.pyplot as plt 
from pylab import mpl
import pandas as pd


if __name__ == "__main__":
    
    
    df = ak.stock_zh_a_hist(symbol='688039',start_date="20230301", end_date='20230310', adjust="")
    print(df)
    path = '/Users/pengbin/Downloads/mkt_index.xlsx'
    df.to_excel(path, index=False)
    date = df['date']
    close = df['close']
    print(close)