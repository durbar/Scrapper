import re
import requests
from bs4 import BeautifulSoup



def add_pageNO(a, keywords='hot+lesbians'):
    url="http://www.xvideos.com/?k=" + keywords
    url+='&p='+str(a)
    return url



print "PELASE ENTER KEYWORDS FOR SEARCH"

keywords = 'mia+malkova'

print "enter no of pages you want to browse"

pages = int(raw_input())

for page in range(pages):
    print "Page: ",page + 1
    url=add_pageNO(page, keywords)
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    g_data=soup.find_all("div", {'class':'thumb-inside'})
    #print g_data
    
    for i in g_data:
    
        k= i.contents[0].text
        k=str(k)
        k=k.split('/')
        vi=re.findall('(.+)?">',k[2])
        print str(vi)[1:-1]
    print '\n\nEND OF PAGE ',page+1
    print '--------------x-----------\n\n'

