def mergesort(A,low,high):
	print(str(low)+str(high))
	if (low<high):
		mid=int((low+high)/2)
		print(mid)
		mergesort(A,low,mid)
		mergesort(A,mid+1,high)
		merge(A,low,mid,high)

def merge(A,low,mid,high):
	l=0
	r=0
	print(mid)
	L=[0]*(mid)
	R=[0]*(high-mid-1)
	for i in range(low,mid):
		L[l]=A[i]
		l=l+1
	for j in range(mid+1,high):
		R[r]=A[j]
		r=r+1
	l=0
	r=0
	i=low
	print(len(L))
	while((l<=(mid-low+1)) and (r<(high-mid+1))):
		if L[l]>R[r]:
			A[i]=R[r]
			r=r+1
		else:
			A[i]=L[l]
			l=l+1
		i=i+1


def main():
	c=[9,3,5,12,34,23,1,18,56,39,45]
	a=0
	b=len(c)-1
	mergesort(c,a,b)

if __name__ == '__main__':
	main()