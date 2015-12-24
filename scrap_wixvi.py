import re
import requests
from bs4 import BeautifulSoup
url="http://wixvi.cc/"
r = requests.get(url)
soup = BeautifulSoup(r.content)
g_data=soup.find_all("div", {"class":"data"})

for i in g_data:
    print i.contents[1].text,":"
    print i.contents[5].contents[0].text," ",
    print i.contents[5].contents[1].text," ",
    print i.contents[5].contents[2].text," ",
    print i.contents[3].contents[3].text
    print
    print 
    
