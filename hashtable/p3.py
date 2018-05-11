class hashtable:
	def __init__(self):
		self.T=[None for i in range(30)]
	
	def insert(self,x):
		c=list()
		for i in x:
			c.append(ord(i))
		d=self.horner(c)
		h=d%30
		temp=ListNode(x,None)
		if(self.T[h]==None):
			self.T[h]=temp
		else:
			temp.next=self.T[h]
			self.T[h]=temp



	def search(self,y):
		e=0
		a=list()
		for i in y:
			a.append(ord(i))
		d=self.horner(a)
		h1=d%30
		if(self.T[h1]==None):
			"""print("String is spelled incorrectly",end=' ')
			print(y)"""
			return False
		else:
			temp3=self.T[h1]
			while(temp3):
				if(temp3.value==y):
					"""print("String spelled correctly",end=' ')
					print(y)"""
					e=1
					return True
				else:
					temp3=temp3.next
			if(e==0):
				"""print("String is spelled incorrectly",end=' ')
				print(y)"""
				return False


	"""def printkeys(self):
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
	"""
	def horner(self,c):
		horn=c[0]
		for i in range(len(c)):
			horn= horn*33 + c[i]
		return horn


	def suggest(self,s):
		alpha=list()
		alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		for p in range(len(s)):
			b=list(s)
			for q in range(len(alpha)):
				b[p]=alpha[q]
				''.join(b)
				if(self.search(b)==True):
					print(b)






class ListNode:
	def __init__(self,val,nxt):
		self.value=val
		self.next=nxt




def main():
	H=hashtable()
	with open('ispell.dict') as f:
		for line in f:
			s=line.strip()
			H.insert(s)
	print("Enter the string ")
	key=input()
	#if(H.search(key)==False):
	H.suggest(key)


    


if __name__ == '__main__':
	main()
