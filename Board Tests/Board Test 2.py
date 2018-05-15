

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
	
	def insert (self, column, playernum):
			c = self.board[column]
			i = -1
			while c[i] != 0:
				i = (i - 1)
			c[i] = playernum

				
if __name__ == '__main__':
	g = Board()
	turn = Player_1
	while True:
		g.printBoard()
		row = input()
		g.insert(int(row), turn)
		if turn == Player_1:
			turn = Player_2 
		else:
			turn = Player_1
		


