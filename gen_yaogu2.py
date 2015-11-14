#coding=utf-8

import os
import re
from  datetime  import  *
from StockDB import *
from Stock import Stock
from pyh import *

stocks = Stocks()
symbols = Symbols()
all_symbols = symbols.getSymbols()

oneWeek = 7
twoWeek = 14
oneMonth = 30
showRecord = 2000
latestDate = stocks.getLatestDate();
latest = stocks.findGreatThan9ForDay(latestDate)
all = stocks.findGreatThan9()
allOneWeek = stocks.findGreatThan9ForLatestDays(oneWeek)
allTwoWeek = stocks.findGreatThan9ForLatestDays(twoWeek)
allOneMonth = stocks.findGreatThan9ForLatestDays(oneMonth)

todayStr = datetime.now().strftime('%Y-%m-%d')
todayStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

title = "最近涨停"

page = PyH(title)
page.addCSS('../bootstrap-3.3.5-dist/css/bootstrap.min.css', '../bootstrap-3.3.5-dist/css/bootstrap-theme.min.css',  '../DataTables-1.10.9/css/dataTables.bootstrap.min.css')
page.addJS('../jQuery-2.1.4/jquery-2.1.4.min.js', '../bootstrap-3.3.5-dist/js/bootstrap.min.js', '../DataTables-1.10.9/js/jquery.dataTables.min.js','../DataTables-1.10.9/js/dataTables.bootstrap.min.js','../my/yaogu.js')

#head = page << head()
#<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
#char = head << meta()
#char.attributes['http-equiv'] = 'Content-Type'
#char.attributes['content'] = 'text/html;charset=utf-8'
#char << 'http-equiv="Content-Type" content="text/html;charset=utf-8"'

div0 = page << div(align='center')


#page << hr()
#page << h5("最后跟新：" + todayStrFull, align='center')
mydiv1 = page << div(id='myDiv1')
mydiv1.attributes['class'] = 'container'
mydiv2 = mydiv1 << div(id='myDiv2')
mydiv2.attributes['class'] = 'row'

#mydiv2 <<h2('title2 in div2') << p('paragraph under title2')

table1 = mydiv2 << table(border='1',id='mytable1', width='100%')
table1.attributes['class'] = 'table table-bordered table-hover'
thead1 = table1 << thead(id='thead1')
tr1 = thead1 << tr(id='headline')
tr1 << th('代码')
tr1 << th('名字')
tr1 << th(latestDate)
tr1 << th('最近1周')
tr1 << th('最近２周')
tr1 << th('最近1月')
tr1 << th('2015')

tbody1 = table1 << tbody(id='tboday1')
i = 0
for r in allOneWeek:
    if(i>=showRecord): break
    i += 1
    symbol = r[0]
    inOneWeek = r[1]

    inTwoWeek = 0
    for r1 in allTwoWeek:
        if(symbol == r1[0]):
            inTwoWeek = r1[1]
            break

    inOneMonth = 0
    for r4 in allOneMonth:
        if(symbol == r4[0]):
            inOneMonth = r4[1]
            break

    inall = 0
    for r2 in all:
        if(symbol == r2[0]):
            inall = r2[1]
            break

    inlatest = 0
    for r3 in latest:
        if(symbol == r3[0]):
            inlatest = r3[1]
            break

    name = symbols.getName(symbol)
    tr1 = tbody1 << tr(id='line'+str(i))
    link1 = tr1 << td()
    link1 << a(symbol,href="http://stock.jrj.com.cn/share," + str(symbol) + ".shtml")
    #http://stock.jrj.com.cn/share,002292.shtml
    tr1 << td(name)
    tr1 << td(inlatest)
    tr1 << td(inOneWeek)
    tr1 << td(inTwoWeek)
    tr1 << td(inOneMonth)
    tr1 << td(inall)

f = 'web2/yaogu/' + todayStr + '.html'
fn = re.sub('web2/','',f)
print("%s is generated" %f)
page.printOut(f)
if os.path.exists('web2/content/pages/yaogu.html'):
    os.remove('web2/content/pages/yaogu.html')
os.symlink('../../' + fn,'web2/content/pages/yaogu.html')
