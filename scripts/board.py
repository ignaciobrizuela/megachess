from scripts import pieces
import numpy as np

class Board():

    def __init__(self, board_str):
        # Board array
        self.matrix = convert_board_matrix(board_str)
        # Black pieces
        self.black_pawns      = []
        self.black_horses     = []
        self.black_bishops    = []
        self.black_rooks      = []
        self.black_queens     = []
        self.black_kings      = []
        # White pieces
        self.white_pawns      = []
        self.white_horses     = []
        self.white_bishops    = []
        self.white_rooks      = []
        self.white_queens     = []
        self.white_kings      = []
        # Empty squares
        self.empty_squares    = []
        
        # Get pieces
        self.get_pieces_from_board()
        
    def get_pieces_from_board(self):

        for row, pieces_row in enumerate(self.matrix):
            for col, piece in enumerate(pieces_row):
                # Creates a list with black pieces
                if piece == 'p':
                    self.black_pawns.append(pieces.Pawn(piece, 'black', row, col))
                elif piece == 'h':
                    self.black_horses.append(pieces.Horse(piece, 'black', row, col))
                elif piece == 'b':
                    self.black_bishops.append(pieces.Bishop(piece, 'black', row, col))
                elif piece == 'r':
                    self.black_rooks.append(pieces.Rook(piece, 'black', row, col))
                elif piece == 'q':
                    self.black_queens.append(pieces.Queen(piece, 'black', row, col))
                elif piece == 'k':
                    self.black_kings.append(pieces.King(piece, 'black', row, col))

                # Creates a list with white pieces
                elif piece == 'P':
                    self.white_pawns.append(pieces.Pawn(piece, 'white', row, col))
                elif piece == 'H':
                    self.white_horses.append(pieces.Horse(piece, 'white', row, col))
                elif piece == 'B':
                    self.white_bishops.append(pieces.Bishop(piece, 'white', row, col))
                elif piece == 'R':
                    self.white_rooks.append(pieces.Rook(piece, 'white', row, col))
                elif piece == 'Q':
                    self.white_queens.append(pieces.Queen(piece, 'white', row, col))
                elif piece == 'K':
                    self.white_kings.append(pieces.King(piece, 'white', row, col))

                # Creates a list with empty squares
                else:
                    self.empty_squares.append(pieces.EmptySquare(row, col))


def convert_board_matrix(board_str):
    # Board splitted in rows and columns, easy to find pieces
    matrix = np.array(list(board_str), dtype=str)
    matrix = matrix.reshape(16,16)

    return matrix
