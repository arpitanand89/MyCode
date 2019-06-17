import re
read = open('tp.txt')
for i in read:
	i=i.rstrip()
	x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', i)
	if len(x)>0:
		print(x)
