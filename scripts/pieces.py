# Made by brz

class Piece():

    def __init__(self, color, row, col):
        self.color  = color
        self.row    = row
        self.col    = col
        self.rivals = []

class Pawn(Piece):

    def valid_move_jump(self, direction):
        if self.color == 'black' and direction == 'down':
            if self.row == 3:
                return 2
            else:
                return 1

        elif self.color == 'white' and direction == 'up':
            if self.row == 12:
                return -2
            else:
                return -1

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

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = rival_row - self.row
        n_squares_col = rival_col - self.col

        # print(n_squares_row, n_squares_col)

        # if n_squares_row > 0 and n_squares_col == 0 or n_squares_row == 0 and n_squares_col >= 1:
        #     return True
        # else:
        #     return None

class Bishop(Piece):

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = abs(rival_row - self.row)
        n_squares_col = abs(rival_col - self.col)

        if n_squares_row == n_squares_col:
            return True
        else:
            return None

class Rook(Piece):

    def valid_move_capture(self, rival_row, rival_col):
        n_squares_row = rival_row - self.row
        n_squares_col = rival_col - self.col

        if n_squares_row > 0 and n_squares_col == 0 or n_squares_row == 0 and n_squares_col >= 1:
            return True
        else:
            return None

class Queen(Piece):

    def valid_move_capture(self, rival_row, rival_col):
        return True

class King(Piece):

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
        self.tag = ' '
