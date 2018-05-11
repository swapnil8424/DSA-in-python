class trienode:
	def __init__(self):
		self.arr=[None]*26
		self.end=False

class trie:
	def __init__(self):
		self.root=trienode()

	def insert(self,x):
		a=list(x)
		temp=self.root
		for i in range(len(a)):
			t=ord(a[i])-97
			if(temp.arr[t]==None):
				temp.arr[t]=trienode()
			temp=temp.arr[t]
		temp.end=True

	def search(self,x):
		b=list(x)
		temp1=self.root
		for i in range(len(b)):
			t=ord(b[i])-97
			if(temp1.arr[t]==None):
				#c=1
				print("Word doesn't exist")
				return
			else:
				temp1=temp1.arr[t]
		#if(c!=1):
		#	print("Word exists")
		if(temp1.end==True):
			print("Word exists")
		else:
			print("Word doesn't exist")

def main():
	t=trie()
	t.insert("apple")
	t.insert("ball")
	t.insert("cat")
	t.insert("elephant")
	t.insert("zebra")
	t.search("sun")
	t.search("elephant")
	t.search("applet")

if __name__ == '__main__':
	main()