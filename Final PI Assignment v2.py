################################################################################################
# Name: Devon Knudsen, Jeremiah Pounds, Newton Koech
# Date: 16 May 2018
# Description: Connect 4! - We created a game of connect four that implements the breadboard as
# well as the RPi touchscreen.
################################################################################################

import RPi.GPIO as GPIO
from Tkinter import *
from time import sleep

DEBUG_LEVEL_1 = False

# set the GPIO pin numbers
# the switches (from L to R)
switches = [ 24, 23, 22, 21, 20, 19, 18 ]

# the LEDs (from L to R)
leds = [ 12, 17 ]

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the input and output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

# list for the pieces of each character that are created
p1Pieces = []
p2Pieces = []

class Piece(object):
    # radius size for each piece
    pieceRadius = 28
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # accessor for x value
    @property
    def x(self):
        return self._x

    # mutator for x value
    @x.setter
    def x(self, newX):
        self._x = newX

    # accessor for x value
    @property
    def y(self):
        return self._y

    # mutator for x value
    @y.setter
    def y(self, newY):
        self._y = newY

# subclass to piece superclass that creates player 1 pieces
class P1Piece(Piece):
    Player_1 = '1'
    p1Color = "red"
    def __init__(self, x, y):
            Piece.__init__(self, x, y)

# subclass to piece superclass that creates player 2 pieces 
class P2Piece(Piece):
    Player_2 = '2'
    p2Color = "blue"
    def __init__(self, x, y):
            Piece.__init__(self, x, y)

