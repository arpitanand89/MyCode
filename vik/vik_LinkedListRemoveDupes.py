class LinkedlistDupes:
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
		
	def dup(self):								# func to delete dupes in LinkedList
		thead = self._head						# thead: temporary head for value that is to be compared
		while thead:
			cnt1 = thead._next					# cnt1: values that are to be compared with element(thead)
			pos = 1
			while cnt1:							# variable to keep track of position
				if thead._element == cnt1._element:				# deletion of dupe element
					cnt2 = self._head			# temp head value which will help delete repeated value
					i = 0
					while i < pos-1:
						cnt2 = cnt2._next
						i+=1
					cnt2._next = cnt2._next._next
					cnt1 = cnt1._next
					self._size -= 1
					pos-=1
				else:
					cnt1 = cnt1._next
				pos+=1
			thead = thead._next
					
	def display(self):									# defining display func
		thead = self._head
		while thead:
			print(thead._element, end = '-->')
			thead = thead._next
		print('\n')

L = LinkedlistDupes()
L.add(20)
L.add(10)
L.add(10)
L.add(40)
L.add(10)
L.add(50)
print('Data added: ', end = ' ')
L.display()
L.dup()
print('Data after removing dupes: ', end = ' ')
L.display()
