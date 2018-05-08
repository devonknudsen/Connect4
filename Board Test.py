

#Variables for grid
Empty = '0'
Player_1 = '1'
Player_2 = '2'

#class
class Board:
	def __init__ (self, columns = 7, rows = 6,):
		self.columns = columns
		self.rows = rows
		self.board = [[Empty] * rows for _ in range(columns)] 
		
	#print for testing
	def printBoard (self):		
		for y in range(self.rows):
			print('  '.join(str(self.board[x][y]) for x in range(self.columns)))
		
	
		
#tests
C = Board()
C.printBoard()