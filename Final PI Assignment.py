#################################################################################
#
#
#
#################################################################################

from Tkinter import *

class Piece(object):
    # subject to change after looking on the grid
    pieceRadius = 5
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

# class for a player one piece
class PlayerOne(Piece):
    # class variable predefining player one piece color to red
    p1Color = "red"
    def __init__(self, x, y):
        Piece.__init__(self, x, y)

# class for a player two piece
class PlayerTwo(Piece):
    # class variable predefining player two piece color to blue
    p2Color = "blue"
    def __init__(self, x, y):
        Piece.__init__(self, x, y)

# class for the game grid
class Grid(Canvas):
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        gameGrid = PhotoImage(file='Connect4Grid.gif')
    
