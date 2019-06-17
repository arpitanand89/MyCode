'''Problem Statement:
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
 
Example:
[1,2,3,       [7,4,1,
 4,5,6,   ->   8,5,2,
 7,8,9]        9,6,3]'''
 
import numpy as np
a=0
b=0
x=np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
z=len(x)
y=np.empty((z,z)).astype('int') # create an empty matrix
while a<z:	
	b=0
	c=z-1
	while c>=0:
		y[a][b]=x[c][a]
		b+=1
		c-=1
	a+=1
print(y)
