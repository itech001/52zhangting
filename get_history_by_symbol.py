import re
from datetime import *
from pprint import pprint
import ystockquote
from StockDB import Stocks
import StockCommon


date_start = '2015-01-01'
date_end = '2015-10-24'
nowStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("Start:" + nowStrFull)

todayStr = ( datetime.now() - timedelta(0)).strftime('%Y-%m-%d')
tomorrowStr = ( datetime.now() + timedelta(1) ).strftime('%Y-%m-%d')
date_end =  tomorrowStr
print("update: %s - %s"  % (date_start, date_end) )

sdb = Stocks();

stock = '000001'
symbol,symbol_y = StockCommon.symbolFormat(stock)
print('-------------------------------------')
print(symbol_y)
all = ystockquote.get_historical_prices(symbol_y,date_start, date_end)
sdb.insertStocks(symbol,all)

sdb.close()

nowStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("End:" + nowStrFull)
