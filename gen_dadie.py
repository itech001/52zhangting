#coding=utf-8

import os
import re
from  datetime  import  *
from StockDB import *
from Stock import Stock
from pyh import *
from StockCommon import *

stocks = Stocks()
symbols = Symbols()
all_symbols = symbols.getSymbols()
concepts = Concepts()

showRecord = 100
latestDate = stocks.getLatestDate()
day_ago = stocks.getOldDate(1)
week_ago = stocks.getOldDate(7)
month_ago = stocks.getOldDate(30)
#all = stocks.findGreatThan9()
all = stocks.findGreatThan9ForLatestDays(30)

todayStr = datetime.now().strftime('%Y-%m-%d')
todayStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

title = "妖股大跌"

page = PyH(title)
page.addCSS('../bootstrap-3.3.5-dist/css/bootstrap.min.css', '../bootstrap-3.3.5-dist/css/bootstrap-theme.min.css',  '../DataTables-1.10.9/css/dataTables.bootstrap.min.css')
page.addJS('../jQuery-2.1.4/jquery-2.1.4.min.js', '../bootstrap-3.3.5-dist/js/bootstrap.min.js', '../DataTables-1.10.9/js/jquery.dataTables.min.js','../DataTables-1.10.9/js/dataTables.bootstrap.min.js','../my/dadie.js')

#head = page << head()
#<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
#char = head << meta()
#char.attributes['http-equiv'] = 'Content-Type'
#char.attributes['content'] = 'text/html;charset=utf-8'
#char << 'http-equiv="Content-Type" content="text/html;charset=utf-8"'

div0 = page << div(align='center')


#page << hr()
page << h5("妖股最近一月一周大跌情况。最后跟新：" + todayStrFull, align='center')
mydiv1 = page << div(id='myDiv1')
mydiv1.attributes['class'] = 'container'
mydiv2 = mydiv1 << div(id='myDiv2')
mydiv2.attributes['class'] = 'row'

#mydiv2 <<h2('title2 in div2') << p('paragraph under title2')

table1 = mydiv2 << table(border='1',id='mytable3', width='100%')
table1.attributes['class'] = 'table table-bordered table-hover'
thead1 = table1 << thead(id='thead1')
tr1 = thead1 << tr(id='headline')
tr1 << th('代码')
tr1 << th('名字')
tr1 << th('一月涨跌%')
tr1 << th('一周涨跌%')
tr1 << th('昨日涨跌%')
tr1 << th('今日涨幅%')
tr1 << th('最近30交易日涨停数')
tr1 << th('概念')

market_open = 1

tbody1 = table1 << tbody(id='tboday2')
i = 0
for r in all:
    if(i>=showRecord): break
    i += 1

    symbol = r[0]
    inall = r[1]

    name = symbols.getName(symbol)
    zhangfu = 0
    if market_open:
      s,is_close_price = getStock(symbol,todayStr)
      if(is_close_price):
          market_open = 0

      if s is not None:
        zhangfu = s.prev_close_to_close
    else:
      stock_today = stocks.findStockBySymbolAndDate(symbol,todayStr)
      if stock_today:
          zhangfu = stock_today.prev_close_to_close

    month_zhangdie = stocks.getzhangdie(symbol,month_ago,latestDate)
    week_zhangdie = stocks.getzhangdie(symbol,week_ago,latestDate)

    zhangfu_day_ago = 0
    stock_day_ago = stocks.findStockBySymbolAndDate(symbol,day_ago)
    if stock_day_ago:
        zhangfu_day_ago = stock_day_ago.prev_close_to_close

    tr1 = tbody1 << tr(id='line'+str(i))
    link1 = tr1 << td()

    link1 << a(symbol,href="http://stock.jrj.com.cn/share," + str(symbol) + ".shtml")
    #http://stock.jrj.com.cn/share,002292.shtml
    tr1 << td(name)
    tr1 << td("%s" % month_zhangdie)
    tr1 << td("%s" % week_zhangdie)
    tr1 << td("%s" % zhangfu_day_ago)
    tr1 << td("%s" % round(zhangfu,2))
    tr1 << td(inall)
    gainian = concepts.getConceptByStock(symbol)
    tr1 << td(gainian)


f = 'web2/dadie/dadie.html'
fn = re.sub('web2/','',f)
print("%s is generated" %f)
page.printOut(f)
if os.path.exists('web2/content/pages/dadie.html'):
    os.remove('web2/content/pages/dadie.html')
os.symlink('../../' + fn,'web2/content/pages/dadie.html')
