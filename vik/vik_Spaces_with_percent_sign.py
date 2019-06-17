''' Problem Statement:
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the
"true" length of the string.
 
Example:
'Mr. John Smith' -> 'Mr.%20John%20Smith%20'  

str1 = str(input('Enter a string: '))
if str1.endswith(" "):
	print(str1.replace(" ", "%20"))
else:
	print(str1.replace(" ", "%20") + "%20" )   '''
	
	
str1 = str(input('Enter a string: '))
output= ""
splt = str1.split()
for i in splt:
	output += i + "%20"
print(output) 