# class that creates the game grid
class Grid(Canvas):
    # highest x's for each column above the grid
    # differnence between slots is 65
    COLUMN0_X = 154
    COLUMN1_X = 219
    COLUMN2_X = 284
    COLUMN3_X = 349
    COLUMN4_X = 414
    COLUMN5_X = 479
    COLUMN6_X = 544
    
    # highest y before starting "piece" drop
    # differnence between slots is 65
    ROW1_Y = 94
    ROW2_Y = 159
    ROW3_y = 224
    ROW4_Y = 289
    ROW5_Y = 354
    ROW6_Y = 419
    
    # need to define class variables such as midpoint values for grid
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        master.attributes("-fullscreen", True)
        self.gameGridImg = PhotoImage(file="Connect4GridPi.gif")

        # overlays grid image onto canvas
        self.overlayGrid()
        
        self.winner = None
        self.gameWon = False

        
    # function used to overlay the grid on top of the canvas 
    def overlayGrid(self):
        self.create_image(150, 25, image=self.gameGridImg, anchor=NW)

    # function used to draw the circles on the canvas
    # to simulate the creation of the pieces
    def createPiece(self, p):
        if p in p1Pieces:
            color = p.p1Color
        else:
            color = p.p2Color
        self.create_oval(p.x, p.y, p.x + Piece.pieceRadius * 2, p.y + Piece.pieceRadius * 2, outline="black", fill=color)

    # function that creates the board of values that will be used to play the game in the background
    def createValuesBoard(self):
        self.columns = 7
        self.rows = 6
        self.board = [[0] * self.rows for _ in range(self.columns)]

    # function that prints the created board for debug purposes
    def printBoard(self):
        for y in range(self.rows):
            print(' '.join(str(self.board[x][y]) for x in range(self.columns)))

    # function that looks for player input from the switches   
    def playerInput(self):
        pressed = False
        # so long as no switch is currently pressed...
        while (not pressed):
            # ...we can check the status of each switch
            for i in range(len(switches)):
                # if one switch is pressed
                while (GPIO.input(switches[i]) == True):
                    # note its index
                    val = i
                    # note that a switch has now been pressed
                    # so that we don't detect any more switch presses
                    pressed = True
                    
        return val

    # this is the entire drop function. It works from checking the bottom up
    def drop(self, column, player):
        # transforms the input() from player into the column for dropping
        c = self.board[column]

        # -1 is the starting block from the bottom
        i = -1

        # if the top of the column isn't 0
        # switches turn so it can be switched back
        # so the player doesn't "lose" their turn
        if c[0] != 0:
            if self.turn == P1Piece.Player_1:
                self.switchTurn(P1Piece.Player_1)
            else:
                self.switchTurn(P2Piece.Player_2)
            return

        # moves up from the bottom if the value isn't zero
        # going less in negatives goes up in the column. So row -2 is 1 above row -1
        while c[i] != 0:
            i -= 1

        # changes the zero to the player's value
        c[i] = player

        # let's the check functions know what row the player added to
        row = i

        if DEBUG_LEVEL_1 == True:
            print "Column currently is " + str(column)
            print "Row currently is " + str(row)
            
        self.draw(column, row, player)

        #runs all the scenarios a player can win each time they change a value
        self.checkVertical(player, column)
        self.checkHorizontal(player, row)
        self.checkDiagnalOrigin(player, column, row)
        self.checkDiagnalMiddle(player, column, row)

    # function that creates pieces on the screen
    def draw(self, column, row, player):
        x = (154 + (column * 65) )
        y = (94 +( (6 + row) * 65) )

        # determines the current player to decide which piece to create
        if player == '1':
            p = P1Piece(x, y)
            p1Pieces.append(p)
        else:
            p = P2Piece(x, y)
            p2Pieces.append(p)

        self.createPiece(p)

    #this function check the entire column the player acted on for a winner
    def checkVertical(self, player, column):
        c = self.board[column]
        i = -1
        
        #these just check upwards from the bottom
        if c[i] == c[i-1] == c[i-2] == c[i-3]:
                self.win(player)
        if c[i-1] != 0 and c[i-1] == c[i-2] == c[i-3] == c[i-4]:
                self.win(player)
        if c[i-2] != 0 and c[i-2] == c[i-3] == c[i-4] == c[i-5]:
                self.win(player)

        #instead of following an origin, this checks the entire row for any winners			
    def checkHorizontal(self, player, row):
        # variables for each column
        a = self.board[0]
        b = self.board[1]
        c = self.board[2]
        d = self.board[3]
        e = self.board[4]
        f = self.board[5]
        g = self.board[6]
        self.row = row
        
        #calls each possible win on every column for the row that the player affected
        if a[row]!=0 and a[row] == b[row] == c[row] == d[row]:
                self.win(player)
        if b[row]!=0 and b[row] == c[row] == d[row] == e[row]:
                self.win(player)
        if c[row]!=0 and c[row] == d[row] == e[row] == f[row]:
                self.win(player)
        if d[row]!=0 and d[row] == e[row] == f[row] == g[row]:
                self.win(player)

    # this checks in an x formation from the last added value(an origin)
    def checkDiagnalOrigin(self, player, column, row):
        a = self.board[column]
        
        #some of these restrictions were created because it crashes when checking outside the range of the array
        
        #don't need to check to the left 
        if column < 4:
                b = self.board[column + 1]
                c = self.board[column + 2]
                d = self.board[column + 3]
                
        #don't need to check to the right
        if column > 2:	
                e = self.board[column - 1]
                f = self.board[column - 2]
                g = self.board[column - 3]
        
        #Checking left and up
        if column > 2 and row > -5:	
                if a[row] == e[row-1] == f[row-2] == g[row-3]:
                        self.win(player)		
        #Checking right and up
        if column < 4 and row > -5:	
                if a[row] == b[row-1] == c[row-2] == d[row-3]:
                        self.win(player)
        #Checking left and down
        if column > 2:			
                if a[row] == e[row+1] == f[row+2] == g[row+3]:
                        self.win(player)
        #Checking right and down
        if column < 4:	
                if a[row] == b[row+1] == c[row+2] == d[row+3]:
                        self.win(player)
                        
    #this checks from the orgin with the assumption it is the middle value creating a diagnol				
    def checkDiagnalMiddle(self, player, column, row):
            a = self.board[column]
            
            #these restrictions were created because it crashes when checking outside the range of the array
            # makes sure you can't go too far to the right
            if column < 6:
                    b = self.board[column + 1]
                    
            if column < 5:
                    c = self.board[column + 2]
                    
            # makes sure you can't go too far to the left
            if column > 0:
                    e = self.board[column - 1]
                    
            if column > 1:
                    f = self.board[column - 2]
                    
            # checking left and up
            if column > 1 and row > -5:	
                    if a[row] == e[row-1] == f[row-2] == b[row+1]:
                            self.win(player)
                            
            # checking right and up
            if column < 5 and row > -5:	
                    if a[row] == b[row-1] == c[row-2] == e[row+1]:
                            self.win(player)
                            
            # checking left and down
            if column < 6 and column > 1 and row < 0:			
                    if a[row] == e[row+1] == f[row+2] == b[row-1]:
                            self.win(player)
                            
            # checking right and down
            if column > 0 and column < 5 and row < 0:	
                    if a[row] == b[row+1] == c[row+2] == e[row-1]:
                            self.win(player)

    # win function	
    def win(self, player):
        self.gameWon = True
        self.winner = player
        if DEBUG_LEVEL_1 == True:
            self.printBoard()
            print ('Player ' + self.winner + ' You Win!')
            
    # function that switches turns
    def switchTurn(self, player):
        if player == P1Piece.Player_1:
            self.turn = P2Piece.Player_2
        else:
            self.turn = P1Piece.Player_1

    # function that plays the game
    def play(self):
        self.createValuesBoard()
        self.turn = P1Piece.Player_1
        while self.gameWon == False:
            g.window.update_idletasks()
            g.window.update()
            if DEBUG_LEVEL_1 == True:
                print "False"
                self.printBoard()
                print
            if self.turn == P1Piece.Player_1:
                GPIO.output(leds[1], False)
                GPIO.output(leds[0], True)
            else:
                GPIO.output(leds[0], False)
                GPIO.output(leds[1], True)
            column = self.playerInput()
            self.drop(column, self.turn)
            self.switchTurn(self.turn)
        if self.winner == '1':
            destroyWidgets()
            Game.state = 4
        else:
            destroyWidgets()
            Game.state = 5
            
