#coding=utf-8 
import os
import re
from  datetime  import  *
from StockDB import *
from Stock import Stock
from pyh import *

stocks = Stocks()
symbols = Symbols()

zhang = stocks.findGreaterCounts(0.09)
die = stocks.findLessCounts(-0.09)
num = len(zhang)
num1 = len(die)
if num1 > num:
    max = num1
else:
    max = num

zhang_str = '['
die_str = '['
date_str = '['
i = 0
j = 0
while(i < max):
  if j >= num1:
      zhang_str += str(zhang[i][0]) + ','
      die_str += '0' + ','
      date_str = date_str + "'" + str(zhang[i][1]) + "',"
      print(str(zhang[i][1]) + 'zhang:' + str(zhang[i][0]) + 'die:0')
      i += 1
  elif i >= num:
      die_str += str(die[j][0]) + ','
      zhang_str += '0' + ','
      date_str = date_str + "'" + str(die[j][1]) + "',"
      print(str(die[j][1]))
      j += 1
  elif zhang[i][1] == die[j][1]:
      zhang_str += str(zhang[i][0]) + ','
      die_str += str(die[j][0]) + ','
      date_str = date_str + "'" + str(zhang[i][1]) + "',"
      print(str(zhang[i][1]) + 'zhang:' + str(zhang[i][0]) + 'die:' + str(die[j][0]))
      i += 1
      j += 1
  elif zhang[i][1] < die[j][1]:
      zhang_str += str(zhang[j][0]) + ','
      die_str += '0' + ','
      date_str = date_str + "'" + str(zhang[i][1]) + "',"
      print(str(zhang[i][1]))
      i += 1

  else:
      die_str += str(die[j][0]) + ','
      zhang_str += '0' + ','
      date_str = date_str + "'" + str(die[j][1]) + "',"
      print(str(die[j][1]))
      j += 1


  print("i %i, j %i" % (i,j))

zhang_str += ']'
die_str += ']'
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
        data:['涨停股数','跌停股数']
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
        }
    ],
    series : [
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
""" % (title,todayStrFull,date_str,zhang_str,die_str)


def writeFile(outPath,content):
    file = open(outPath, 'w')
    if file:
        #file.write(content)
        file.writelines(content)
        file.close()
    else:
        print ("Error Opening File.")

if os.path.exists('web2/content/pages/qushi.html'):
    os.remove('web2/content/pages/qushi.html')

writeFile('web2/content/pages/qushi.html',html)



