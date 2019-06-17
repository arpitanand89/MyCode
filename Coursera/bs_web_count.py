import requests
from bs4 import BeautifulSoup
url = "http://py4e-data.dr-chuck.net/comments_42.html"
sum1 = 0
sourcecode=requests.get(url)   #print(sourcecode) to check the op just in case
soup = BeautifulSoup(sourcecode.text, features="html.parser")   #plain_text=sourcecode.text >> clarity
for link in soup.findAll('span', {'class': 'comments'}):
	#num = link.get('span.string')
	print(link)


