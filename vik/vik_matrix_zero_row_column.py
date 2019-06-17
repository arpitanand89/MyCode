'''Problxem Statement:
Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column are set to 0.
 
Example:
[1, 2, 0, 4,      [0, 0, 0, 0,
 1, 2, 3, 4,  ->   0, 2, 0, 4,
 0, 2, 3, 4]       0, 0, 0, 0]'''

# without using numpy
x = ([[1, 2, 0, 4],[1, 2, 3, 4],[0, 2, 3, 4]])
y = ([[1, 2, 0, 4],[1, 2, 3, 4],[0, 2, 3, 4]])
r = len(x) # count of rows
c = len(x[0]) # count of columns
for i in range(r):  # Loop to set '0' in rows 
	if (0 in x[i]): # check if there is a zero in a row 
		for j in range(c):
			y[i][j] = 0   # Set row as 0
for k in range(c): # Loop to set '0' in colums
	l = 0
	while l<r:						# wh
		if (x[l][k] == 0):          # check if value in a column is zero
			for m in range(len(x)):
				y[m][k] = 0         # Set all Columns as '0' 
		l+=1						# increment length of row	
print(y)


# by using numpy

import numpy as np
x = np.array([[1, 2, 0, 4],[1, 2, 3, 4],[0, 2, 3, 4]]) # Assign array to a variable
y = np.array([[1, 2, 0, 4],[1, 2, 3, 4],[0, 2, 3, 4]]) # creating a duplicate array
r = len(x) # length of row
c = len(x[0]) # length of column
for i in range(r):  # Loop to set '0' in rows 
	if (0 in x[i]):
		y[i] = 0    # Set row as 0
for j in range(c): # Loop to set '0' in colums
	if (0 in x[:, j]):
		y[:, j] = 0 # Set Column as 0 

print(y)