# global function used to change the game's state (doesn't work)
def changeState(button):
    if button == "start":
        destroyWidgets()
        Game.state = 2
        if DEBUG_LEVEL_1 == True:
            print "2"
            
    if button == "home":
        Game.state = 0
        
    if button == "quit":
        GPIO.cleanup()
        Game.window.destroy()

# function that is used to destroy all widgets on the current screen 
def destroyWidgets():
    for widget in Game.window.winfo_children():
            widget.destroy()

# class that creates the start menu
class StartMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.attributes("-fullscreen", True)
        self.setupGUI()
        
    # sets up the GUI for the start menu
    def setupGUI(self):
        # creates the logo at the top of the start menu
        connect4LogoImg = PhotoImage(file="Connect4Logo.gif")
        logo = Label(self.master, image=connect4LogoImg)
        logo.configure(background="white")
        logo.image = connect4LogoImg
        logo.pack(fill=BOTH, expand=1)

        # creates the start button in the midsection of the start menu
        startButtonImg = PhotoImage(file="StartButton.gif")
        start = Button(self.master, image=startButtonImg, command=lambda: changeState("start"))
        start.configure(background="white")
        start.image = startButtonImg
        start.pack(fill=BOTH, expand=1)

        # creates the quit button at the button of the start menu
        quitButtonImg = PhotoImage(file="QuitButton.gif")
        quitButton = Button(self.master, image=quitButtonImg, command=lambda: changeState("quit"))
        quitButton.configure(background="white")
        quitButton.image = quitButtonImg
        quitButton.pack(fill=BOTH, expand=1)

# class that composes the win screen for player 1
class Player1WinScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.attributes("-fullscreen", True)
        self.setupGUI()

    def setupGUI(self):     
        playerOneWinsImg = PhotoImage(file="PlayerOneWins.gif")
        logo = Label(self.master, image=playerOneWinsImg)
        logo.configure(background="white")
        logo.image = playerOneWinsImg
        logo.pack(fill=BOTH, expand=1)

# class that composes the win screen for player 2
class Player2WinScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.attributes("-fullscreen", True)
        self.setupGUI()

    def setupGUI(self):         
        playerTwoWinsImg = PhotoImage(file="PlayerTwoWins.gif")
        logo = Label(self.master, image=playerTwoWinsImg)
        logo.configure(background="white")
        logo.image = playerTwoWinsImg
        logo.pack(fill=BOTH, expand=1)
    

# class that runs the game
class Game(object):
    states = {"create start menu": 0, "remain on start menu": 1, "create grid": 2, "play game": 3,\
              "player 1 win screen": 4, "player 2 win screen": 5, "return to start menu": 6}
    state = 0
    def __init__(self, state = 0):
        Game.window = Tk()
        Game.state = state
        self.checkState()

    # function to check what state the game is in
    def checkState(self):
        if Game.state == 0:
            self.startMenu = StartMenu(Game.window)
            Game.state = Game.states["remain on start menu"]
        elif Game.state == 1:
            if DEBUG_LEVEL_1 == True:
               print "1"
        elif Game.state == 2:
            self.grid = Grid(Game.window)
            Game.state = Game.states["play game"]
        elif Game.state == 3:
            if DEBUG_LEVEL_1 == True:
                print "3"
            self.grid.play()
        elif Game.state == 4:
            self.winScreen = Player1WinScreen(Game.window)
            Game.state = Game.states["return to start menu"]
        elif Game.state == 5:
            self.winScreen = Player2WinScreen(Game.window)
            Game.state = Game.states["return to start menu"]
        elif Game.state == 6:
            sleep(5)
            destroyWidgets()
            Game.state = Game.states["create start menu"]

# MAIN PART OF PROGRAM             
g = Game()
while True:
    g.checkState()
    g.window.update_idletasks()
    g.window.update()
    sleep(0.001)
