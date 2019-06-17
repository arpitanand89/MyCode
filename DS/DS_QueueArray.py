# Queue method follows FiFO method using queue(append) and dequeue(return first value and replace first value by None)

from exceptions import Empty
class QueueStack:
	def __init__(self):
		self.lst = []
		self.first = 0
		self.size = 0
	def __len__(self):
		return self.size
	def is_empty(self):
		return self.size == 0
	def enqueue(self, inp):
		self.lst.append(inp)
		self.size+=1
	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		else:
			value = self.lst[self.first]
			self.lst[self.first] = None
			self.first+=1
			self.size-=1
			return value
	def First(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		else:
			return self.lst[self.first] 

Q = QueueStack()
print(Q.is_empty())
#print(Q.First())
Q.enqueue('Red')
Q.enqueue('Green')
print(Q.lst)
print(len(Q))
print(Q.First())
Q.dequeue()
print(Q.lst)
print(Q.First())
Q.dequeue()
Q.enqueue('Green')
Q.enqueue('Pink')
print(Q.lst)
