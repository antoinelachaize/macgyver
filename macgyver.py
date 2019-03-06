
class Macgyver:

#MacGyver has a name, a position, he can move and catch items.
	def __init__(self, name, position, labyrinth, move, catch):
		self.name = Macgyver
		self.position = position
		self.maze = maze
		self.move = move
		self.catch = catch
		self.items = None

	def move(self, move):
		#Move to the right.
		if move == 'right':
				#We check that the destination box is not a wall
				if self.position[self.case_y][self.case_x+1] != '#':
					#Moving a box
					self.case_x += 1
					
		#Move to the left.
		if move == 'left':
				if self.position[self.case_y][self.case_x-1] != '#':
					self.case_x -= 1
		
		#Move up.
		if move == 'up':
				if self.position[self.case_y-1][self.case_x] != '#':
					self.case_y += 1

		#Move down
		if move == 'down':
				if self.position[self.case_y+1][self.case_x] != '#':
					self.case_y -= 1

	def catch(self, move, items):
		#If MacGyver moves on an items.
		if self.move on self.items:
			#He has one more items.
			self.items += 1
		#If you miss items.
		if self.items != 3
			print ("You are missing" [self.items] "items")		
		#If you caught all the items.
		elif self.items == 3
			print ("You caught all the items you can now fight the guardian")

