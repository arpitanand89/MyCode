#class vs instance variables

class girl:
	gender = 'female'   # This(gender) is a class variable
	def __init__(self, name):
		self.name=name        #This(name) is a instance variable

g1=girl('jassi')
g2=girl('kanny')
print(g1.name)
print(g2.name)	 # instance variable is diff for every instance
print(g1.gender) # class variable remains same for entire class
print(g2.gender)
