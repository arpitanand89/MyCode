# Return the K{th} to last node in Linked list.

class LinkedlistDupes:							# Naming Linked List
	class _Node:								# defining a node
		def __init__(self, element, next):		# initializing variables for node
			__slots__ = '_element', '_next'
			self._element = element
			self._next = next
	def __init__(self):							# initializing the Linkedlist
		self._size = 0
		self._head = None
		self._tail = None
		
	def is_empty(self):							# defining empty func
		return self._size == 0
		
	def __len__(self):
		return self._size
	
	def add(self, e):							# defining add func
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			self._tail._next = newest
			self._tail = self._tail._next
		self._size+=1

	def NthValue(self, K):							# function to displat Kth value to last
		temp = self._head
		i = 0
		if K > len(self)-1:
			print('Value of N is greater than or equal to the length of Linked list')
			exit()
		else:
			pos = (len(self)-1) - K
			while i < pos:
				temp = temp._next
				i += 1
		print(temp._element)

	def display(self):									# defining display func
		thead = self._head
		while thead:
			print(thead._element, end = '-->')
			thead = thead._next
		print('\n')

L = LinkedlistDupes()
L.add(10)
L.add(20)
L.add(30)
L.add(40)
L.add(50)
L.add(60)
L.display()
L.NthValue(2)


 
