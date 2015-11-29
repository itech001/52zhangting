
#py3
import re
from bs4 import UnicodeDammit
from selenium import webdriver
from xvfbwrapper import Xvfb
from bs4 import BeautifulSoup
try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode

def getHtml(url):
  headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
  req = Request(url,headers=headers)
  try:
     response = urlopen(req)
     html = response.read()
     return html
  except Exception as e:
     print(e.code)
     print(e.read().decode("utf8"))
     return None

def get_unicode_html(html):
        if isinstance(html, str):
            return html
        if not html:
            return html
        converted = UnicodeDammit(html, is_html=True)
        if not converted.unicode_markup:
            raise Exception(
                'Failed to detect encoding of article HTML, tried: %s' %
                ', '.join(converted.tried_encodings))
        html = converted.unicode_markup
        return html

def getHtml2(url):
    try:
        vdisplay = Xvfb()
        vdisplay.start()

        browser = webdriver.Firefox()
        browser.set_page_load_timeout(120)
        browser.get(url)
        return browser.page_source
    except Exception as e:
        print(e)
    finally:
        vdisplay.stop()


def getLinks(url,regex):
    html = getHtml(url)
    html = get_unicode_html(html)
    #regex_new = '"(' + regex + ')"'
    #print('regex:' + regex_new)
    links = re.findall(regex, html)

    return list(set(links))


def getAllByCss(html,css):
    try:
       soup = BeautifulSoup(html, 'html.parser')
       all =soup.select(css)
       if all is None:
           return None
       alltxts = []
       for a in all:
           alltxts.append(a.get_text())
       return alltxts
    except Exception as e:
       print(e)

