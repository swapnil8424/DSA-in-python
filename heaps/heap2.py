class heap:
	def __init__(self):
		self.h=[]
		self.h.append(0)

	def insert(self,x):
		"""if len(self.h)==0:
			self.h.append(x)
		else:
			l=len(self.h)
			self.h.append(x)
		#heapify(self.h,0)"""
		self.h.append(x)

	def buildheap(self):
		m=len(self.h)
		m=m-1
		#print(m)
		m=int(m/2)
		for i in range(m,0,-1):
			self.heapify(i)
			#print(self.h)


	def heapify(self,x):
		m=len(self.h)
		#print(m)
		#he=height(self.h)
		#if(x>=0)and(x<pow(2,he)):
		#for x in range(0,pow(2,he)):
		temp=self.h[x]
		y=(2*x)
		w=y+1
		if(w<m):
			if(temp<self.h[y] and temp<self.h[w]):
				if(self.h[y]>self.h[w]):
					self.h[x]=self.h[y]
					self.h[y]=temp
					self.heapify(y)
				else:
					self.h[x]=self.h[w]
					self.h[w]=temp
					self.heapify(w)
				return
			elif(temp>self.h[y] and temp<self.h[w]):
				self.h[x]=self.h[w]
				self.h[w]=temp
				self.heapify(w)
				return
			elif(temp<self.h[y] and temp>self.h[w]):
				self.h[x]=self.h[y]
				self.h[y]=temp
				self.heapify(y)
				return
		elif(y<m):
			if(temp<self.h[y]):
				self.h[x]=self.h[y]
				self.h[y]=temp
				self.heapify(y)
			return

			

	def printh(self):
		'''for i in range(1,len(self.h)):
			print(self.h[i])'''
		del self.h[0]
		print(self.h)

	def printheap(self):
		print(self.h)


	def maximum(self):
		return self.h[0]


	def extract_max(self):
		print(self.h[0])
		del self.h[0]
		self.buildheap()


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
	h1.insert(25)
	#h1.heapify(0)
	h1.insert(15)
	h1.insert(1)
	h1.insert(8)
	h1.insert(32)
	#h1.heapify(0)
	#h1.heapify(0)
	h1.buildheap()
	h1.printh()
	print("Maximum element is:")
	print(h1.maximum())
	print("Extracted max")
	h1.extract_max()
	print("Heap after extract_max")
	h1.printheap()



if __name__ == '__main__':
	main()


