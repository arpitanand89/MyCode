import re
op1 = open('tp.txt')
for line in op1:
	line=line.rstrip()
	'''if re.search('^F\S+ \S+@\S+', line):
		print(line)'''
	x=re.findall('^From (\S+@\S+)', line)
	if len(x)>0:
		print(x)
