# Binary search operation recursively

def binary_search(A, key, low, high):
	mid = (low+high)//2
	while low <= high:
		if key == A[mid]:
			return True
		elif key < A[mid]:
			return binary_search(A, key, low, mid-1)
		else:
			return binary_search(A, key, mid+1, high)
	return False
	
A = [15, 21, 33, 47, 61]
aa = binary_search(A, 62, 0, 4)
print(aa)
		
