from StockDB import Symbols
import StockCommon

symbols = Symbols()

for stock in StockCommon.getAllSymbols():
    symbol,symol_y = StockCommon.symbolFormat(stock)
    name = StockCommon.getStockName(symbol)
    if name:
        symbols.insertSymbol(symbol,name)

symbols.close()