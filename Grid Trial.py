from Tkinter import *

# class for the game grid
class Grid(Canvas):
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        self.gameGridImg = PhotoImage(file="Connect4Grid.gif")
    def overlayGrid(self):
        self.create_image(5, 0, image=self.gameGridImg, anchor=NW)
        

window = Tk()
window.geometry("{}x{}".format(700, 800))
window.title("Connect 4")
g = Grid(window)
g.overlayGrid()
window.mainloop()
