class game:
	life=3
	def shoot(self):
		print('Ouch')
		self.life -=1
	def current_life(self):
		if (self.life<=0):
			print('I am dead')
		else:
			print(str(self.life)+' life left')

player1 = game()
player2=game()
player1.shoot()
player1.current_life()
player2.current_life()
