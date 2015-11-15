#coding=utf-8 
import os
import re
from  datetime  import  *
from StockDB import *
from Stock import Stock
from pyh import *

stocks = Stocks()
symbols = Symbols()

alldata = {}

#shangzheng
shangzheng = stocks.findStocksBySymbol('sh000001') #shangzheng zhishu
for s in shangzheng:
    alldata[s.dateV] = {'shangzheng': s.close}

#zhang die
zhang = stocks.findGreaterCounts(9)
die = stocks.findLessCounts(-9)
for s in zhang:
    num = s[0]
    date = s[1]
    allkeys = alldata.keys()
    if date in allkeys:
        tmp = alldata[date]
        tmp['zhangting'] = num
    else:
        alldata[date] = {'zhangting':num}
for s in die:
    num = s[0]
    date = s[1]
    allkeys = alldata.keys()
    if date in allkeys:
        tmp = alldata[date]
        tmp['dieting'] = num
    else:
        alldata[date] = {'dieting':num}

shangzheng_str = '['
zhangting_str = '['
dieting_str = '['
date_str = '['

prev_shangzheng = 0
for date in sorted(alldata.keys()):
    hash = alldata[date]
    keys = hash.keys()
    if "shangzheng" in keys:
        v = int(hash["shangzheng"] / 2)
        shangzheng_str += str(v ) + ','
        prev_shangzheng = v
    else:
        shangzheng_str += str(prev_shangzheng) + ','
    if "zhangting" in keys:
        zhangting_str += str(hash["zhangting"]) + ','
    else:
        zhangting_str += '0,'
    if "dieting" in keys:
        dieting_str += str(hash["dieting"]) + ','
    else:
        dieting_str += '0,'
    date_str += "'" + date + "',"


shangzheng_str += ']'
zhangting_str += ']'
dieting_str += ']'
date_str += ']'

todayStr = datetime.now().strftime('%Y-%m-%d')
todayStrFull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

title = "涨停趋势"

html = """
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>%s</title>
</head>
<body>
    <div id="myDiv1" class="container"><div id="myDiv2" class="row">
    <div id="main" style="height:400px"></div>
    </div></div>
    <!-- ECharts单文件引入 -->
    <script src="http://echarts.baidu.com/build/dist/echarts.js"></script>
    <script type="text/javascript">
        // 路径配置
        require.config({
            paths: {
                echarts: 'http://echarts.baidu.com/build/dist'
            }
        });

        // 使用
        require(
            [
                'echarts',
                'echarts/chart/line'
            ],
            function (ec) {
                // 基于准备好的dom，初始化echarts图表
                var myChart = ec.init(document.getElementById('main'));

option = {
    title : {
        text: '涨跌股数与大盘',
        subtext: '跟新：%s'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['上证指数','涨停股数','跌停股数']
    },
    calculable : true,
    dataZoom : {
        show : true,
        realtime: true,
        start : 50,
        end : 100
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data: %s,

        }
    ],
    yAxis : [
        {
            type : 'value',
            splitNumber: 15,
        }
    ],
    series : [
        {
            name:'上证指数',
            type:'line',
            data:%s,
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'涨停股数',
            type:'line',
            data:%s,
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'跌停股数',
            type:'line',
            data: %s,
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: '平均值'}
                ]
            }
        }
    ]
};

                // 为echarts对象加载数据
                myChart.setOption(option);
            }
        );
    </script>
</body>
""" % (title,todayStrFull,date_str,shangzheng_str,zhangting_str,dieting_str)


def writeFile(outPath,content):
    file = open(outPath, 'w')
    if file:
        #file.write(content)
        file.writelines(content)
        file.close()
    else:
        print ("Error Opening File.")

filename = 'web2/content/pages/qushi.html'
if os.path.exists(filename):
    os.remove(filename)

writeFile(filename,html)
print(filename)



