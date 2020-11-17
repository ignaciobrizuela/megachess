# Made by brz

import moves

class Piece():

    def __init__(self, tag, color, row, col):
        self.tag    = tag
        self.color  = color
        self.row    = row
        self.col    = col

class EmptySquare():
    # Constrains
    # It can be in any place in the board

    def __init__(self, row, col):
        self.row  = row
        self.col  = col
        self.tag = ' '
