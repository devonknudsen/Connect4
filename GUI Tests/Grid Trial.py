from Tkinter import *
import RPi.GPIO as GPIO

DEBUG = True

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

plPieces = []
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

class P1Piece(Piece):
    Player_1 = '1'
    p1Color = "red"
    def __init__(self, x, y):
            Piece.__init__(self, x, y)

class P2Piece(Piece):
    Player_2 = '2'
    p2Color = "blue"
    def __init__(self, x, y):
            Piece.__init__(self, x, y)

# class that creates the game grid
class Grid(Canvas):
    window = Tk()
    
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
    ROW0_Y = 94
    ROW1_Y = 159
    ROW2_y = 224
    ROW3_Y = 289
    ROW4_Y = 354
    ROW5_Y = 419
    
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
        redXButton = Button(self, image=redXimg, command=Grid.window.destroy)
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
        self.create_oval(p.x, p.y, p.x + Piece.pieceRadius * 2, p.y + Piece.pieceRadius * 2, outline="black", fill=color)

    def createValuesBoard(self):
        self.columns = 7
        self.rows = 6
        self.board = [[0] * self.rows for _ in range(self.columns)]

    def printBoard(self):
        if DEBUG == True:
            for y in range(self.rows):
                print(' '.join(str(self.board[x][y]) for x in range(self.columns)))
        else:
            pass
        
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

    def drop(self, column, player):
        c = self.board[column]
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

        while c[i] != 0:
            i -= 1

        c[i] = player

        row = i

        self.checkVertical(column)
        self.checkHorizontal(row)
        self.checkDiagnalOrigin(column, row)
        self.checkDiagnalMiddle(column, row)

    #this function check the entire column the player acted on for a winner
    def checkVertical(self, column):
            self.column = column
            c = self.board[column]
            i = -1
            
            #these just check upwards from the bottom
            if c[i] == c[i-1] == c[i-2] == c[i-3]:
                    self.win()
            if c[i-1] != 0 and c[i-1] == c[i-2] == c[i-3] == c[i-4]:
                    self.win()
            if c[i-2] != 0 and c[i-2] == c[i-3] == c[i-4] == c[i-5]:
                    self.win()

        #instead of following an origin, this checks the entire row for any winners			
    def checkHorizontal(self, row):
            #variables for each column
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
                    self.win()
            if b[row]!=0 and b[row] == c[row] == d[row] == e[row]:
                    self.win()
            if c[row]!=0 and c[row] == d[row] == e[row] == f[row]:
                    self.win()
            if d[row]!=0 and d[row] == e[row] == f[row] == g[row]:
                    self.win()

#this checks in an x formation from the last added value(an origin)
    def checkDiagnalOrigin(self, column, row):
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
                        self.win()		
        #Checking right and up
        if column < 4 and row > -5:	
                if a[row] == b[row-1] == c[row-2] == d[row-3]:
                        self.win()
        #Checking left and down
        if column > 2:			
                if a[row] == e[row+1] == f[row+2] == g[row+3]:
                        self.win()
        #Checking right and down
        if column < 4:	
                if a[row] == b[row+1] == c[row+2] == d[row+3]:
                        self.win()
#this checks from the orgin with the assumption it is the middle value creating a diagnol				
    def checkDiagnalMiddle(self, column, row):
            self.row = row
            a = self.board[column]
            #these restrictions were created because it crashes when checking outside the range of the array
                    #makes sure you can't go too far to the right
            if column < 6:
                    b = self.board[column + 1]
            if column < 5:
                    c = self.board[column + 2]	
                    #makes sure you can't go too far to the left
            if column > 0:
                    e = self.board[column - 1]	
            if column > 1:
                    f = self.board[column - 2]
                    
            #Checking left and up
            if column > 1 and row > -5:	
                    if a[row] == e[row-1] == f[row-2] == b[row+1]:
                            self.win()		
            #Checking right and up
            if column < 5 and row > -5:	
                    if a[row] == b[row-1] == c[row-2] == e[row+1]:
                            self.win()
            #Checking left and down
            if column < 6 and column > 1 and row < 0:			
                    if a[row] == e[row+1] == f[row+2] == b[row-1]:
                            self.win()
            #Checking right and down
            if column > 0 and column < 5 and row < 0:	
                    if a[row] == b[row+1] == c[row+2] == e[row-1]:
                            self.win()

    #temp proof of win	
    def win(self):
            self.printBoard()
            if DEBUG == True:
                print 'You Win!'
            GPIO.cleanup()
            sys.exit()

    def switchTurn(self, player):
        if player == P1Piece.Player_1:
            self.turn = P2Piece.Player_2
        else:
            self.turn = P1Piece.Player_1
        
    def play(self):
        self.createValuesBoard()
        self.turn = P1Piece.Player_1
        while(True):
            if DEBUG == True:
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
            
g = Grid(Grid.window)
g.window.title("Connect 4")
if DEBUG == True:
    p1 = P1Piece(Grid.COLUMN0_X, Grid.ROW1_Y)
    p2 = P2Piece(Grid.COLUMN1_X, Grid.ROW5_Y)
    p2Pieces.append(p2)
    plPieces.append(p1)
    g.createPiece(p1)
    g.createPiece(p2)
g.window.mainloop()
#g.play()
