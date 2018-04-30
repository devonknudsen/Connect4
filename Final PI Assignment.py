#################################################################################
#
#
#
#################################################################################

from Tkinter import *

class Piece(object):
    # radius size for each piece
    pieceRadius = 44

    # colors for both players pieces
    p1Color = "red"
    p2Color = "blue"
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # accessor for x value
    @property
    def x(self):
        return self._x

    # mutator for x value
    @x.setter
    def x(self, newX):
        self._x = newX

    # accessor for y value
    @property
    def y(self):
        return self._y

    # mutator for y value
    @y.setter
    def y(self, newY):
        self._y = newY


# class for the game grid
class Grid(Canvas):
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        gameGrid = PhotoImage(file='Connect4Grid.gif')
    
