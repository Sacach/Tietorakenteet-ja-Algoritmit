#Implementation of linked list

#Node in the list
class Node:
	def __init__(self,d,n=None):
		self.data = d
		self.next = n

#The list: its head	
class LinkedList:
	def __init__(self):
		self.head = None

#Inserts a key into list
#inserted to head	
def list_insert(li, key):
	n = Node(key)
	n.data = key
	n.next=li.head
	li.head = n

#Searches and returns a node with
#the given key
def list_search(li, key):
	node = li.head
	found = False
	
	while node != None and not found:
		if node.data == key:
			found = True
		else:
			node = node.next
	
	return node

#Searches and removes a node with
#the given key
def list_remove(li,key):
	node = list_search(li,key)
	
	if node != None:
		
		# Check if head node deleted
		if node == li.head:
			li.head = node.next
		else:
			# Find predecessor
			pred = li.head
			
			while pred.next != node:
				pred = pred.next
			
			pred.next = node.next;
		
#Prints node
def print_node(node):
	print(node.data)

#Prints list starting from head
def print_list(li):
	node = li.head
	while node != None:
		print_node(node)
		node = node.next;
	

