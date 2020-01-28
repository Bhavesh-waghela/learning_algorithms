A = [-2,3,2,-1]

def kadane(A)
	max_current = max_global = A[0]
	for i from 1 to length(A)-1:
		max_current = max(A[i], max_current + A[i])
		if max_current > max_global
			max_global = max_current
	return max_global