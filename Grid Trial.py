from Tkinter import *

# class for the game grid
class Grid(Canvas):
    POINT_RADIUS = 44
    
    # highest x's for each column above the grid
    COLUMN1_X = 305
    COLUMN2_X = 405
    COLUMN3_X = 505
    COLUMN4_X = 605
    COLUMN5_X = 705
    COLUMN6_X = 805
    COLUMN7_X = 905
    
    # highest y before starting "piece" drop
    TOP_Y = 75
    MID_Y = 170
    
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        master.attributes("-fullscreen", True)
        self.gameGridImg = PhotoImage(file="Connect4Grid.gif")
        self.setupGUI()

    # sets up GUI for game grid
    def setupGUI(self):
        # overlays grid image onto canvas
        self.overlayGrid()

        # creates a quit button in the top right corner
        # needs to be made into an image button
        quitButton = Button(self, text="Quit", command=window.destroy)
        quitButton.pack(side=RIGHT, anchor=NE)

        # creates a settings button in the top right corner
        # needs to be made into an image button
        settingsButton = Button(self, text="Settings")
        settingsButton.pack(side=RIGHT, anchor=NE)

        # creates a home button in the top right corner
        # needs to be made into an image button
        homeButton = Button(self, text="Home")
        homeButton.pack(side=RIGHT, anchor=NE)
        

    # function used to overlay the grid on top of the canvas 
    def overlayGrid(self):
        self.create_image(300, 65, image=self.gameGridImg, anchor=NW)

    # function used to draw the circles on the canvas
    # to simulate the placing of the pieces
    def placePiece(self, x, y, player):
        if player == "p1":
            self.create_oval(x, y, x + Piece.pieceRadius * 2, y + Piece.pieceRadius * 2, outline="black", fill=Piece.plColor)
        if player == "p2":
            self.create_oval(x, y, x + Piece.pieceRadius * 2, y + Piece.pieceRadius * 2, outline="black", fill=Piece.p2Color)

window = Tk()
window.title("Connect 4")
g = Grid(window)
g.placePiece()
window.mainloop()
