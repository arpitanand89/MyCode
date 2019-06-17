fname = input('Enter name of the file: ')
fh=open(fname, 'r')
#alpha = fh.read()
#print(alpha.upper())
dic = dict()
names = list()
bigname=None
bigcount=0
for line in fh:
	if line.startswith('From '):
		l1=line.split()
		names.append(l1[1])
		#print(names)
for name in names:
	dic[name]=dic.get(name, 0)+1
		#print(dic[name])
for keys, value in dic.items():
	if bigcount<value:
		bigcount= value
		bigname=keys
print(bigname, bigcount)
	
	


	
 
