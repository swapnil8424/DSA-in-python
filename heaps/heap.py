class heap:
	def __init__(self):
		self.h=[]

	def insert(self,x):
		if len(self.h)==0:
			self.h.append(x)
		else:
			l=len(self.h)
			self.h.append(x)
		#heapify(self.h,0)

	def buildheap(self):
		m=len(self.h)
		m=int(m/2)
		for i in range(m,-1,-1):
			self.heapify(i)


	def heapify(self,x):
		m=len(self.h)
		he=height(self.h)
		#if(x>=0)and(x<pow(2,he)):
		#for x in range(0,pow(2,he)):
		temp=self.h[x]
		y=(2*x)+1
		w=y+1
		if(w<m):
			if(temp<self.h[y] and temp<self.h[w]):
				if(self.h[y]>self.h[w]):
					self.h[x]=self.h[y]
					self.h[y]=temp
				else:
					self.h[x]=self.h[w]
					self.h[w]=temp
			elif(temp>self.h[y] and temp<self.h[w]):
				self.h[x]=self.h[w]
				self.h[w]=temp
			elif(temp<self.h[y] and temp>self.h[w]):
				self.h[x]=self.h[y]
				self.h[y]=temp
		elif(y<m):
			if(temp<self.h[y]):
				self.h[x]=self.h[y]
				self.h[y]=temp

			

	def printh(self):
		print(self.h)	


	def maximum(self):
		return self.h[0]


def height(x):
	n=len(x)
	j=0
	for i in range(1,10):
		if(n-pow(2,i)>0):
			j=j+1
		else:
			return j


def main():
	h1=heap()
	h1.insert(4)
	h1.insert(6)
	h1.insert(2)
	h1.insert(20)
	h1.insert(16)
	h1.insert(12)
	#h1.heapify(0)
	h1.insert(10)
	#h1.heapify(0)
	h1.insert(8)
	#h1.heapify(0)
	h1.insert(15)
	#h1.heapify(0)
	#h1.heapify(0)
	h1.buildheap()
	h1.printh()
	print(h1.maximum())


if __name__ == '__main__':
	main()


