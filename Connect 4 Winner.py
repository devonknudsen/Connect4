
#this is here to stop the game when someone wins
import sys

#NEEDS A CHECK FOR WHEN THE BOARD IS FULL. Can do this but setting all columns[0] != 0
#Function for full grid and 

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
	
	#This is the entire drop function. It works from checking the bottom up
	def drop (self, column, player):
			self.column = column
			#transforms the input() from player into the column for dropping
			c = self.board[column]
			#-1 is the starting block from the bottom
			i = -1
			
			#row 0 is the top of the column
			#if the top of the column(0) != 0 then this leaves that column because it's full
			if c[-6] != 0:
				return
				
			#moves up from the bottom if the value isn't zero
			#going less in negatives goes up in the column. So row -2 is 1 above row -1
			while c[i] != 0:
				i = (i - 1)
				
			#changes the zero to the player's value
			c[i] = player
			
			#let's the check functions know what row the player added to 
			row = i
			#runs all the scenarios a player can win each time they change a value
			self.checkvertical(player, column)
			self.checkhorizontal(player,row)
			self.checkdiagnolorigin(player,column, row)
			self.checkdiagnolmiddle(player,column, row)
			
	#this checks in an x formation from the last added value(an origin)
	def checkdiagnolorigin(self, player, column, row):
		self.row = row
		a = self.board[column]
		#some of these restrictions were created because it crashes when checking outside the range of the array
		
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
		if column > 2 and row > -5:	
			if a[row] == e[row-1] == f[row-2] == g[row-3]:
				self.win(player)		
		#Checking right and up
		if column < 4 and row > -5:	
			if a[row] == b[row-1] == c[row-2] == d[row-3]:
				self.win(player)
		#Checking left and down
		if column > 2:			
			if a[row] == e[row+1] == f[row+2] == g[row+3]:
				self.win(player)
		#Checking right and down
		if column < 4:	
			if a[row] == b[row+1] == c[row+2] == d[row+3]:
				self.win(player)
			
			
			
	#this checks from the orgin with the assumption it is the middle value creating a diagnol				
	def checkdiagnolmiddle(self, player, column, row):
		self.row = row
		a = self.board[column]
		#these restrictions were created because it crashes when checking outside the range of the array
			#makes sure you can't go too far to the right
		if column < 6:
			b = self.board[column + 1]
		if column < 5:
			c = self.board[column + 2]	
			#makes sure you can't go too far to the left
		if column > 0:
			e = self.board[column - 1]	
		if column > 1:
			f = self.board[column - 2]
			
		#Checking left and up
		if column > 1 and row > -5:	
			if a[row] == e[row-1] == f[row-2] == b[row+1]:
				self.win(player)		
		#Checking right and up
		if column < 5 and row > -5:	
			if a[row] == b[row-1] == c[row-2] == e[row+1]:
				self.win(player)
		#Checking left and down
		if column < 6 and column > 1 and row < 0:			
			if a[row] == e[row+1] == f[row+2] == b[row-1]:
				self.win(player)
		#Checking right and down
		if column > 0 and column < 5 and row < 0:	
			if a[row] == b[row+1] == c[row+2] == e[row-1]:
				self.win(player)
				
				
	#instead of following an origin, this checks the entire row for any winners			
	def checkhorizontal(self, player, row):
		#variables for each column
		a = self.board[0]
		b = self.board[1]
		c = self.board[2]
		d = self.board[3]
		e = self.board[4]
		f = self.board[5]
		g = self.board[6]
		self.row = row
		
		#calls each possible win on every column for the row that the player affected
		if a[row]!=0 and a[row] == b[row] == c[row] == d[row]:
			self.win(player)
		if b[row]!=0 and b[row] == c[row] == d[row] == e[row]:
			self.win(player)
		if c[row]!=0 and c[row] == d[row] == e[row] == f[row]:
			self.win(player)
		if d[row]!=0 and d[row] == e[row] == f[row] == g[row]:
			self.win(player)
			
	#this function check the entire column the player acted on for a winner
	def checkvertical(self, player, column):
		self.column = column
		c = self.board[column]
		i = -1
		
		#these just check upwards from the bottom
		if c[i] == c[i-1] == c[i-2] == c[i-3]:
			self.win(player)
		if c[i-1] != 0 and c[i-1] == c[i-2] == c[i-3] == c[i-4]:
			self.win(player)
		if c[i-2] != 0 and c[i-2] == c[i-3] == c[i-4] == c[i-5]:
			self.win(player)
			
	
	#temp proof of win	
	def win(self, player):
		self.printBoard()
		winner = player
		print ('Player ' + winner + ' You Win!')
		sys.exit()
		
#starts the game
b = Board()
turn = Player_1

while True:
	#print test
	b.printBoard()
	#calls on drop
	column = input()
	b.drop(column, turn)
	#switches turns
	if turn == Player_1:
		turn = Player_2
	else:
		turn = Player_1
			



