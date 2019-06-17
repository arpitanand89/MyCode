''''Problem Statement:
Assume you have a method isSubstring() which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring().
 
Example:
stringRotation("waterbottle", "erbottlewat") '''

s1 = input('Enter string1: ')
s2 = input('Enter string2: ')
lst = list()
def issubstring(str1, str2):
	if str1==str2:					   # if strings are same
		print('S2 is a substing of S1')
	elif sorted(str1) == sorted(str2):	#if all character in string are same
		i=1
		while i < len(str2):
			word = str2[i:]+str2[0:i]  # This gives all jumble word combinations of s2
			lst.append(word)
			i+=1
		if str1 in lst:
			print('S2 is a substing of S1')
		else:
			print('S2 is not a substring of s1')
	
	else:
		print('S2 is not a substring of s1')

issubstring(s1, s2)
	
