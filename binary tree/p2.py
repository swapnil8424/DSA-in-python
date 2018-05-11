class TreeNode:
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.left=l
		self.right=r

def preorder(self):
    if(self==None):
    	return
    else:
    	print(self.key)
    	preorder(self.left)
    	preorder(self.right)


class BinSearchTree:
	def __init__(self):
		self.root=None

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

	def delete(self,x):
		if(x.right==None and x.left==None):
			if(x.parent.key>x.key):
				x.parent.left=None
			else:
				x.parent.right=None
		elif(x.left==None or x.right==None):
			if(x.left==None):
				x.right.parent=x.parent
				x.parent=None
				x.right=None
			else:
				x.left.parent=x.parent
				x.parent=None
				x.left=None
		else:
			y=self.predecessor(x)
			x.value=y.value
			self.delete(y)



	"""def pre_traverse(self):
		temp=self.root
		while(temp.left!=None):
			print(temp.left.key)
			temp=temp.left
	"""

def main():
	T=BinSearchTree()
	T.insert(10)
	T.insert(5)
	T.insert(3)
	T.insert(7)
	T.insert(12)
	T.insert(15)
	T.insert(11)
	T.insert(17)
	"""print(T.root.key)
	print(T.root.right.key)
	print(T.root.left.key)"""
	T.search(20)
	T.search(17)
	T.maximum()
	T.minimum()
	print("Preorder traversal of tree")
	preorder(T.root)
	T.delete(T.root.left.left)
	T.delete(T.root.right.right)
	print("Deleting 3 and 17")
	preorder(T.root)
	print("Successor of 7")
	s=T.successor(T.root.left.right)
	print(s.key)
	print("Predecessor of 7")
	p=T.predecessor(T.root.left.right)
	print(p.key)


if __name__ == '__main__':
	main()

