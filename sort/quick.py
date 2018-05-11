def quicksort(A,low,high):
	if low<high:
		q=partition(A,low,high)
		print(q)
		quicksort(A,low,q-1)
		quicksort(A,q+1,high)

def partition(A,low,high):
	x=A[high]
	i=low-1
	for j in range(low,high):
		if A[j]<=x:
			t=A[j]
			A[j]=A[i+1]
			A[i+1]=t
			i=i+1
	l=A[i+1]
	A[i+1]=A[high]
	A[high]=l
	print(A)
	return (i+1)

def main():
	alist = [54,26,93,17,77,31,44,55,20]
	quicksort(alist,0,8)
	print(alist)

if __name__ == '__main__':
	main()