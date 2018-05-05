

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

	
def checkOWin(Board):

    boardHeight = len(board)
    boardWidth = len(board[0])
    tile = 'O'
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False
	
b = Board()
turn = Player_1
while True:
	#print test
	b.printBoard()
	#calls on drop
	row = input()
	b.drop(int(row), turn)
	#switches turns
	if turn == Player_1:
		turn = Player_2 
	else:
		turn = Player_1
		



