class Chess(object):
    'An interactive cheesboard object indexed by tiles in rows A-H, and columns 1-8' 

    def __init__(self):
        'Constructor for the Chess class which initilizes chess piece variables with unicode and initilizes a dictionary with a key for each tile and the appropriate chesss piece for each key' 
        self.WPawn = '\u265f'; self.WRook = '\u265c'; self.WKnight = '\u265e'; self.WBishup = '\u265d'; self.WQueen = '\u265a'; self.WKing = '\u265b'; self.BPawn = '\u2659'; self.BRook = '\u2656'; self.BKnight = '\u2658'; self.BBishup = '\u2657'; self.BQueen = '\u2654'; self.BKing = '\u2655'; self.space = ' '
        self.locations = {'A1' : self.WRook, 'A2' : self.WKnight, 'A3' : self.WBishup, 'A4' : self.WKing, 'A5' : self.WQueen, 'A6' : self.WBishup, 'A7' : self.WKnight, 'A8' : self.WRook, 'B1' : self.WPawn, 'B2' : self.WPawn, 'B3' : self.WPawn, 'B4' : self.WPawn, 'B5' : self.WPawn, 'B6' : self.WPawn, 'B7' : self.WPawn, 'B8' : self.WPawn, 'C1' : self.space, 'C2' : self.space, 'C3' : self.space, 'C4' : self.space, 'C5' : self.space, 'C6' : self.space, 'C7' : self.space, 'C8' : self.space, 'D1' : self.space, 'D2' : self.space, 'D3' : self.space, 'D4' : self.space, 'D5' : self.space, 'D6' : self.space, 'D7' : self.space, 'D8' : self.space, 'E1' : self.space, 'E2' : self.space, 'E3' : self.space, 'E4' : self.space, 'E5' : self.space, 'E6' : self.space, 'E7' : self.space, 'E8' : self.space, 'F1' : self.space, 'F2' : self.space, 'F3' : self.space, 'F4' : self.space, 'F5' : self.space, 'F6' : self.space, 'F7' : self.space, 'F8' : self.space, 'G1' : self.BPawn, 'G2' : self.BPawn, 'G3' : self.BPawn, 'G4' : self.BPawn, 'G5' : self.BPawn, 'G6' : self.BPawn, 'G7' : self.BPawn, 'G8' : self.BPawn, 'H1' : self.BRook, 'H2' : self.BKnight, 'H3' : self.BBishup, 'H4' : self.BKing, 'H5' : self.BQueen, 'H6' : self.BBishup, 'H7' : self.BKnight, 'H8' : self.BRook} 

    def __str__(self):
        "returns a string representation of the board using -'s and |'s as a boarder"
        return f'''   1 2 3 4 5 6 7 8\n  -----------------\nA |{self.locations['A1']}|{self.locations['A2']}|{self.locations['A3']}|{self.locations['A4']}|{self.locations['A5']}|{self.locations['A6']}|{self.locations['A7']}|{self.locations['A8']}|\n  -----------------\nB |{self.locations['B1']}|{self.locations['B2']}|{self.locations['B3']}|{self.locations['B4']}|{self.locations['B5']}|{self.locations['B6']}|{self.locations['B7']}|{self.locations['B8']}|\n  -----------------\nC |{self.locations['C1']}|{self.locations['C2']}|{self.locations['C3']}|{self.locations['C4']}|{self.locations['C5']}|{self.locations['C6']}|{self.locations['C7']}|{self.locations['C8']}|\n  -----------------\nD |{self.locations['D1']}|{self.locations['D2']}|{self.locations['D3']}|{self.locations['D4']}|{self.locations['D5']}|{self.locations['D6']}|{self.locations['D7']}|{self.locations['D8']}|\n  -----------------\nE |{self.locations['E1']}|{self.locations['E2']}|{self.locations['E3']}|{self.locations['E4']}|{self.locations['E5']}|{self.locations['E6']}|{self.locations['E7']}|{self.locations['E8']}|\n  -----------------\nF |{self.locations['F1']}|{self.locations['F2']}|{self.locations['F3']}|{self.locations['F4']}|{self.locations['F5']}|{self.locations['F6']}|{self.locations['F7']}|{self.locations['F8']}|\n  -----------------\nG |{self.locations['G1']}|{self.locations['G2']}|{self.locations['G3']}|{self.locations['G4']}|{self.locations['G5']}|{self.locations['G6']}|{self.locations['G7']}|{self.locations['G8']}|\n  -----------------\nH |{self.locations['H1']}|{self.locations['H2']}|{self.locations['H3']}|{self.locations['H4']}|{self.locations['H5']}|{self.locations['H6']}|{self.locations['H7']}|{self.locations['H8']}|\n  -----------------'''

    def makeMove(self, color):
        "Make move allows a single move to be made for the color ('B' or 'W') and can be cancelled by entering 'done' in any case"
        willBreak = False
        while True:
            if color == 'W':
                side = 'White team'
                cTuple = (self.WPawn, self.WRook, self.WKnight, self.WBishup, self.WQueen, self.WKing)
                nTuple = (self.BPawn, self.BRook, self.BKnight, self.BBishup, self.BQueen, self.BKing)
            if color == 'B':
                side = 'Black team'
                cTuple = (self.BPawn, self.BRook, self.BKnight, self.BBishup, self.BQueen, self.BKing)
                nTuple = (self.WPawn, self.WRook, self.WKnight, self.WBishup, self.WQueen, self.WKing)
            choice = input(f'\n{side}, choose the tile of the piece you\'d like to move.\n\t').upper()
            if choice in self.locations.keys():
                if self.locations[choice] in cTuple:
                    while True:
                        secondChoice = input('\nWhich tile would you like to move your piece to?\n\t').upper()
                        if secondChoice.capitalize()  == 'Done':
                            willBreak = True
                            return ''
                        if secondChoice in self.locations.keys() and self.locations[secondChoice] not in cTuple:
                            self.locations[secondChoice] = self.locations[choice]
                            self.locations[choice] = self.space
                            willBreak = True
                            break
                        elif secondChoice in self.locations.keys():
                            print('You already have a piece there')
                        else:
                            print('That is not a valid tile index')
                    else:
                        print('That choice is invalid')
                        if choice.capitalize() == 'Done':
                            return ''
                else:
                    print('Your choice is invalid')
            elif choice.capitalize()  == 'Done':
                return ''
            if willBreak == True:
                willBreak = False
                break

    def playGame(self):
        "One call to playGame allows the user to play a game which ends when the string 'Done' is entered (not case sensitive)"
        UI = None
        color = 'B'
        print(self)
        while UI != '':
            if color == 'W':
                color = 'B'
            else:
                color = 'W'
            UI = self.makeMove(color)
            print(self)
a = Chess()
a.playGame()
