import urllib.request
import json
sum1=0
i=0
url=input("")
data = urllib.request.urlopen(url).read()
js = json.loads(data)
while i<(len(js["comments"])):
	sum1+=(js["comments"][i]["count"])
	i+=1
print(sum1)

