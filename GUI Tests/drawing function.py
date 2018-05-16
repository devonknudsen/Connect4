
		
def draw(self, column, row, player):
	x = (154 +(column * 65))
	y = (94 +((6+row)* -65))
	if player == 1:
		P1piece(x, y, player)
	else: 
		P2piece(x, y, player)
		
