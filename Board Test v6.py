import sys

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
	
	def drop (self, column, player):
			c = self.board[column]
			#i is the starting block from the bottom
			i = -1
			#moves up if the value isn't zero
			while c[i] != 0:
				i = (i - 1)
				
			#changes the zero to the player's value
			c[i] = player
			
	#def checkforwin():
	
	#def checkhorizontal():
	
	def checkvertical(self, column):
		self.column = column
		c = self.board[column]
		i = -1
		if c[i] == c[i-1] == c[i-2] == c[i-3]:
			print 'win'
		if c[i-1] != 0 and c[i-1] == c[i-2] == c[i-3] == c[i -4]:
			print 'win'
		if c[i-2] != 0 and c[i -2] == c[i-3] == c[i-4] == c[i-5]:
			print 'win'
		else:
			pass

	
b = Board()
turn = Player_1
while True:
	#print test
	b.printBoard()
	#calls on drop
	column = input()
	b.drop(int(column), turn)
	b.checkvertical(int(column))
	#switches turns
	if turn == Player_1:
		turn = Player_2 
	else:
		turn = Player_1
		



