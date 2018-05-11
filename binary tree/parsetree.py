class TreeNode:
	def __init__(self):
		self.parent=None
		self.left=None
		self.right=None
		self.value=0

class parseTree:
	def __init__(self):
		self.root=None

def isoperator(op):
	if op=='*'or op=='+'or op=='/' or op=='-' or op=='%':
		return True
	else:
		return False

def printPostfix(x):
	if x==None:
		return
	else:
		printPostfix(x.left)
		printPostfix(x.right)
		print(x.value,end=" ")

def printPrefix(x):
	if x==None:
		return
	else:
		print(x.value,end=" ")
		printPrefix(x.left)
		printPrefix(x.right)

def evaluate(x):
	if x.left==None and x.right==None:
		return x.value
	else:
		op1=evaluate(x.left)
		op2=evaluate(x.right)
		result=cal(op1,op2,x.value)
		return result

def cal(op1,op2,symb):
	if symb=='+':
		return op1+op2
	elif symb=='-':
		return op1 - op2
	elif symb=='*':
		return op1*op2
	elif symb=='%':
		return op1%op2
	else:
		return op1/op2

def parse(T,x):
	current=T.root
	for i in range(len(x)):
		if x[i]=='(':
			temp=TreeNode()
			temp.parent=current
			if T.root==None:
				current=temp
				T.root=current
			elif current.left==None:
				current.left=temp
				current=temp
			else:
				current.right=temp
				current=temp
		elif x[i]==')':
			if current.parent!=None:
				current=current.parent
		elif isoperator(x[i]):
			current.value=x[i]
		else:
			temp=TreeNode()
			temp.value=int(x[i])
			if current.left==None:
				current.left=temp
				temp.parent=current
			else:
				current.right=temp
				temp.parent=current

def main():
	T=parseTree()
	x="(2*(3+(6-4)))"
	print("The equation is ",end=" ")
	print(x)
	parse(T,x)
	print("Postfix of the equation is ",end=" ")
	printPostfix(T.root)
	print()
	print("Postfix of the equation is ",end=" ")
	printPrefix(T.root)
	print()
	print("The value of expression is ",end=" ")
	print(evaluate(T.root))

if __name__ == '__main__':
	main()

