''' init is used to initialize a class with a value viz. an object of this class
 will have a specific value by defaul when it initializes '''
class Tuna:
	def __init__(self):
		 print('My name is Tuna')
	def name(self):
		print('Whats is ur name')
		
name1=Tuna()
name1.name()
	 
class game:
	def __init__(self, default_energy):  #Here energy value is assigned to a player in the beginnig by default and user can get it as and when required
		self.energy=default_energy
	def current_life(self):
		print(self.energy)
		
p1=game(5)
p2=game(20)
p1.current_life()
p2.current_life()
