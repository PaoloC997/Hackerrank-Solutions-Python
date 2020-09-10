
# Insertion Sort


def insertion_sort(A):
	

	for i in range(1, len(A)):
		for j in range( i -1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1],A[j]
			else:
				break;
				
	return A			


print(insertion_sort([5,45,34,1,4,3,2]))


# With a while loop


def insertion_sort2(A):

	for i in range(1, len(A)):
		j = i -1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1],A[j]
			j -= 1
				
	return A			



print(insertion_sort([6,45,34,1,4,3,2]))


# Shifting Method


def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		for j in range (i -1, -1, -1):
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				A[j + 1] = curNum
				break;
	return A	

print(insertion_sort3([5,9,10,7,8]))


