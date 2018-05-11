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
			"""if i!=(len(a)-1):
				temp=temp.arr[t]
			else:
				temp.end="#"""
		temp.end="#"

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
		if(temp1.end=="#"):
			print("Word exists")
		else:
			print("Word doesn't exist")

def main():
	t=trie()
	t.insert("apple")
	t.insert("ball")
	t.insert("cat")
	t.insert("to")
	t.insert("today")
	t.insert("elephant")
	t.insert("zebra")
	t.search("sun")
	t.search("elephant")
	t.search("applet")
	t.search("to")
	t.search("today")

if __name__ == '__main__':
	main()