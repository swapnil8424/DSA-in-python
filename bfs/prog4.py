class queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        return self.arr.pop(0)

    def isEmpty(self):
        return self.arr == []


class graphnode:
	def __init__(self,n):
		self.key=n
		self.color='white'
		self.dist=1000
		self.ls=[]
		self.pred=None


class graph:
	def __init__(self,x):
		self.ver=[None] * x
		for i in range(x):
			self.ver[i]=graphnode(i)

	def insert(self,x,y):
		self.ver[x].ls.append(y)
		self.ver[y].ls.append(x)

	"""def printm(self,x):
		for i in range(x):
			for j in range(x):
				print(self.matrix[i][j],end=' ')
			print()"""

	def bfs(self,s):
		self.ver[s].dist=0
		self.ver[s].color='black'
		q=queue()
		q.enqueue(self.ver[s])
		print("vertex distance")
		while(not q.isEmpty()):
			u=q.dequeue()
			print(str(u.key)+"        "+str(u.dist))
			for v in self.ver[u.key].ls:
				if self.ver[v].color=='white':
					self.ver[v].dist=u.dist+1
					self.ver[v].color='black'
					self.ver[v].pred=u
					q.enqueue(self.ver[v])
	


	def printl(self,x):
		for i in range(x):
			print("Vertex"+str(i)+": ",end='')
			#print(' '.join(str(self.ls[i])))
			#for j in range(len(self.ver[i])):
			print(self.ver[i].ls)

	def isCycle(self):
		for i in range(len(self.ver)):
			for j in range(len(self.ver[i].ls)):
				if(self.ver[i].ls[j])


def main():
	print("Enter the number of vertices:")
	n=int(input())
	g=graph(n)
	print("Enter the number of edges:")
	a=int(input())
	print("Enter the edges:")
	for i in range(a):
		l,m = map(int,input().strip().split(" "))
		g.insert(l,m)
	print("The adjacency list is:")
	#g.printm(n)
	g.printl(n)
	#print("Complete list")
	#g.pr()
	print("Enter the source vertex")
	k=int(input())
	g.bfs(k)

if __name__ == '__main__':
	main()
