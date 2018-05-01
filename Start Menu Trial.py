from Tkinter import *

class StartMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.setupGUI()

    def setupGUI(self):
        
        connect4LogoImg = PhotoImage(file="Connect4Logo.gif")
        logo = Label(self.master, image=connect4LogoImg)
        logo.configure(background="white")
        logo.image = connect4LogoImg
        logo.grid(row=2, column=0, columnspan=10, rowspan=2, sticky=N+S+E+W)

        startButtonImg = PhotoImage(file="StartButton.gif")
        start = Button(self.master, image=startButtonImg)
        start.configure(background="white")
        start.image = startButtonImg
        start.grid(row=4, column=0, columnspan=10, rowspan=1, sticky=N+S+E+W)

        quitButtonImg = PhotoImage(file="QuitButton.gif")
        quitButton = Button(self.master, image=quitButtonImg, command=window.destroy)
        quitButton.configure(background="white")
        quitButton.image = quitButtonImg
        quitButton.grid(row=6, column=0, columnspan=10, rowspan=1, sticky=N+S+E+W)

window = Tk()
start = StartMenu(window)
window.mainloop()
