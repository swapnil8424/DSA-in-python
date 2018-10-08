class hashtable:
	def __init__(self):
		self.T=[None for i in range(30)]
	
	def insert(self,x):
		sum=0
		a=x.split()
		for i in x:
			sum += ord(i)
		h=sum%30
		temp=ListNode(x,None)
		if(self.T[h]==None):
			self.T[h]=temp
		else:
			temp.next=self.T[h]
			self.T[h]=temp



	def search(self,y):
		sum1=0
		d=0
		b=y.split()
		for i in y:
			sum1 += ord(i)
		h1=sum1%30
		if(self.T[h1]==None):
			print("String not found",end=' ')
			print(y)
		else:
			temp3=self.T[h1]
			while(temp3):
				if(temp3.value==y):
					print("String found",end=' ')
					print(y)
					d=1;
					return
				else:
					temp3=temp3.next
			if(d==0):
				print("String not found",end=' ')
				print(y)


	def printkeys(self):
		print("The keys used are:")
		for i in range(30):
			if(self.T[i]!=None):
				print(i)



	def printtable(self):
		for i in range(30):
			if(self.T[i]!=None):
				print(i)
				temp2=self.T[i]
				while(temp2):
					print(temp2.value,end=' ')
					temp2=temp2.next
				print()






class ListNode:
	def __init__(self,val,nxt):
		self.value=val
		self.next=nxt




def main():
	H=hashtable()
	H.insert('cat')
	H.insert('dog')
	H.insert('manasr')
	H.insert('act')
	H.insert('god')
	H.printkeys()
	print("The hash table is")
	H.printtable()
	H.search('manas')
	H.search('tac')
	H.search('bad')

if __name__ == '__main__':
	main()
