# Stack method follows LiFO method using append(push)/ pop. A stack is closed at bottom and open at top hence LiFO.

from exceptions import Empty
class StackArray:
	def __init__(self):
		self.lst = []
	def __len__(self):
		return len(self.lst)
	def is_empty(self):
		return len(self.lst) == 0
	def push(self, inp):
		self.lst.append(inp)
	def pop(self):
		if self.is_empty():
			raise Empty('The list is empty')
		else:
			return self.lst.pop()
	def top(self):
		if self.is_empty():
			raise Empty('The list is empty')
		else:
			return self.lst[-1]

s = StackArray()
print('Length', len(s))
print('Output of is_empty', s.is_empty())
#s.top()
s.push(10)
s.push(20)
print('data after push', s.lst)
s.pop()
print('data after pop', s.lst)
s.push(30)
s.push(40)
s.top()
print('data after 2 push and top', s.lst)
