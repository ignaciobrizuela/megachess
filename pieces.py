# Made by brz

class Piece():

    def __init__(self, tag, color, row, col):
        self.tag    = tag
        self.color  = color
        self.row    = row
        self.col    = col
        self.rivals = []

class Pawn(Piece):

    def valid_move_jump(self):
        if self.color == 'black':
            if self.row == 3:
                return 2
            else:
                return 1

        elif self.color == 'white':
            if self.row == 12:
                return -2
            else:
                return -1

class Queen(Piece):

    def valid_move_jump(self):
        if self.color == 'black':
            if self.row == 3:
                return 2
            else:
                return 1

        elif self.color == 'white':
            if self.row == 12:
                return -2
            else:
                return -1

class EmptySquare():
    # Constrains
    # It can be in any place in the board

    def __init__(self, row, col):
        self.row  = row
        self.col  = col
        self.tag = ' '
