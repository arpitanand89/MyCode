import re
sum1 = 0
op = open('regex_sum_88217.txt')
for line in op:
	line = line.rstrip()
	x=re.findall('[0-9]+',line)
	if len(x)>0:
		for y in x:
			sum1+=int(y)
print(sum1)
