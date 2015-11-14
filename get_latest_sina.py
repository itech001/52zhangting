import re
from datetime import *
from pprint import pprint
import ystockquote
from StockDB import Stocks
import StockCommon


nowStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("Start:" + nowStrFull)
todayStr = ( datetime.now() - timedelta(0)).strftime('%Y-%m-%d')

sdb = Stocks();


for stock in StockCommon.getAllSymbols2():
    symbol,symbol_y = StockCommon.symbolFormat(stock)
    print('-------------------------------------')
    print(symbol)
    s,is_close_price = StockCommon.getStock(symbol,todayStr)
    if is_close_price:
        sdb.insertStocksSina(symbol,s)
    else:
        print('the stock market stil openning, need run later')
        break

sdb.close()

nowStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("End:" + nowStrFull)
