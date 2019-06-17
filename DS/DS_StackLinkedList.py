from exceptions import Empty
class StackLinked:
	class _Node:
		__slots__ = '_element', '_next'
		def __init__(self, element, next):
			self._element = element
			self._next = next
	def __init__(self):
		self._head = None
		self._size = 0
	def __len__(self):
		return self._size
	def is_empty(self):
		return self._size == 0
	
	def push(self, e):
		self._head = self._Node(e, self._head)
		self._size += 1
		
	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		else:
			value = self._head._element
			self._head = self._head._next
			self._size -= 1
			return value
			
	def top(self):
		value = self._head._element
		return value
		
	def display(self):
		temp = self._head
		while temp:
			print(temp._element, end = "-->")
			temp = temp._next
		print('\n')
		
SLL = StackLinked()
SLL.push(10)
SLL.push(20)
SLL.display()			
SLL.push(30)
SLL.display()
SLL.pop()
SLL.display()
SLL.push(40)
SLL.display()
print(SLL.top())	
SLL.pop()	
SLL.display()			 
			
