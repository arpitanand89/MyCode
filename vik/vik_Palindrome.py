''' Problem Statement:
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or
phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does
not need to be limited to just dictionary words.
 
Example:
"tact coa" -> True (permutations: "tacocat", "atcocta", etc.) '''

str1=str(input('Enter a string: '))
str_op=""
splt_str=str1.split()
for i in splt_str:
	str_op+=i
set1=set(str_op)
if len(set1) <= int((len(str_op)/2)+1):     
	print('String is a Palindrome')
else:
	print('String is not a Palindrome')
