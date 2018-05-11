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

	def search(self,x,c):
		b=list(x)
		temp1=self.root
		d=0
		loc=list()
		for j in range(len(c)):
			for i in range(len(b)):
				t=ord(b[i])-97
				if(temp1.arr[t]==None):
					#c=1
					#print("Word doesn't exist")
					break
				else:
					temp1=temp1.arr[t]
			#if(c!=1):
			#	print("Word exists")
			if(temp1.end==True):
				#print("Word exists")
				d=d+1
				loc.append(j+1)
			#else:
				#print("Word doesn't exist")
		print("The count of occurrences of the word is "+d)
		print("The loctaion detail is"+loc)

def main():
	t=trie()
	"""t.insert("apple")
	t.insert("ball")
	t.insert("cat")
	t.insert("elephant")
	t.insert("zebra")
	t.search("sun")
	t.search("elephant")
	t.search("applet")"""
	with open('a.txt') as file:
		words=[]
		for line in file:
			words.append(line.strip('\n'))
	#print(words)
	for i in range(len(words)):
		t.insert(words[i])

	t.search("apple",words)



if __name__ == '__main__':
	main()