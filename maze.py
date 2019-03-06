
class Maze:

#The Maze is composed of a departure, an exit, walls and path
	def __init__(self, departure, exit, walls, path, width, height):
		self.path = []
        self.walls = []
        self.departure = None
        self.exit = None

        self.width = None
        self.height = None

    def display(self):
        for x in range(self.height):
            for y in range(self.width):
                if (x, y) in self.paths:
                    print(".", end="")
                else:
                    print("*", end="")
            print()

    @classmethod
    def load_from_file(cls, filename):
    	with open(filename, 'r') as f:
			for x, line in enumerate (f):
				for y, char in enumerate(line):
				#If Char is # then it's a wall.
				if char == '#':
					walls.append((x,y))
				#If Char is . then it's a path.
				elif char == '.':
					path.append((x,y))
				#If Char is D then it's the departure.
				elif char == 'D':
					path.append((x,y))
					departure = (x,y)
				#If Char is X then it's the exit.
				elif char == 'X'
					path.append((x,y))
					exit = (x,y)

			maze.width = x
			maze.height = y
            return maze
                    
    
maze = Maze.load_from_file('maze.txt')
maze.display()
