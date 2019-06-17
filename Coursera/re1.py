import re
op = open('tp.txt')
#print (op)
for line in op:
	if re.search('^F.', line):
		print(line)

