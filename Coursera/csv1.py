import random
from urllib import request
#url1="https://query1.finance.yahoo.com/v7/finance/download/GOOGL?period1=1545040154&period2=1547718554&interval=1d&events=history&crumb=skDVAQ5G3az"
url1="https://sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv"
def download_csv(url):
	response = request.urlopen(url)
	csv = response.read()
	str_csv = str(csv)
	lines = str_csv.split("\\n")
	dst_url = r'google.csv'
	fx = open(dst_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()
		
download_csv(url1)
