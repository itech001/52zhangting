import re
from HtmlCommon import *
from StockDB import Concepts

c = Concepts()

def getJrjConcept():
  jrj = 'http://stock.jrj.com.cn/concept/conceptpage.shtml'
  regex = '<a href="(http://stock.jrj.com.cn/concept/conceptdetail/conceptDetail_(.+)\.shtml)".*>(.*)</a>'
  #regex = '(http://stock.jrj.com.cn/concept/conceptdetail/conceptDetail_.+\.shtml).+\>(.+?)\<'
  lists = getLinks(jrj,regex)
  stock_hash = {}
  for l in lists:
      url = l[0]
      concept = l[1]
      name = l[2]
      name = name.replace('概念股', '')
      if c.getConcept(concept):
          print(concept + 'is existed')
          continue
      stocks = getJrjConceptStocks(url)
      if stocks is None:
          continue
      stocks_str = ''
      for s in stocks:
          if stocks_str == '':
              stocks_str = s
          else:
              stocks_str += ',' + s
      c.insertConcept(concept,name,url,stocks_str)


def getJrjConceptStocks(url):
    html = getHtml2(url)
    if html is None or html == '':
        return None
    html = get_unicode_html(html)
    css ='#stockTbody > tr > td:nth-of-type(2) > a'
    xpath = '//*[@id="stockTbody"]/tr/td[2]'
    stocks = getAllByCss(html,css)
    return stocks


getJrjConcept()
print('concepts table updated')
#getJrjConceptStocks('http://stock.jrj.com.cn/concept/conceptdetail/conceptDetail_wrj.shtml')
