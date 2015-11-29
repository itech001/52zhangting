#coding=utf-8
from pprint import pprint
from SqliteWrapper import SqliteWrapper
from Stock import Stock

dbfile = 'stocks.db'
dbtable_stocks = 'stocks'
dbtable_stocks_create = '''CREATE TABLE IF NOT EXISTS ''' + dbtable_stocks + '''
   (symbol TEXT NOT NULL,
    dateV TEXT NOT NULL,
    open REAL NOT NULL,
    close REAL NOT NULL,
    close_adj REAL NOT NULL,
    high  REAL NOT NULL,
    low  REAL NOT NULL,
    volume REAL NOT NULL,
    prev_close_to_close REAL,
    open_to_close REAL,
    low_to_high REAL);'''

dbtable_symbols = 'symbols'
dbtable_symbols_create = '''CREATE TABLE IF NOT EXISTS ''' + dbtable_symbols + '''
   (symbol CHAR(128) NOT NULL PRIMARY KEY,
    name CHAR(128) NOT NULL );'''

dbtable_concepts = 'concepts'
dbtable_concepts_create ='''CREATE TABLE IF NOT EXISTS ''' + dbtable_concepts + '''
   (concept CHAR(128) NOT NULL PRIMARY KEY,
    name CHAR(128) NOT NULL,
    url CHAR(500) NOT NULL,
    stocks CHAR(1000));
'''

class Stocks:
    def __init__(self):
        self.dbh = SqliteWrapper()
        self.dbh.connect(dbfile)
        #print('-------------------------------------')
        #print(dbtable_stocks_create)
        self.dbh.execute(dbtable_stocks_create)

    def __del__(self):
        self.dbh.close()


    def findStockBySymbolAndDate(self,symbol,dateV):
        sql = "SELECT * FROM " + dbtable_stocks + " WHERE symbol = '%s' and dateV = date('%s')" % (symbol,dateV)
        all = self.dbh.select(sql)
        stock = None
        if(len(all)):
            s = all[0]
            stock = Stock(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10])
        return stock

    def findStocksBySymbol(self,symbol):
        all = self.dbh.select("SELECT * FROM " + dbtable_stocks + " WHERE symbol = '%s' order by dateV " % symbol)
        #pprint(all)
        stockList = []
        for s in all:
            stock = Stock(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10])
            stockList.append(stock)
        return stockList

    def findGreatThan9(self):
        sql = "select symbol,count(dateV) as c from stocks where prev_close_to_close > 9 group by symbol order by c desc;"
        all = self.dbh.select(sql)
        return all

    def findGreatThan9ForLatestDays(self,num):
        sql = "select symbol,count(dateV) as c from stocks where prev_close_to_close > 9 and dateV > date('now','-%i days') group by symbol order by c desc;" %num
        all = self.dbh.select(sql)
        return all

    def getLatestClose(self,symbol):
        sql = "select close,dateV from stocks where symbol='%s' order by dateV desc " % symbol
        all = self.dbh.select(sql)
        if(len(all) > 0 ):
            return all[0][0],all[0][1]
        else:
            return 0,None

    def getLatestDate(self):
        sql = "select distinct dateV from stocks order by dateV desc;"
        all = self.dbh.select(sql)
        if(len(all) > 0 ):
            return all[0][0]
        else:
            return None

    def findGreaterCounts(self,rate):
        sql = "select count(symbol),dateV from stocks where prev_close_to_close > %f group by dateV order by dateV" %rate
        all = self.dbh.select(sql)
        return all

    def findLessCounts(self, rate):
        sql = "select count(symbol),dateV from stocks where prev_close_to_close < %f group by dateV order by dateV" % rate
        all = self.dbh.select(sql)
        return all

    def findGreatThan9ForDay(self,day):
        sql = "select symbol,count(dateV) as c from stocks where prev_close_to_close > 9 and dateV = '%s' group by symbol order by c desc;" %day
        all = self.dbh.select(sql)
        return all

    def findGreatThan9ForDay2(self,day):
        sql = "select symbol,low_to_high,prev_close_to_close as c from stocks where prev_close_to_close > 9 and dateV = '%s' group by symbol order by c desc;" %day
        all = self.dbh.select(sql)
        return all

    def insertStocks(self, symbol, stockDBHash):
        if stockDBHash is None:
            return
        #print('-------------------------------------')
        prev_close,dateV = self.getLatestClose(symbol)
        ks = stockDBHash.keys()
        for date in sorted(ks):
            value = stockDBHash[date]
            open = float(value['Open'])
            close = float(value['Close'])
            close_adj = float(value["Adj Close"])
            high = float(value['High'])
            low = float(value['Low'])
            volume = float(value['Volume'])
            pre_close_to_close = 0
            if(prev_close != 0):
                pre_close_to_close = round((close - prev_close) / prev_close *100,2)
            open_to_close = 0
            if(open != 0):
                open_to_close = round((close -open) / open * 100,2)
            low_to_high = 0
            if(low != 0):
                low_to_high = round((high - low) / low * 100,2)
            prev_close = close
            find = self.findStockBySymbolAndDate(symbol,date)
            if find is not None:
                print("existed: %s, %s" % (symbol,date) )
                continue
            try:
                sql = "INSERT INTO " + dbtable_stocks + "(symbol,dateV, open, close, close_adj, high, low, volume,prev_close_to_close,open_to_close,low_to_high) VALUES('%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f') " \
                                                        %(symbol,date, open, close, close_adj,high,low,volume,pre_close_to_close,open_to_close,low_to_high);
                #print("\n" + sql)
                self.dbh.execute (sql )
                print("add: %s, %s" % (symbol,date))
            except:
                print("Failed: " + symbol + ' ' + date )

    def insertStocksSina(self, symbol, stock):
        if stock is None:
            return
        #print('-------------------------------------')
        find = self.findStockBySymbolAndDate(symbol,stock.dateV)
        if find is not None:
            print("existed: %s, %s" % (symbol,stock.dateV) )
            return
        try:
            sql = "INSERT INTO " + dbtable_stocks + "(symbol, dateV, open, close, close_adj, high, low, volume,prev_close_to_close,open_to_close,low_to_high) VALUES('%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f') " \
                                                        %(stock.symbol,stock.dateV, float(stock.open), float(stock.close), float(stock.close_adj),float(stock.high),float(stock.low),float(stock.volume),float(stock.prev_close_to_close),float(stock.open_to_close),float(stock.low_to_high));
            #print("\n" + sql)
            self.dbh.execute (sql )
            print("add: %s, %s" % (symbol,stock.dateV))
        except Exception as e:
            print("Failed: " + symbol + ' ' + stock.dateV + 'exception:' +  str(e))

    def close(self):
        self.dbh.close()

