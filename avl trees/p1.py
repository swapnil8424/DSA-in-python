class TreeNode:
	def __init__(self,p=None,k=None,l=None,r=None,h=0):
		self.parent=p
		self.key=k
		self.left=l
		self.right=r
		self.height=h

def heightnode(self):                              
	h=1
	temp=TreeNode()
	while(temp):												
		if(temp.left!=None):
			h=h+1
			temp=temp.left
		elif(temp.right!=None):
			temp=temp.right
			h=h+1
		else:
			return h

"""def height(self):
	temp=self
	h=0
	while(temp):
		if(temp.right==None and temp.left==None):
			return h
		else:
			h=h+1
			if(temp.right==None):
				temp=temp.left
			else:
				temp=temp.right"""


def preorder(self):
    if(self==None):
    	return
    else:
    	print(self.key)
    	preorder(self.left)
    	preorder(self.right)

class avlTree:
	def __init__(self):
		self.root=None

	def insert(self,x):
		temp=TreeNode()
		temp3=TreeNode()
		ancestor=[]
		temp.key=x
		temp.left=None
		temp.right=None
		if(self.root==None):
			self.root=temp
		else:
			temp2=self.root
			temp3=temp2.parent
			while(temp2!=None):
				ancestor.append(temp3)
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
		temp.height=heightnode(temp)
		while(temp.parent!=None):
			print(temp.parent.key,end=" ")
			h1=heightnode(temp.parent.left)
			print(h1,end=" ")
			h2=heightnode(temp.parent.right)
			print(h2)
			if(abs(h1-h2)>1):
				print("Yes")
				z=temp.parent
				print(z.key)
				if(z.left in ancestor):
					y=z.left
				else:
					y=z.right
				print(y.key)
				if(y.left in ancestor):
					x=y.left
				else:
					x=y.right
				print(x.key)
				if(y==z.left and x==y.left):
					y.parent=None
					z.parent=y
					z.left=y.right
					y.right.parent=z
					y.right=z
				elif(y==z.right and x==y.right):
					y.parent=None
					z.parent=y
					y.left.parent=z
					z.right=y.left
					y.left=z
				elif(y==z.left and x==y.right):
					x.parent=z
					y.parent=x
					y.right=x.left
					x.left.parent=y
					x.parent=None
					z.parent=x
					z.left=x.right
					x.right.parent=z
					x.right=z
				else:
					x.parent=z
					y.parent=x
					y.left=x.right
					x.right.parent=y
					x.parent=None
					x.left=z
					z.parent=x
					z.right==x.left
					x.left.parent=z
					x.left=z
				break	
			else:
				temp=temp.parent

def main():
	T=avlTree()
	T.insert(10)
	s=heightnode(T.root)
	print(s)
	T.insert(5)
	T.insert(12)
	T.insert(7)
	T.insert(3)
	T.insert(9)
	#T.insert(11)
	#T.insert(17)
	#T.insert(16)
	#T.insert(19)
	#T.insert(13)
	#T.insert(21)
	preorder(T.root)
	#print(T.root)

if __name__ == '__main__':
	main()





