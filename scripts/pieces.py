# Made by brz

class Piece():

    def __init__(self, color, row, col):
        self.color  = color     # True == white, False == black
        self.row    = row
        self.col    = col
        self.points  = 0
        self.rivals = []

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 10

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

    def valid_move(self, rival):
        n_squares_row = rival.row - self.row
        n_squares_col = abs(rival.col - self.col)

        # If it is a black piece
        if self.color == False:
            # Given an empty square
            if isinstance(rival, EmptySquare):
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
            if isinstance(rival, EmptySquare):
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
        self.points = 30

    def valid_move(self, rival):
        n_squares_row = abs(rival.row - self.row)
        n_squares_col = abs(rival.col - self.col)

        if n_squares_row == 2 and n_squares_col == 1:
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 40

    def valid_move(self, rival):
        n_squares_row = abs(rival.row - self.row)
        n_squares_col = abs(rival.col - self.col)

        if n_squares_row == n_squares_col:
            return True
        else:
            return False

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 60

    def valid_move(self, rival):
        n_squares_row = abs(rival.row - self.row)
        n_squares_col = abs(rival.col - self.col)

        if (n_squares_row > 0 and n_squares_col == 0) or (n_squares_row == 0 and n_squares_col > 0):
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 5

    def valid_move(self, rival):
        return True

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 100

    def valid_move(self, rival):
        n_squares_row = rival.row - self.row
        n_squares_col = rival.col - self.col

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