class Symbols:
    def __init__(self):
        self.dbh = SqliteWrapper()
        self.dbh.connect(dbfile)
        #print('-------------------------------------')
        #print(dbtable_symbols_create)
        self.dbh.execute(dbtable_symbols_create)

    def __del__(self):
        self.dbh.close()

    def insertSymbol(self, symbol, name):
        try:
            sql = "INSERT INTO " + dbtable_symbols + "(symbol,name) VALUES('%s','%s') " %(symbol,name)
            #print('-------------------------------------')
            #print(sql)
            self.dbh.execute (sql )
            print("add: %s, %s" % (symbol,name))
        except Exception as e:
            print(e)

    def getSymbols(self):
        try:
            sql = "select symbol from " + dbtable_symbols
            all = self.dbh.select(sql)
            symbols = []
            for s in all:
                symbols.append(s[0])
            return symbols
        except Exception as e:
            print(e)

        return None

    def getName(self,symbol):
        sql = "select name from symbols where symbol='%s' " %symbol
        all = self.dbh.select(sql)
        if(len(all)):
            return all[0][0]
        return None

    def close(self):
        self.dbh.close()


class Concepts:
    def __init__(self):
        self.dbh = SqliteWrapper()
        self.dbh.connect(dbfile)
        print('-------------------------------------')
        print(dbtable_concepts_create)
        self.dbh.execute(dbtable_concepts_create)

    def __del__(self):
        self.dbh.close()

    def insertConcept(self, concept, name, url,stocks):
        con = self.getConcept(concept)
        if con:
            print(concept + 'is existed')
            return
        try:
            sql = "INSERT INTO " + dbtable_concepts + "(concept,name,url,stocks) VALUES('%s','%s','%s','%s') " %(concept,name,url,stocks)
            #print('-------------------------------------')
            #print(sql)
            self.dbh.execute (sql )
            print("add: %s, %s, %s, %s" % (concept,name,url,stocks))
        except Exception as e:
            print(e)

    def getConcepts(self):
        try:
            sql = "select * from " + dbtable_concepts
            all = self.dbh.select(sql)
            return all
        except Exception as e:
            print(e)

        return None

    def getConcept(self,concept):
        sql = "select * from %s where concept='%s' " %(dbtable_concepts,concept)
        all = self.dbh.select(sql)
        return all

    def getConceptByStock(self,stock):
        sql = "select name,url from %s where stocks like '%s" %(dbtable_concepts,stock)
        all = self.dbh.select(sql)
        links_str = ''
        for a in all:
            name = a[0]
            link = a[1]
            if links_str == '':
                links_str = "<a href=%s>%s</a>" % (name,link)
            else:
                links_str += ",<a href=%s>%s</a>" % (name,link)

        return links_str


    def close(self):
        self.dbh.close()


