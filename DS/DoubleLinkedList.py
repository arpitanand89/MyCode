from exceptions import Empty
class DoubleLinkedList:
	class _Node:
		__slots__ = '_element', '_next', '_prev'
		def __init__(self, element, next, prev):
			self._element = element
			self._next = next
			self._prev = prev
	def __init__(self):
		self._head = self._Node(None, None, None)
		self._tail = self._Node(None, None, None)
		self._head._next = self._tail
		self._tail._next = self._head
		self._size = 0
	def __len__(self):
		return self._size
		
	def is_empty(self):
		return self._size == 0
		
	def add_start(self, e):
		newest = self._Node(e, None, None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			newest._next = self._head
			self._head._prev = newest
			self._head = newest
		self._size += 1
			
	def add_end(self, e):
		newest = self._Node(e, None, None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			newest._next = None
			newest._prev = self._tail
			self._tail._next = newest
			self._tail = newest
		self._size += 1
			
	def add_any(self, e, pos):
		newest = self._Node(e, None, None)
		thead = self._head
		i = 1
		while i < pos:
			thead = thead._next
			i+=1
		newest._next = thead._next
		thead._next = newest
		newest._prev = thead
		self._size += 1
			
	def delete_start(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		else:
			self._head = self._head._next
			self._head._prev = None
		self._size -= 1
	
	def delete_end(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		else:
			i = 0
			thead = self._head
			while i < len(self)-2:
				thead = thead._next
				i += 1
			#thead._next = None
			self._tail = thead
			thead = thead._next
			self._tail._next = None
		self._size -= 1	
		
	def delete_any(self, pos):
		i = 1
		thead = self._head
		while i < pos:
			thead = thead._next
			i += 1
		thead._next = thead._next._next
		thead._next._prev = thead
		self._size -= 1
	def display(self):
		thead = self._head
		while thead != None:
			print(thead._element, end = "-->")
			thead = thead._next
		print('\n')
			
DLL = DoubleLinkedList()
DLL.add_end(10)
DLL.add_end(20)
DLL.add_end(30)
DLL.display()
DLL.delete_start()
DLL.display()
DLL.add_start(40)
DLL.add_start(50)
DLL.display()
DLL.add_any(60, 2)
DLL.display()
DLL.delete_any(2)	
DLL.display()	
DLL.delete_end() 
DLL.display()
