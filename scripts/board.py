from scripts import pieces
import numpy as np

class Board():

    def __init__(self, board_str):
        # Board array
        self.matrix = convert_board_matrix(board_str)
        self.matrix_pieces = np.full((16, 16), pieces.Piece('black',0,0))
        
        # Get pieces
        self.complete_matrix_pieces()
        
    def complete_matrix_pieces(self):

        for row, pieces_row in enumerate(self.matrix):
            for col, piece in enumerate(pieces_row):
                # Creates a list with black pieces
                if piece == 'p':
                    black_pawn = pieces.Pawn('black', row, col)
                    self.black_pawns.append(black_pawn)
                    self.matrix_pieces[row][col] = black_pawn
                elif piece == 'h':
                    black_horse = pieces.Horse('black', row, col)
                    self.black_horses.append(black_horse)
                    self.matrix_pieces[row][col] = black_horse
                elif piece == 'b':
                    black_bishop = pieces.Bishop('black', row, col)
                    self.black_bishops.append(black_bishop)
                    self.matrix_pieces[row][col] = black_bishop
                elif piece == 'r':
                    black_rook = pieces.Rook('black', row, col)
                    self.black_rooks.append(black_rook)
                    self.matrix_pieces[row][col] = black_rook
                elif piece == 'q':
                    black_queen = pieces.Queen('black', row, col)
                    self.black_queens.append(black_queen)
                    self.matrix_pieces[row][col] = black_queen
                elif piece == 'k':
                    black_king = pieces.King('black', row, col)
                    self.black_kings.append(black_king)
                    self.matrix_pieces[row][col] = black_king

                # Creates a list with white pieces
                elif piece == 'P':
                    white_pawn = pieces.Pawn('white', row, col)
                    self.white_pawns.append(white_pawn)
                    self.matrix_pieces[row][col] = white_pawn
                elif piece == 'H':
                    white_horse = pieces.Horse('white', row, col)
                    self.white_horses.append(white_horse)
                    self.matrix_pieces[row][col] = white_horse
                elif piece == 'B':
                    white_bishop = pieces.Bishop('white', row, col)
                    self.white_bishops.append(white_bishop)
                    self.matrix_pieces[row][col] = white_bishop
                elif piece == 'R':
                    white_rook = pieces.Rook('white', row, col)
                    self.white_rooks.append(white_rook)
                    self.matrix_pieces[row][col] = white_rook
                elif piece == 'Q':
                    white_queen = pieces.Queen('white', row, col)
                    self.white_queens.append(white_queen)
                    self.matrix_pieces[row][col] = white_queen
                elif piece == 'K':
                    white_king = pieces.King('white', row, col)
                    self.white_kings.append(white_king)
                    self.matrix_pieces[row][col] = white_king

                # Creates a list with empty squares
                else:
                    empty_square = pieces.EmptySquare(row, col)
                    self.empty_squares.append(empty_square)
                    self.matrix_pieces[row][col] = empty_square

    def get_piece(self, row, col):
        return self.matrix[row][col]


def convert_board_matrix(board_str):
    # Board splitted in rows and columns, easy to find pieces
    matrix = np.array(list(board_str), dtype=str)
    matrix = matrix.reshape(16,16)

    return matrix
