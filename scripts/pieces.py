# Made by brz

class Piece():

    def __init__(self, color, row, col):
        self.color  = color     # True == white, False == black
        self.row    = row
        self.col    = col
        self.point_move  = 0
        self.point_been_captured  = 0
        self.rivals = []

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.point_move = 10
        self.point_been_captured = 100

    def make_a_jump(self):
        if self.color == False:
            if self.row == 3:
                return 2
            else:
                return 1

        elif self.color == True:
            if self.row == 12:
                return -2
            else:
                return -1
        else:
            return None

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
        self.point_been_captured = 300

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
        self.point_been_captured = 400

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
        self.point_been_captured = 600

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
        self.point_been_captured = 800

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
        self.point_been_captured = 990

    def valid_move(self, element_in_square):
        n_squares_row = abs(element_in_square.row - self.row)
        n_squares_col = abs(element_in_square.col - self.col)

        if n_squares_row <= 1 and n_squares_col <= 1:
            return True

        return False

class EmptySquare():
    # Constrains
    # It can be in any place in the board

    def __init__(self, row, col):
        self.row  = row
        self.col  = col
        self.color = None