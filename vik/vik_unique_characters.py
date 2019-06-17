#implememt an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures.
import sys
ip = input('Enter a string: ')
for char in ip:
	cnt=(ip.count(char))
	if cnt > 1:
		print('Characters are not unique')
		exit()
print('All characters are unique')
