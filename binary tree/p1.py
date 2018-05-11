class TreeNode:
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.left=l
		self.right=r

	def preorder(self):
	    print(self.key)
	    if self.leftChild:
	        self.leftChild.preorder()
	    if self.rightChild:
	        self.rightChild.preorder()


class BinSearchTree:
	def __init__(self):
		self.root=TreeNode()

	def insert(self,x):
		temp=TreeNode()
		temp.key=x
		temp.left=None
		temp.right=None
		if(self.root==None):
			self.root=temp
		else:
			temp2=self.root
			temp3=temp2.parent
			while(temp2!=None):
				temp3=temp2
				if(x>temp2.key):
					temp2=temp2.right
				else:
					temp2=temp2.left
			temp.parent=temp3
			if(temp3.key>x):
				temp3.left=temp
			else:
				temp3.right=temp


	def search(self,k):
		c=0
		temp=self.root
		if(temp==None):
			return None
		while(temp!=None):
			if(temp.key==k):
				print("Key Found")
				c=1
				return temp
			elif(temp.key>k):
				temp=temp.left
			else:
				temp=temp.right
		if(c==0):
			print("Key Not Found")
			

	#def delete(self)


	def minimum(self):
		temp=self.root
		while(temp.left!=None):
			temp=temp.left
		print(temp.key)

	def maximum(self):
		temp=self.root
		while(temp.right!=None):
			temp=temp.right
		print(temp.key)

	def min(self,x):
		temp=x
		while(temp.left!=None):
			temp=temp.left
		return temp

	def max(self,x):
		temp=x
		while(temp.right!=None):
			temp=temp.right
		return temp


	def predecessor(self,y):
		if(y.left!=None):
			return min(y.left)
		temp=y.parent
		while(y!=temp.right and y!=None):
			y=temp
			temp=temp.parent
		return temp

	def successor(self,y):
		if(y.right!=None):
			return min(y.right)
		temp2=y.parent
		while(y!=temp2.left and temp2!=None):
			y=temp2
			temp2=temp2.parent
		return temp2

	"""def delete(self,x):
		if(x.right==None and x.left==None):
			if(x.parent.key>x.key):
				x.parent.left=None
			else:
				x.parent.right=None
		elif(x.left==None or x.right==None):
			if(x.left==None):
				x.parent"""



	"""def pre_traverse(self):
		print(self.key)
		if(temp.left!=None):
			self.left.pre_traverse()
		if(self.right!=None):
			self.right.pre_traverse()"""

	"""def PreOrder(self, root):
        if(self.root != None):
            if(self.root.key!=None):
                print(self.root.key)
                PreOrder(self, self.root.left)
                PreOrder(self, self.root.right)"""


def main():
	t=TreeNode()
	T=BinSearchTree()
	T.insert(10)
	T.insert(5)
	T.insert(3)
	T.insert(7)
	T.insert(12)
	T.insert(15)
	T.insert(11)
	T.insert(17)
	preorder(T.root)
	"""print(T.root.key)
	print(T.root.right.key)
	print(T.root.left.key)"""
	T.search(20)
	T.search(17)
	T.maximum()
	T.minimum()
	s=T.successor(T.root.left.right)
	print(s.key)
	p=T.predecessor(T.root.left.right)
	print(p.key)


if __name__ == '__main__':
	main()