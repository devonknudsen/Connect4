

#Variables for grid
Player_1 = '1'
Player_2 = '2'

#classx
class Board:
	def __init__ (self, columns = 7, rows = 6,):
		self.columns = columns
		self.rows = rows
		self.board = [[0] * rows for _ in range(columns)] 
		
	#print for testing
	def printBoard (self):		
		for y in range(self.rows):
			print('  '.join(str(self.board[x][y]) for x in range(self.columns)))
	
	def insert (self, column, player):
			c = self.board[column]
			#i is the starting block from the bottom
			i = -1
			#moves up if the value isn't zero
			while c[i] != 0:
				i = (i - 1)
			#changes the zero to the player's value
			c[i] = player

				
b = Board()
turn = Player_1
while True:
	#print test
	b.printBoard()
	#calls on insert
	row = input()
	b.insert(int(row), turn)
	#switches turns
	if turn == Player_1:
		turn = Player_2 
	else:
		turn = Player_1
		



