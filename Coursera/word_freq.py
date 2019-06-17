import requests
from bs4 import BeautifulSoup
import operator
lst =list()
dict1=dict()
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
url='https://www.olx.in/hyderabad/motorcycles/'
data = requests.get(url)
soup = BeautifulSoup(data.text, features="html.parser")
#print(soup)
#for link in soup.findAll('a', {'class': 'marginright5 link linkWithHash detailsLink'}):
for link in soup.findAll('div', {'class': 'IKo3'}):	
	print(link)
	l=link.span.string.split()
	print(l)
	for l1 in l:
		lst.append(l1)
		print(lst)
		'''for c1 in lst:
			if chars in c1:
				c1.replace(chars,"") '''

#print(lst) 


