import random
from urllib import request
def download_csv(url):
	name = "sample.csv"
	request.urlretrieve(url, name)
	
download_csv("https://sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv")
	
