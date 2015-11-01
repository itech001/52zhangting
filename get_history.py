import re
from datetime import *
from pprint import pprint
import ystockquote
from StockDB import Stocks
import StockCommon

#ystockquote.get_historical_prices('002317.SZ','2015-01-01','2015-10-24')

#date_start = '2015-01-01'
#date_end = '2015-10-24'

todayStr = datetime.now().strftime('%Y-%m-%d')
ago = datetime.now() - timedelta(8)
agoStr = ago.strftime('%Y-%m-%d')
date_start = agoStr
date_end =  todayStr

sdb = Stocks();

for stock in StockCommon.getAllSymbols2():
#for stock in ['600008']:
    #if(stock < '600008'): continue
    #if(re.search('318$',stock)): continue
    symbol,symbol_y = StockCommon.symbolFormat(stock)
    print(symbol_y)
    #has = sdb.findStocksBySymbol(symbol)
    #if(len(has)):
    #    print("existed:" + symbol_y)
    #    continue
    all = ystockquote.get_historical_prices(symbol_y,date_start, date_end)
    sdb.insertStocks(symbol,all)

sdb.close()


