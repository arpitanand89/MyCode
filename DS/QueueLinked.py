from exceptions import Empty
class QueueLinked:
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
		
	def enqueue(self, e):
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size+=1
	def deqeue(self):
		value = self._head._element
		self._head = self._head._next
		self._size-=1
		
	def display(self):
		temp = self._head
		while temp != None:
			print(temp._element, end= '-->')
			temp = temp._next
			#print(temp._next._element)
		print('\n')
		
QL = QueueLinked()
QL.enqueue(10)
QL.enqueue(20)
QL.enqueue(30)
QL.display()
QL.deqeue()
QL.display()
QL.enqueue(40)
QL.display()
QL.deqeue()
QL.deqeue()
QL.display()
			
			
