import urllib.request
from bs4 import BeautifulSoup
url1="http://py4e-data.dr-chuck.net/known_by_Cormac.html"
count=7
position=18
i=1
j=1
while j <= count:
	html1 = urllib.request.urlopen(url1).read()
	soup = BeautifulSoup(html1, 'html.parser')
	tags = soup('a')
	for tag in tags:
		if i==position:
			url1=tag.get('href')
			i+=1
		else:
			i+=1
	i=1
	j+=1
html2 = urllib.request.urlopen(url1).read()
soup1 = BeautifulSoup(html2, 'html.parser')
tags1 = soup('a')
for t in tags1:
	if i==position:
		print(t.text)
		i+=1
	else:
		i+=1

	
		

	
		

