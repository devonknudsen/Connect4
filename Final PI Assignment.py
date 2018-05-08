#################################################################################
#
#
#
#################################################################################

from Tkinter import *
from time import sleep

p1Pieces = []
p2Pieces = []

class Piece(object):
    # radius size for each piece
    pieceRadius = 44
    
    def __init__(self, x):
        self.x = float(x)

    # accessor for x value
    @property
    def x(self):
        return self._x

    # mutator for x value
    @x.setter
    def x(self, newX):
        self._x = newX

class P1Piece(Piece):
	p1Color = "red"
	def __init__(self, x):
		Piece.__init__(self, x)

class P2Piece(Piece):
	p2Color = "blue"
	def __init__(self, x):
		Piece.__init__(self, x)

# class that creates the game grid
class Grid(Canvas):
    POINT_RADIUS = 28
    
    # highest x's for each column above the grid
    # difference between slots is 65
    COLUMN1_X = 154
    COLUMN2_X = 219
    COLUMN3_X = 284
    COLUMN4_X = 349
    COLUMN5_X = 414
    COLUMN6_X = 479
    COLUMN7_X = 544
    
    # highest y before starting "piece" drop
    TOP_Y = 32
    MID_Y = 94
    
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        master.attributes("-fullscreen", True)
        self.gameGridImg = PhotoImage(file="Connect4GridPi.gif")
        self.setupGUI()

    # sets up GUI for game grid
    def setupGUI(self):
        # overlays grid image onto canvas
        self.overlayGrid()

        # creates a quit button in the top right corner
        redXimg = PhotoImage(file="RedXPi.gif")
        redXButton = Button(self, image=redXimg, command=Game.window.destroy)
        redXButton.configure(background="white")
        redXButton.image = redXimg
        redXButton.pack(side=RIGHT, anchor=NE)
        
    # function used to overlay the grid on top of the canvas 
    def overlayGrid(self):
        self.create_image(150, 25, image=self.gameGridImg, anchor=NW)

    # function used to draw the circles on the canvas
    # to simulate the creation of the pieces
    def createPiece(self, p):
        if p in plPieces:
            color = p.p1Color
        else:
            color = p.p2Color
        self.create_oval(p.x, TOP_Y, p.x + Piece.pieceRadius * 2, TOP_Y + Piece.pieceRadius * 2, outline="black", color=color)
	
	#self.dropPiece()
	
	#def dropPiece(self,

# global function used to change the game's state (doesn't work)
def changeState(button):
    if button == "start":
        Game.state = 2
##        print "2"
    if button == "home":
        Game.state = 0

# class that creates the start menu
class StartMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.resizable(False, False)
        self.setupGUI()

        
    # sets up the GUI for the start menu
    def setupGUI(self):
        # creates the logo at the top of the start menu
        connect4LogoImg = PhotoImage(file="Connect4Logo.gif")
        logo = Label(self.master, image=connect4LogoImg)
        logo.configure(background="white")
        logo.image = connect4LogoImg
        logo.grid(row=2, column=0, columnspan=10, rowspan=2, sticky=N+S+E+W)

        # creates the start button in the midsection of the start menu
        startButtonImg = PhotoImage(file="StartButton.gif")
        start = Button(self.master, image=startButtonImg, command=lambda: changeState("start"))
        start.configure(background="white")
        start.image = startButtonImg
        start.grid(row=4, column=0, columnspan=10, rowspan=1, sticky=N+S+E+W)

        # creates the quit button at the button of the start menu
        quitButtonImg = PhotoImage(file="QuitButton.gif")
        quitButton = Button(self.master, image=quitButtonImg, command=Game.window.destroy)
        quitButton.configure(background="white")
        quitButton.image = quitButtonImg
        quitButton.grid(row=6, column=0, columnspan=10, rowspan=1, sticky=N+S+E+W)



# class that runs the game
class Game(object):
    window = Tk()
    states = {"create start menu": 0, "remain on start menu": 1, "create grid": 2, "play game": 3}
    state = 0
    def __init__(self, state = 0):
        Game.state = state
        self.checkState()

    # function to check what state the game is in
    def checkState(self):
        if Game.state == 0:
            self.startMenu = StartMenu(Game.window)
            Game.state = Game.states["remain on start menu"]
        if Game.state == 1:
            pass
##            print "1"
        if Game.state == 2:
            self.grid = Grid(Game.window)
            
g = Game()
while True:
    g.checkState()
    g.window.update_idletasks()
    g.window.update()
    sleep(0.01)
