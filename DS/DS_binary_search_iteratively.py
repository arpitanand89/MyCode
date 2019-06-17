# Binary search operation iteratively
def binary_search(A, key):
	low = 0
	high = len(A)-1
	while low <= high:
		mid = (low+high)//2
		if key == A[mid]:
			return True
		elif key < A[mid]:
			high = mid-1
		else:
			low = mid+1
	return False

A = [5, 10, 15, 20, 25] 
aa = binary_search(A, 10)
print(aa)
			

