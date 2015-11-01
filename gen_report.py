from  datetime  import  *
from StockDB import *
from Stock import Stock
from pyh import *

stocks = Stocks()
symbols = Symbols()
all_symbols = symbols.getSymbols()

latestDay = 14
showRecord = 100
all = stocks.findGreatThan9()
allIn7Days = stocks.findGreatThan9ForLatest(latestDay)

page = PyH("MyPage")
page.addCSS('../bootstrap-3.3.5-dist/css/bootstrap.css', '../bootstrap-3.3.5-dist/css/bootstrap-theme.css', 'bootstrap-3.3.5-dist/css/bootstrap-theme.css.map', '../DataTables-1.10.9/css/dataTables.bootstrap.css', '../Scroller-1.3.0/css/scroller.bootstrap.css', '../Select-1.0.1/css/select.bootstrap.css')
page.addJS('../jQuery-2.1.4/jquery-2.1.4.js', '../bootstrap-3.3.5-dist/js/bootstrap.js', '../DataTables-1.10.9/js/jquery.dataTables.js','../DataTables-1.10.9/js/dataTables.bootstrap.js','../Scroller-1.3.0/js/dataTables.scroller.js','../Select-1.0.1/js/dataTables.select.js','../my/my.js')

#head = page << head()
#<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
#char = head << meta()
#char.attributes['http-equiv'] = 'Content-Type'
#char.attributes['content'] = 'text/html;charset=utf-8'
#char << 'http-equiv="Content-Type" content="text/html;charset=utf-8"'

todayStr = datetime.now().strftime('%Y-%m-%d')
page << h1('妖股 -' + todayStr,align='center')
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
tr1 << th('最近')
tr1 << th('所有')

tbody1 = table1 << tbody(id='tboday1')
i = 0
for r in allIn7Days:
    if(i>=showRecord): break
    i += 1
    symbol = r[0]
    in7days = r[1]
    inall = 0
    for r2 in all:
        if(symbol == r2[0]):
            inall = r2[1]
            break
    name = symbols.getName(symbol)
    tr1 = tbody1 << tr(id='line'+str(i))
    tr1 << td(symbol)
    tr1 << td(name)
    tr1 << td(in7days)
    tr1 << td(inall)

page << hr()
page << h5('www.52zhangting.com, qq群：513656027',align='center')

f = 'web/yaogu/' + todayStr + '.html'
print("The file %s is generated" %f)
page.printOut(f)
