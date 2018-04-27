from Tkinter import *

# class for the game grid
class Grid(Canvas):
    POINT_RADIUS = 44
    TOP_LEFT_X = 10
    TOP_LEFT_Y = 10
    
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        self.gameGridImg = PhotoImage(file="Connect4Grid.gif")

    # function used to overlay the grid on top of the canvas 
    def overlayGrid(self):
        self.create_image(5, 0, image=self.gameGridImg, anchor=NW)

    # function used to draw the circles on the canvas
    # to simulate the placing of the pieces
    def placePiece(self):
        self.create_oval(Grid.TOP_LEFT_X, Grid.TOP_LEFT_Y, Grid.TOP_LEFT_X + Grid.POINT_RADIUS * 2, Grid.TOP_LEFT_Y + Grid.POINT_RADIUS * 2, outline="black", fill="red")

window = Tk()
window.geometry("{}x{}".format(700, 800))
window.title("Connect 4")
g = Grid(window)
g.overlayGrid()
g.placePiece()
window.mainloop()
