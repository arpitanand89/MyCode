# Factorial
'''inp_num = int(input('Enter a number to find a factorial: '))
out = 1
while inp_num > 1:
	out*=inp_num
	inp_num-=1
print(out)'''


inp = int(input('Enter a number to find a factorial: '))
def fact(inp1):
	if inp1 == 0:
		return 1
	else:
		return inp1*fact(inp1-1)     # return 5*fact(4) >> 5*4*fact(3) and so on
aa = fact(inp)
print(aa)
