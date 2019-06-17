# Dequeue helps adding to list at first(insert)/ last(append) and also removing first(pop(0))/ last(pop) of queue.
from exceptions import Empty
class DequeueArray:
	def __init__(self):
		self.lst = []
		self.first = 0
	def __len__(self):
		return len(self.lst)
	def front(self):
		if self.is_empty():
			raise('The queue is empty')
		else:
			return (self.first)
	def is_empty(self):
		return len(self.lst) == 0
	def add_first(self, inp1):
		self.lst.insert(self.first, inp1)
	def add_last(self, inp2):
		self.lst.append(inp2)
	def del_first(self):
		if self.is_empty():
			raise('The queue is empty')
		else:
			return self.lst.pop(self.first)
	
	def del_last(self):	
		if self.is_empty():
			raise('The queue is empty')
		else:
			return self.lst.pop()

D = DequeueArray()
D.add_first('10')
D.add_first('20')
print(D.lst)
D.add_last('30')
D.add_last('40')
print(D.lst)
D.del_first()
print(D.lst)
D.del_last()
print(D.lst)

	
		
