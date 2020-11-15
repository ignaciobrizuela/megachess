# Made by brz

import moves

class Pawn():
    # Constrains
    # 2 squares at first move from row 3 ('black'), 12('white).
    # 1 square in rectline for normal move.
    # 1 square in diagonal to capture a enemy piece.

    def __init__(self, color, row, col):
        self.color          = color
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        if self.color == 'white':
            return 'P'
        elif self.color == 'black':
            return 'p'

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col
    
class Horse():
    # Constrains
    # L movement

    def __init__(self, color, row, col):
        self.color          = color
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        if self.color == 'white':
            return 'H'
        elif self.color == 'black':
            return 'h'

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col    

class Bishop():
    # Constrains
    # n square in diagonal to move and capture a enemy piece.

    def __init__(self, color, row, col):
        self.color          = color
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        if self.color == 'white':
            return 'B'
        elif self.color == 'black':
            return 'b'

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col        

class Rook():
    # Constrains
    # n square in rectline to move and capture a enemy piece.

    def __init__(self, color, row, col):
        self.color          = color
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        if self.color == 'white':
            return 'R'
        elif self.color == 'black':
            return 'r'

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col


class Queen():
    # Constrains
    # n square in rectline to move and capture a enemy piece.
    # n square in diagonal to move and capture a enemy piece.

    def __init__(self, color, row, col):
        self.color          = color
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        if self.color == 'white':
            return 'Q'
        elif self.color == 'black':
            return 'q'

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col

class King():
    # Constrains
    # 1 square in rectline to move and capture a enemy piece.
    # 1 square in diagonal to move and capture a enemy piece.

    def __init__(self, color, row, col):
        self.color          = color
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        if self.color == 'white':
            return 'K'
        elif self.color == 'black':
            return 'k'

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col

class EmptySquare():
    # Constrains
    # It can be in any place in the board

    def __init__(self, row, col):
        self.row_possition  = row
        self.col_possition  = col
        self.tag = self.set_tag()

    def get_tag(self):
        return self.tag

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row_possition, self.col_possition

    def set_tag(self):
        return ' '

    def set_position(self, row, col):
        self.row_possition = row
        self.col_possition = col
