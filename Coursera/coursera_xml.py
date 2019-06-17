import urllib.request
import xml.etree.ElementTree as ET
sum1=0
url=input()
data = urllib.request.urlopen(url).read()
xml_data=ET.fromstring(data)
lst = xml_data.findall('.//count')
for item in lst:
	sum1+=int(item.text)
print(sum1)
