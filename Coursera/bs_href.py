import urllib.request
from bs4 import BeautifulSoup
url=("http://www.dr-chuck.com/page1.htm")
url1=("http://dr-chuck.com/")
http1 = urllib.request.urlopen(url1).read()
soup = BeautifulSoup(http1, 'html.parser')
tags = soup('a')
for tag in tags:
	aa=tag.get('href', None)
	print(aa)
