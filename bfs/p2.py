class graphnode:
	def __init__(self,n):
		self.name=n
		self.dist=1000
		self.color='white'
		self.adj=list()

class graph:
	def __init__(self):
		self.root=graphnode()

	def bfs(self,x):
		q.list()
		x.dist=0
		x.color='black'
		for v in x.adj:
			self.adj[v].dist=x.dist+1
			q.append(v)

		

