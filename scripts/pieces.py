# Made by brz

class Piece():

    def __init__(self, color, row, col):
        if valid_color(color):
            self.color  = color     # True == white, False == black
        else:
            raise Exception("Color must be True(white) or False(black)")

        if valid_row(row):
            self.row    = row
        else:
            raise Exception("Row must be an integer from 0 to 15")

        if valid_col(col):
            self.col    = col
        else:
            raise Exception("Col must be an integer from 0 to 15")

        self.point_move  = 0
        self.point_been_captured  = 0

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 10
        self.point_been_captured = 10

    def valid_move(self, element_in_square):
        n_squares_row = element_in_square.row - self.row
        n_squares_col = abs(element_in_square.col - self.col)

        # If it is a black piece
        if self.color == False:
            # Given an empty square
            if isinstance(element_in_square, EmptySquare):
                # From row 3 can jump 2 or 1 squares.
                if self.row == 3 and n_squares_row == (2 or 1) and n_squares_col == 0:
                    return True
                # From any other row can jump only 1.
                elif n_squares_row == 1 and n_squares_col == 0:
                    return True
                else:
                    return False
            # Can capture pieces in diagonal
            elif n_squares_row == 1 and n_squares_col == 1:
                return True
            else:
                return False

        # If it is a white piece
        if self.color == True:
            # Given an empty square
            if isinstance(element_in_square, EmptySquare):
                # From row 12 can jump 2 or 1 squares.
                if self.row == 12 and n_squares_row == (-2 or 1) and n_squares_col == 0:
                    return True
                # From any other row can jump only 1.
                elif n_squares_row == -1 and n_squares_col == 0:
                    return True
                else:
                    return False
            # Can capture pieces in diagonal
            elif n_squares_row == -1 and n_squares_col == 1:
                return True
            else:
                return False


class Horse(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 7
        self.point_been_captured = 30

    def valid_move(self, element_in_square):
        n_squares_row = abs(element_in_square.row - self.row)
        n_squares_col = abs(element_in_square.col - self.col)

        if (n_squares_row == 2 and n_squares_col == 1) or (n_squares_row == 1 and n_squares_col == 2):
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 8
        self.point_been_captured = 40

    def valid_move(self, element_in_square):
        n_squares_row = abs(element_in_square.row - self.row)
        n_squares_col = abs(element_in_square.col - self.col)

        if n_squares_row == n_squares_col:
            return True
        else:
            return False

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 9
        self.point_been_captured = 60

    def valid_move(self, element_in_square):
        n_squares_row = abs(element_in_square.row - self.row)
        n_squares_col = abs(element_in_square.col - self.col)

        if (n_squares_row > 0 and n_squares_col == 0) or (n_squares_row == 0 and n_squares_col > 0):
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 6
        self.point_been_captured = 80

    def valid_move(self, element_in_square):
        n_row = abs(element_in_square.row - self.row)
        n_col = abs(element_in_square.col - self.col)

        if n_row > 0 and n_col == 0:
            return True
        elif n_row == 0 and n_col > 0:
            return True
        elif n_row == n_col:
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 5
        self.point_been_captured = 99

    def valid_move(self, element_in_square):
        n_squares_row = abs(element_in_square.row - self.row)
        n_squares_col = abs(element_in_square.col - self.col)
    
        if n_squares_row <= 1 and n_squares_col <= 1:
            return True
        else:
            return False

class EmptySquare():
    # Constrains
    # It can be in any place in the board

    def __init__(self, row, col):
        self.row  = row
        self.col  = col
        self.color = None
        self.point_been_captured = 0

def valid_color(color):
    if color == True or color == False:
        return True
    else:
        return False

def valid_row(row):
    if isinstance(row, int):
        if 0 <= row <= 15:
            return True
        else:
            return False

def valid_col(col):
    if isinstance(col, int):
        if 0 <= col <= 15:
            return True
        else:
            return False


bishop = Bishop(False, 7, 7)