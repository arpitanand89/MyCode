import requests
from bs4 import BeautifulSoup
def webcrawler(max_pages):
	pval=1
	while pval <= max_pages:
		url = "https://www.olx.in/hyderabad/motorcycles/?page=" + str(pval)   #url1 = "https://www.bigboytoyz.com/suv"  >> other URL
		sourcecode=requests.get(url)   #print(sourcecode) to check the op just in case
		soup = BeautifulSoup(sourcecode.text, features="html.parser")   #plain_text=sourcecode.text >> clarity
		pval+=1
		for link in soup.findAll('a', {'class': 'marginright5 link linkWithHash detailsLink'}):
			href = link.get('href')
			print(link.span.string)
			print(href)
			#crawl_page(href)
			
'''def crawl_page(mapped_url):
	sourcecode1=requests.get(mapped_url)   #print(sourcecode) to check the op just in case
	soup1 = BeautifulSoup(sourcecode1.text, features="html.parser")
	for link1 in soup1.findAll('h1', {'class': 'brkword lheight28'}):
		print(link1.string)
	for urls in soup1.findAll('a'):
		href = urls.get('href')
		print(href)		'''	
	
webcrawler(10)

									
'''for link in soup.findAll('a', {'class': 'carImg'}):										 
    href=link.get("href")
    print(href)
for title in soup.findAll('span', {'class': 'carName'}):
	title1 = title.string
	print(title1)
# , features="html.parser"    '''
