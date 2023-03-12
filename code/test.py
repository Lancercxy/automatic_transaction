import akshare as ak
import matplotlib.pyplot as plt 
from pylab import mpl
import pandas as pd
from jqdatasdk  import *
import datetime
import time

def a():
    print('aaa')
    
def b(fun):
    fun
    
def timerFun(sched_Timer):
    flag = 0
    while True:
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        if now == sched_Timer:
            # run_Task()
            print("我在规定时间运行了！！")
            print(now)
            flag-1
            return 0
            
        else:
            print("时间未到")
            time.sleep(0.5)
            if flag == 1:
                sched_Timer = sched_Timer + datetime.timedelta(day=1)
                flag = 0                                             
                                                               

if __name__ == "__main__":
    
    
    # df = ak.stock_zh_a_hist(symbol='688039',start_date="20230301", end_date='20230310', adjust="")
    # print(df)
    # path = '/Users/pengbin/Downloads/mkt_index.xlsx'
    # df.to_excel(path, index=False)
    # date = df['date']
    # close = df['close']
    # print(close)
    # start_date = (datetime.datetime.now() - datetime.timedelta(days = 30))
    # start_date = start_date.strftime('%Y%m%d')
    # end_date = time.strftime('%Y%m%d')
    
    # df = ak.stock_zh_a_hist(symbol='600095',start_date=start_date, end_date=end_date, adjust="")
    # print(df)
    # tomorrow = (datetime.datetime.now() + datetime.timedelta(days = 1))
    # sell_Timer = datetime.datetime(tomorrow.year,tomorrow.month,tomorrow.day,14,55,0)
    # print(sell_Timer.strftime('%Y%m%d%H%M%S'))
    # timerFun(sell_Timer.strftime('%m%d%H%M%S'))
    
    # df = pd.read_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\willbuy_code_list.csv')
    # df01 = df.drop(df[df['code']==688004].index)
    # df01.to_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\willbuy_code_list.csv',index=False)
    b(a())