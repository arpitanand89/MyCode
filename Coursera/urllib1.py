import urllib.request
fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
dict1 = dict()
for line in fhand:
	words=line.decode().split()
	print(words)
	for word in words:
		dict1[word]=dict1.get(word, 0) + 1

print(dict1)
