# stock_scraper
Get stock quotes from Google.

import urllib
import re
import ezodf

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    if m:
        quote = m.group(2)
    else:
        quote = 'no quote available for: ' + symbol
    return quote

TRMB = eval(get_quote('trmb'))
print 'TRMB:', TRMB
FB = eval(get_quote('fb'))
print 'FB  :', FB
CAT = eval(get_quote('cat'))
print 'CAT :',CAT
GOOG = eval(get_quote('goog'))
print 'GOOG:',GOOG
AMZN = eval(get_quote('amzn'))
print 'AMZN:',AMZN
GRMN = eval(get_quote('grmn'))
print 'GRMN:',GRMN
EBAY = eval(get_quote('ebay'))
print 'EBAY:',EBAY
AAPL = eval(get_quote('aapl'))
print 'AAPL:',AAPL
IWO = eval(get_quote('iwo'))
print 'IWO :',IWO
DIA = eval(get_quote('dia'))
print 'DIA :',DIA
LNKD = eval(get_quote('lnkd'))
print 'LNKD:', LNKD
WFC = eval(get_quote('WFC'))
print 'WFC :' ,WFC
                
stock = ezodf.opendoc("valuation.ods")
sheet = stock.sheets[0]
sheet['J3'].set_value(TRMB,currency='USD')
sheet['J4'].set_value(AAPL,currency='USD')
sheet['J5'].set_value(AMZN,currency='USD')
sheet['J6'].set_value(FB,currency='USD')
sheet['J7'].set_value(CAT,currency='USD')
sheet['J8'].set_value(GRMN,currency='USD')
sheet['J9'].set_value(GOOG,currency='USD')
sheet['J10'].set_value(EBAY,currency='USD')
sheet['J11'].set_value(DIA,currency='USD')
sheet['j24'].set_value(LNKD,currency='USD')
sheet['j28'].set_value(WFC,currency='USD')
stock.save()            
