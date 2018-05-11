class graphnode:
	def __init__(self,n):
		self.color='white'
		self.pred=None
		self.ls=[]
		self.key=n
		self.start=0
		self.end=0

class graph:
	def __init__(self,x):
		self.ver=[None] * x
		for i in range(x):
			self.ver[i]=graphnode(i)

	def insert(self,x,y):
		self.ver[x].ls.append(y)
		self.ver[y].ls.append(x)

	def dfs(self,s,time):
		print(self.ver[s].key)
		time=time+1
		self.ver[s].start=time
		self.ver[s].color='grey'
		for v in self.ver[s].ls:
			if self.ver[v].color=='white':
				self.dfs(v,time)
				self.ver[v].pred=self.ver[s]
		self.ver[s].color='black'
		time=time+1
		self.ver[s].end=time

	def printl(self,x):
		for i in range(x):
			print("Vertex"+str(i)+": ",end='')
			#print(' '.join(str(self.ls[i])))
			#for j in range(len(self.ver[i])):
			print(self.ver[i].ls)
	
	def printt(self,n):
		print("Vertex No.     StartTime     EndTime")
		for i in range(n):
			print("Vertex"+str(i)+":"+str(self.ver[i].start)+"          "+str(self.ver[i].end))


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
	t=0
	g.dfs(k,t)
	g.printt(n)	

if __name__ == '__main__':
	main()