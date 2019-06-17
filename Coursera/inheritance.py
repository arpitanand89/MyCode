# Inheritence

class Badminton():
	def play(self):
		print('You can play BD')

class shot():
	def drop(self):
		print("Shuttle close to the net")
	def toss(self):
		print("Shuttle far from the net")
		
class special_shot():
	def smash(self):
		print("Boom")

class player1(Badminton,shot):
	pass
class player2(Badminton,special_shot):
	pass

p1=player1()
p2=player2()
p1.play()
p1.drop()
p1.toss()
p2.play()
p2.smash()
	

