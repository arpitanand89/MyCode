# To check if one string is permutation of another.
inp1=list(input('Enter a string: '))
inp2=list(input('Enter another string: '))
if sorted(inp1) == sorted(inp2):
	print ('Strings are a permutation')
else:
	print('Strings are not a permutation')
