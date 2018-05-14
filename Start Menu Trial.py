from Tkinter import *

# class that creates the start menu
class StartMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
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
        start = Button(self.master, image=startButtonImg)
        start.configure(background="white")
        start.image = startButtonImg
        start.grid(row=4, column=0, columnspan=10, rowspan=1, sticky=N+S+E+W)

        # creates the quit button at the button of the start menu
        quitButtonImg = PhotoImage(file="QuitButton.gif")
        quitButton = Button(self.master, image=quitButtonImg, command=window.destroy)
        quitButton.configure(background="white")
        quitButton.image = quitButtonImg
        quitButton.grid(row=6, column=0, columnspan=10, rowspan=1, sticky=N+S+E+W)

window = Tk()
StartMenu(window)
window.mainloop()
