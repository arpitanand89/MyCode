''' There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
 
Example:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false   '''

def str_fun():

	s1=str(input('Enter string 1: '))
	s2=str(input('Enter string 2: '))
	if s1==s2:                                      # If strings are same
		print('The strings are same')
		exit()
	j=0
	if (abs(len(s1)-len(s2)) == 0 or abs(len(s1)-len(s2))== 1):
		l1=list(s1)
		l2=list(s2)
		if len(l1)>len(l2):							#If length of s1>s2
			for k in range(len(l2)):
				if l2[k]==l1[k] or l2[k]==l1[k+1]:
					j+=1
			if j==len(l2):
					print('Strings are an edit away')
			else:
					print('Strings are not an edit away')			
		elif len(l1)<len(l2):
			for k in range(len(l1)):				#If length of s1<s2
				if l1[k]==l2[k] or l1[k]==l2[k+1]:
					j+=1
			if j==len(l1):
					print('Strings are an edit away')
			else:
					print('Strings are not an edit away')
		elif len(l1)==len(l2):						#If length of s1=s2
			for k in range(len(l1)):
				if l1[k]==l2[k]:
					j+=1
			if j==len(l1)-1:
					print('Strings are an edit away')
			else:
					print('Strings are not an edit away')
	else:
		print('The strings are not an edit away')
		
str_fun()

