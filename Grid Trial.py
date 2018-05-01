from Tkinter import *

# class that creates the game grid
class Grid(Canvas):
    POINT_RADIUS = 28
    
    # highest x's for each column above the grid
    # differnence between slots is 65
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
        redXButton = Button(self, image=redXimg, command=window.destroy)
        redXButton.configure(background="white")
        redXButton.image = redXimg
        redXButton.pack(side=RIGHT, anchor=NE)
        
        # creates a home button in the top right corner
        homeButtonImg = PhotoImage(file="HomeButtonPi.gif")
        homeButton = Button(self, image=homeButtonImg)
        homeButton.configure(background="white")
        homeButton.image = homeButtonImg
        homeButton.pack(side=RIGHT, anchor=NE)
        

    # function used to overlay the grid on top of the canvas 
    def overlayGrid(self):
        self.create_image(150, 25, image=self.gameGridImg, anchor=NW)

    # function used to draw the circles on the canvas
    # to simulate the placing of the pieces
    # must change radius back to point radius and colors back to strs before implemeting into main game file
    def placePiece(self):
            self.create_oval(Grid.COLUMN7_X , Grid.MID_Y, Grid.COLUMN7_X  + Grid.POINT_RADIUS * 2, Grid.MID_Y + Grid.POINT_RADIUS * 2, outline="black", fill="red")
        

window = Tk()
window.title("Connect 4")
g = Grid(window)
window.mainloop()
