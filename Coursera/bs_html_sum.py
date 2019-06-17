import urllib.request
from bs4 import BeautifulSoup
url1="http://py4e-data.dr-chuck.net/comments_88219.html"
sum=0
html1 = urllib.request.urlopen(url1).read()
soup = BeautifulSoup(html1, 'html.parser')
for tags in soup.findAll('span', {'class': 'comments'}):
	sum+=int(tags.text)
print(sum)
		
