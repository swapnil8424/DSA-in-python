class queue:
	def __init__(self):
		self.qu=[]

	def enqueue(self,x):
		self.qu.append(x)
		#print(self.qu)

	def dequeue(self):
		#print(self.qu)
		return self.qu.pop(0)

	def isEmpty(self):
		return self.qu==[]

class ListNode:
	def __init__(self,x):
		self.key=x
		self.next=None

class linkedlist:
	def __init__(self):
		self.head=None

	def insertl(self,a):
		temp=ListNode(a)
		if self.head==None:
			self.head=temp
		else:
			temp1=self.head
			while(temp1.next!=None):
				temp1=temp1.next
			temp1.next=temp


class graphnode:
	def __init__(self,b):
		self.key=b
		self.ls=linkedlist()
		self.color='white'

class graph:
	def __init__(self,n):
		self.ver=[None]*n
		for i in range(n):
			self.ver[i]=graphnode(i)

	def insert(self,a,b):
		self.ver[a].ls.insertl(b)

	def printl(self,n):
		for i in range(n):
			print("Vertex "+str(i)+": ",end=' ')
			temp=self.ver[i].ls.head
			while(temp!=None):
				print(temp.key,end=' ')
				temp=temp.next
			print()

	def isCycle(self,s):
		t=0
		d=queue()
		e=queue()
		print(self.ver[s].key)
		self.ver[s].color='black'
		d.enqueue(self.ver[s])
		#print(d)
		e.enqueue(self.ver[s].key)
		u=d.dequeue()
		#print(u)
		#print(u.key)
		temp=self.ver[s].ls.head
		while(temp!=None):
			if (self.ver[temp.key].color=='white'):
				self.ver[temp.key].color='black'
				t=t+1
				d.enqueue(self.ver[temp.key])
				e.enqueue(self.ver[temp.key].key)
				u=d.dequeue()
				temp=self.ver[u.key].ls.head
			if t>2:
				temp1=temp
				while(temp1.next!=None):
					if self.ver[temp1.key].color=='black':
						e.enqueue(self.ver[temp1.key].key)
						print("Cycle Detected")
						break
					else:
						temp1=temp1.next






def main():
	print("Enter the number of vertices")
	n=int(input())
	g=graph(n)
	print("Enter the number of edges")
	m=int(input())
	print("Enter the edges")
	for i in range(m):
		a,b=map(int,input().strip().split(" "))
		g.insert(a,b)
	g.printl(n)
	g.isCycle(0)


if __name__ == '__main__':
	main()