# Made by brz

class Piece():

    def __init__(self, color, row, col):
        self.color  = color
        self.row    = row
        self.col    = col
        self.points  = 0
        self.rivals = []

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 10

    def make_a_jump(self):
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
        else:
            return None


    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = rival_row - self.row
        n_squares_col = abs(rival_col - self.col)

        if self.color == 'black' and n_squares_row == 1 and n_squares_col == 1:
            return True
        elif self.color == 'white' and n_squares_row == -1 and n_squares_col == 1:
            return True
        else:
            return None

class Horse(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 30

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = rival_row - self.row
        n_squares_col = rival_col - self.col

        # print(n_squares_row, n_squares_col)

        # if n_squares_row > 0 and n_squares_col == 0 or n_squares_row == 0 and n_squares_col >= 1:
        #     return True
        # else:
        #     return None

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 40

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = abs(rival_row - self.row)
        n_squares_col = abs(rival_col - self.col)

        if n_squares_row == n_squares_col:
            return True
        else:
            return None

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 60

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = rival_row - self.row
        n_squares_col = rival_col - self.col

        if n_squares_row > 0 and n_squares_col == 0 or n_squares_row == 0 and n_squares_col >= 1:
            return True
        else:
            return None

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 5

    def valid_move_capture(self, rival_row, rival_col):
        return True

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.points = 100

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = rival_row - self.row
        n_squares_col = rival_col - self.col

        if n_squares_row <= 1 and n_squares_col <= 1:
            return True

        return False

class EmptySquare():
    # Constrains
    # It can be in any place in the board

    def __init__(self, row, col):
        self.row  = row
        self.col  = col
