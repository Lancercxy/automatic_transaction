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
                     
def market_open():
    # log.info('函数运行时间(market_open):'+str(context.current_dt.time()))
    #1、读取将要购入的个股代码
    df = pd.read_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\willbuy_code_list.csv')
    
    #2、创建名为own_stock的列表，用于存储以购买的个股代码
    own_stock = []
    
    #3、取得当前的现金并平均分成n份（n为即将购买的个股数）
    # cash = context.portfolio.available_cash/len(df)
    
    #4、遍历数据
    for code in df['code']:
        # print(code)
        # g.security = f'{code}.XSHE'
        # security = g.security
        
        #5、调用high_open()函数判断高开是否在0-2%之间
        # if high_open(f'{code}.XSHE'):
            
            #6、若满足要求用cash买入股票
            # order_value(code, cash)
            
            #7、将已经买入的股票代码保存入own_stock列表
            own_stock.append(code)
        # else:
            # 若不满足则打印出来
            print("不买入",code)
        
    #8、将已经买入的股票代码以CSV格式保存入本地文件
    pf = pd.DataFrame(own_stock)
    pf.columns=['code']
    pf.to_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\own_stock.csv',index=False)    
    

def sell_stock():
    
    #1、读取已拥有的个股代码
    df = pd.read_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\own_stock.csv')
    
    #2、创建Limit_of_drop列表用于存储跌停的个股
    Limit_of_drop = []
    
    #3、判断数据是否为空,不为空则遍历数据
    if len(df) != 0:
        # for code in df['code']:
            # print(code)
            # g.security = f'{code}.XSHE'
            # security = g.security
            
            #4、调用change_pct()函数判断其涨跌幅(返回'0'可卖出,返回'-1'为跌停,涨停返回'1')
            state = change_pct('-1')
            if state == '0':
                
                #5、若满足要求卖出股票
                # order_target(code, 0)
                
                #6、将已经卖出的股票代码从own_stock文件移除
                df = pd.read_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\own_stock.csv')
                df01 = df.drop(df[df['code']==688350].index)
                df01.to_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\own_stock.csv',index=False)
                
            #7、处理跌停的个股
            elif state == '-1':
                
                #8、将代码添加进列表
                Limit_of_drop.append(603859)
                
                #9、将跌停的股票代码从own_stock文件移除
                df = pd.read_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\own_stock.csv')
                df01 = df.drop(df[df['code']==603859].index)
                df01.to_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\own_stock.csv',index=False)
                # print("无法卖出",code)
    if  len(Limit_of_drop) != 0:     
        #10、将跌停的股票代码以CSV格式保存为Limit_of_drop_stock文件
        drop = pd.DataFrame(Limit_of_drop)
        drop.columns=['code']
        drop.to_csv('D:\office\Github\爬虫\自动买卖股票数据采集\data\Limit_of_drop_stock.csv',index=False)       
        
def change_pct(code):
    #1、获取今天日期
    # g.today = context.current_dt.strftime('%Y-%m-%d')
    
    # #2、获取上个交易日日期
    # g.start = context.current_dt - datetime.timedelta(day = 1)
    
    # #3、获取涨跌幅
    # money_flow = get_money_flow(f'{code}.XSHG',start_date=g.start, end_date=g.today, fields="change_pct")
    
    #4、判断是否满足高开在0-2%之间
    if code == '0':
        return '0'
    elif code == '-1':
        return '-1'
    else:
        return '1'                               

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
    # b(a())
    # market_open()
    # print(change_pct('-1'))
    sell_stock()