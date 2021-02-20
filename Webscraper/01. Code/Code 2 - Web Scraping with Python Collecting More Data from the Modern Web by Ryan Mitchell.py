# Chapter 1
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

#########
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)

##########
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    #return null, break, or do some other plan b
except URLError as e:
    print('The server could not be found')
else:
    print('it worked')
    
##############################
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
print(bs)
name_list = bs.findAll('span', {'class':'green'})
for name in name_list:
    print(name.get_text())
    
nameList = bs.find_all(text='the prince')
print(len(nameList))
title = bs.find_all(id='title', class_='text')
title = bs.find(id='title')

# page 41

