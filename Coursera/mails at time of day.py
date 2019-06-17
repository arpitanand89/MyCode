fname=input('Enter a filename: ')
fh=open(fname, 'r')
lst=list()
dic=dict()
for line in fh:
	if line.startswith('From '):
		l1=line.split()
		l2=l1[5].split(":")
		#print(l2)
		lst.append(l2[0])
for m1 in lst:
	dic[m1]=dic.get(m1,0)+1
tup=sorted(dic.items())
for k,v in tup:
	print(k,v)
		
		
	
