'''Fibonacci 0 1 1 2 3 5 8 13 21 34  55
			 0 1 2 3 4 5 6  7  8  9  10  '''

inp = int(input('Enter a num: '))
def fibonacci(inp1):
	if inp1 == 0:
		return 0
	elif inp1 == 1:
		return 1
	else:
		return (fibonacci(inp1-2)+ fibonacci(inp1-1))

for i in range(0, inp+1):
	print(fibonacci(i), end=" ")
			
	
		
		
		

	
