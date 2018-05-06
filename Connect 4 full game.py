


#Variables for grid
Player_1 = '1'
Player_2 = '2'

#class
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
			self.column = column
			c = self.board[column]
			#-1 is the starting block from the bottom
			i = -1
			#0 is the top of the column
			#if its been changed it returns
			if c[0] != 0:
				return
			#moves up if the value isn't zero	
			while c[i] != 0:
				i = (i - 1)
				
			#changes the zero to the player's value
			c[i] = player
			row = i
			
			self.checkvertical(column)
			self.checkhorizontal(row)
			self.checkdiagnol(column, row)
			
			
	def checkdiagnol(self, column, row):
		self.row = row
		a = self.board[column]
		#these restrictions were created because it crashes when checking outside the range of the array
		#don't need to check to the left 
		if column < 4:
			b = self.board[column + 1]
			c = self.board[column + 2]
			d = self.board[column + 3]
		#don't need to check to the right
		if column > 2:	
			e = self.board[column - 1]
			f = self.board[column - 2]
			g = self.board[column - 3]
		
		#Checking left and up
		if column > 2 and row > -3:	
			if a[row] == e[row-1] == f[row-2] == g[row-3]:
				print 'win'		
		#Checking right and up
		if column < 4 and row > -3:	
			if a[row] == b[row-1] == c[row-2] == d[row-3]:
				print 'win'
		#Checking left and down
		if column > 2:			
			if a[row] == e[row+1] == f[row+2] == g[row+3]:
				print 'win'
		#Checking right and down
		if column < 4:	
			if a[row] == b[row+1] == c[row+2] == d[row+3]:
				print 'win'
			
			
	def checkhorizontal(self, row):
		self.row = row
		#variables for each column for the acted on row from drop()
		a = self.board[0]
		b = self.board[1]
		c = self.board[2]
		d = self.board[3]
		e = self.board[4]
		f = self.board[5]
		g = self.board[6]
		if a[row]!=0 and a[row] == b[row] == c[row] == d[row]:
			print 'win'
		if b[row]!=0 and b[row] == c[row] == d[row] == e[row]:
			print 'win'
		if c[row]!=0 and c[row] == d[row] == e[row] == f[row]:
			print 'win'
		if d[row]!=0 and d[row] == e[row] == f[row] == g[row]:
			print 'win'
			

	def checkvertical(self, column):
		self.column = column
		c = self.board[column]
		# -1 is the bottow row
		i = -1
		#these just check upwards from the bottom
		if c[i] == c[i-1] == c[i-2] == c[i-3]:
			print 'win'
		if c[i-1] != 0 and c[i-1] == c[i-2] == c[i-3] == c[i -4]:
			print 'win'
		if c[i-2] != 0 and c[i -2] == c[i-3] == c[i-4] == c[i-5]:
			print 'win'
		

	
b = Board()
turn = Player_1
while True:
	#print test
	b.printBoard()
	#calls on drop
	column = input()
	b.drop(int(column), turn)
	#switches turns
	if turn == Player_1:
		turn = Player_2 
	else:
		turn = Player_1
		



