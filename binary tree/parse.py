class TreeNode:
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.left=l
		self.right=r

class parseTree:
	def __init__(self):
		self.root=TreeNode()

	def insert(self,x):
		a=x.split()
		print(a)
		print(len(a))
		temp=TreeNode()
		temp2=TreeNode()
		temp2=self.root
		for i in a:  
			if(i=='('):
				continue
			elif(i=='+' or i=='-' or i=='*' or i=='/'):
				temp2.key=i
				if(temp2.left!=None):
					temp2.right=temp
				else:
					temp2.left=temp
				temp.parent=temp2
				#print(temp.key)
				print(temp2.key)
			elif(i==')'):
				if(temp2.left!=None):
					temp2.right=temp
				else:
					temp2.left=temp
				temp.parent=temp2
			else:
				temp.key=i
				print(temp.key)
				temp.parent=None
				temp.left=None
				temp.right=None

def main():
	T=parseTree()
	a='( 2 * 3 )'
	T.insert(a)
	print("  ")
	print(T.root.key)
	print(T.root.left.key)
	print(T.root.right.key)
	
if __name__ == '__main__':
	main()
		
