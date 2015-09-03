#coding:utf-8
__author__ = 'yangh'
import requests
from bs4 import BeautifulSoup
import re
import urllib
DownPath = "F:\\pic\\"
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5
PhotoName = 0
c = '.jpg'
PWD="F:\\pic\\"
with open('url.txt', 'rb') as url:
    for site in url.readlines():
        site = site.strip('\r\n')
        Page = requests.session().get(site,headers=head,timeout=TimeOut)
        Coding =  (Page.encoding)
        Content = Page.content#.decode(Coding).encode('utf-8')
        ContentSoup = BeautifulSoup(Content)
        count = ContentSoup.find_all('br')
        lmt = len(count)
        jpg = ContentSoup.find_all('img',limit = lmt)
        for photo in jpg:
          PhotoAdd = photo.get('src')
          PhotoName +=1
          Name =  (str(PhotoName)+c)
          r = requests.get(PhotoAdd,stream=True)
          with open(PWD+Name, 'wb') as fd:
              for chunk in r.iter_content():
                      fd.write(chunk)
print ("%d photos download" %PhotoName)
