from exceptions import Empty
class DequeueLinked:
	class _Node:
		def __init__(self, element, next):
			__slots__ = '_element', '__next'
			self._element  = element
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
			self._head = newest
			self._tail = newest
		else:
			newest._next = self._head
			self._head = newest
		self._size+=1
		return self._head._element
	def add_end(self, e):
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size+=1
		return newest

	def delete_start(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		else:
			thead = self._head
			self._head = thead._next
			self._head._next = thead._next._next
		if self.is_empty():
			self._tail = None
		self._size-=1
		return self._head._element
	def delete_end(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		else:
			i = 0
			thead = self._head
			while i<len(self)-2:
				thead = thead._next
				i+=1
			self._tail = thead
			thead = thead._next
			value = thead._element
			self._tail._next = None
			self._size-=1
			return value
		if self.is_empty():
			print('Empty Linked list')

	def display(self):
		thead = self._head
		while thead != None:
			print(thead._element, end = "-->")
			thead = thead._next
		print('\n')

L = DequeueLinked()
L.add_end(10)
L.add_end(20)
L.add_end(30)
L.display()
L.delete_start()
L.display()
L.add_start(40)
L.display()
L.delete_end()		
L.display()	
				
			
			
	
		
		 
			

	

