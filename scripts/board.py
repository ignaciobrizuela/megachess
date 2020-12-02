#Made by brz
from scripts import pieces
import numpy as np

class Board():

    def __init__(self, board_str):
        # Board array
        self.matrix = convert_board_matrix(board_str)
        self.matrix_pieces = np.full((16, 16), pieces.Piece(False,0,0))
        
        # Get pieces
        self.complete_matrix_pieces()
        
    def complete_matrix_pieces(self):

        for row, pieces_row in enumerate(self.matrix):
            for col, piece in enumerate(pieces_row):
                # Creates a list with black pieces
                if piece == 'p':
                    black_pawn = pieces.Pawn(False, row, col)
                    self.matrix_pieces[row][col] = black_pawn
                elif piece == 'h':
                    black_horse = pieces.Horse(False, row, col)
                    self.matrix_pieces[row][col] = black_horse
                elif piece == 'b':
                    black_bishop = pieces.Bishop(False, row, col)
                    self.matrix_pieces[row][col] = black_bishop
                elif piece == 'r':
                    black_rook = pieces.Rook(False, row, col)
                    self.matrix_pieces[row][col] = black_rook
                elif piece == 'q':
                    black_queen = pieces.Queen(False, row, col)
                    self.matrix_pieces[row][col] = black_queen
                elif piece == 'k':
                    black_king = pieces.King(False, row, col)
                    self.matrix_pieces[row][col] = black_king

                # Creates a list with white pieces
                elif piece == 'P':
                    white_pawn = pieces.Pawn(True, row, col)
                    self.matrix_pieces[row][col] = white_pawn
                elif piece == 'H':
                    white_horse = pieces.Horse(True, row, col)
                    self.matrix_pieces[row][col] = white_horse
                elif piece == 'B':
                    white_bishop = pieces.Bishop(True, row, col)
                    self.matrix_pieces[row][col] = white_bishop
                elif piece == 'R':
                    white_rook = pieces.Rook(True, row, col)
                    self.matrix_pieces[row][col] = white_rook
                elif piece == 'Q':
                    white_queen = pieces.Queen(True, row, col)
                    self.matrix_pieces[row][col] = white_queen
                elif piece == 'K':
                    white_king = pieces.King(True, row, col)
                    self.matrix_pieces[row][col] = white_king

                # Creates a list with empty squares
                else:
                    empty_square = pieces.EmptySquare(row, col)
                    self.matrix_pieces[row][col] = empty_square

    def get_piece(self, row, col):
        return self.matrix_pieces[row][col]


def convert_board_matrix(board_str):
    # Board splitted in rows and columns, easy to find pieces
    matrix = np.array(list(board_str), dtype=str)
    matrix = matrix.reshape(16,16)

    return matrix
