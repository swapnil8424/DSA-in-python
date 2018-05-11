class LinkedList:
    """Defines a Singly Linked List.
	attributes: head"""
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()

    def insert(self,x,p):
        """Insert element x in the position after p"""
        temp=ListNode()
        temp.value=x
        temp.next=p.next
        p.next=temp


    def delete(self,p):
        """Delete the node following node p in the linked list."""
        p.next=p.next.next

    def printlist(self):
        """ Print all the elements of a list in a row."""
        i=self.head.next
        while i:
        	print(str(i.value))
        	i=i.next


    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        j=self.head
        p=0
        temp=ListNode()
        temp.value=x
        while(i>p):
        	j=j.next
        	p=p+1
        temp.next=j.next
        j.next=temp
   

    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        i=self.head
        while(i.next != None and i.value !=x):
        	i=i.next
        if(i.next != None):
        	print("Value found at position"+str(i))
        else:
        	return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        i=0
        j=self.head
        while(j.next != None):
        	i=i+1
        	j=j.next
        return i

   
    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if(self.head.next==None):
        	print("True")
        else:
        	print("False")


class ListNode:
    """Represents a node of a Singly Linked List.
	attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ')
    L.printlist()
    L.insert(12,L.head.next)
    print('List is: ')
    L.printlist()
    L.insert(2,L.head)
    print('List is: ')
    L.printlist()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ')
    L.printlist()
    L.delete(L.head.next)
    print('List is: ')
    L.printlist()
    print('List is empty?')
    L.isEmpty()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?')
    L.isEmpty()
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ')
    L.printlist()


if __name__ == '__main__':
    main()
