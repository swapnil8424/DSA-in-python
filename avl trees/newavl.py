class TreeNode:
	def __init__(self,k=None,,p=None,l=None,r=None,h=0):
		self.key=k
		self.parent=p
		self.left=l
		self.right=r
		self.height=h

class AvlTree:
	def __init__(self):
		self.root=TreeNode()


	def insert(self,x):
		temp=TreeNode()
		temp.left=None
		temp.right=None
		temp.parent=None
		temp.height=0
		temp.key=x
		if(self.root==None):
			self.root=temp
		else:
			temp2=self.root
			temp3=TreeNode()
			ancestors=[]
			while(temp2):
				temp3=temp2
				ancestors.append(temp3)
				if(x>temp2.key):
					temp2=temp2.right
				else:
					temp2=temp2.left
			temp.parent=temp3
			temp2=temp
			if(x>temp3.key):
				temp3.right=temp
			else:
				temp3.left=temp
