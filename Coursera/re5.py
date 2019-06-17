import re
op2 = open('tp.txt')
for line in op2:
	z = re.findall('@([^ ]*)', line)
	if len(z)>0:
		print(z)
