from exceptions import Empty
class CircularLinkedList:
	class _Node:
		__slots__ = '_element', '_next'
		
		def __init__(self, element, next):
			self._element = element
			self._next = next
			
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0
		
	def __len__(self):
		return self._size
		
	def is_empty(self):
		return self._size == 0
		
	def add_start(self, e):
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest
			self._head = newest
			self._tail = newest
		else:
			newest._next = self._head
			self._tail._next = newest
			self._head = newest
		self._size += 1
		
	def add_end(self, e):
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest
			self._head = newest
			self._tail = newest
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size += 1
		
	def add_any(self, e, pos):
		newest = self._Node(e, None)
		thead = self._head
		i = 1
		while i < pos:
			thead = thead._next
			i +=1
		newest._next = thead._next
		thead._next = newest
		self._size += 1
	
	def delete_start(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		else:
			thead = self._head
			self._tail._next = thead._next
			self._head = thead._next
		self._size -= 1
	def delete_end(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		else:
			thead = self._head
			i = 0
			while i < len(self)-2:
				thead = thead._next
				i +=1
			self._tail = thead
			thead = thead._next
			self._tail._next =  self._head
		self._size -= 1
	def delete_any(self, pos):
		thead = self._head
		i = 1
		while i < pos:
			thead = thead._next
			i += 1
		thead._next = thead._next._next
		self._size -= 1
	
	def display(self):
		i = 0
		thead = self._head
		while i < len(self):
			print(thead._element, end = "-->")
			thead = thead._next
			i +=1
		print('\n')

CL = CircularLinkedList()
CL.add_end(10)
CL.add_end(20)
CL.add_end(30)
CL.display()
CL.delete_start()
CL.display()
CL.add_start(40)
CL.add_start(50)
CL.display()
CL.delete_any(2)
CL.display()
CL.add_any(70,2)
CL.display()
CL.delete_end()
CL.display()
