#Made by brz
from scripts import pieces
import numpy as np

PRETTY_PIECES = {
    'p': '♟',
    'P': '♙',
    'r': '♜',
    'R': '♖',
    'k': '♚',
    'K': '♔',
    'h': '♞',
    'H': '♘',
    'b': '♝',
    'B': '♗',
    'q': '♛',
    'Q': '♕',
    ' ': ' ',
}

class Board():

    def __init__(self, board_str):
        # Board array
        self.matrix = convert_board_matrix(board_str)
        self.matrix_pieces = np.full((16, 16), pieces.Piece(False,0,0))
        
        # Transform from str to pieces
        self.complete_matrix_pieces()
        
    def complete_matrix_pieces(self):

        for row, pieces_row in enumerate(self.matrix):
            for col, piece in enumerate(pieces_row):
                # Creates a list with black pieces
                if piece == '♟':
                    black_pawn = pieces.Pawn(False, row, col)
                    self.matrix_pieces[row][col] = black_pawn
                elif piece == '♞':
                    black_horse = pieces.Horse(False, row, col)
                    self.matrix_pieces[row][col] = black_horse
                elif piece == '♝':
                    black_bishop = pieces.Bishop(False, row, col)
                    self.matrix_pieces[row][col] = black_bishop
                elif piece == '♜':
                    black_rook = pieces.Rook(False, row, col)
                    self.matrix_pieces[row][col] = black_rook
                elif piece == '♛':
                    black_queen = pieces.Queen(False, row, col)
                    self.matrix_pieces[row][col] = black_queen
                elif piece == '♚':
                    black_king = pieces.King(False, row, col)
                    self.matrix_pieces[row][col] = black_king

                # Creates a list with white pieces
                elif piece == '♙':
                    white_pawn = pieces.Pawn(True, row, col)
                    self.matrix_pieces[row][col] = white_pawn
                elif piece == '♘':
                    white_horse = pieces.Horse(True, row, col)
                    self.matrix_pieces[row][col] = white_horse
                elif piece == '♗':
                    white_bishop = pieces.Bishop(True, row, col)
                    self.matrix_pieces[row][col] = white_bishop
                elif piece == '♖':
                    white_rook = pieces.Rook(True, row, col)
                    self.matrix_pieces[row][col] = white_rook
                elif piece == '♕':
                    white_queen = pieces.Queen(True, row, col)
                    self.matrix_pieces[row][col] = white_queen
                elif piece == '♔':
                    white_king = pieces.King(True, row, col)
                    self.matrix_pieces[row][col] = white_king

                # Creates a list with empty squares
                else:
                    empty_square = pieces.EmptySquare(row, col)
                    self.matrix_pieces[row][col] = empty_square


def convert_board_matrix(board_str):
    # Board splitted in rows and columns, easy to find pieces
    matrix = np.array(list(board_str), dtype=str)
    matrix = matrix.reshape(16,16)

    return matrix

def transform_pretty_pieces(board_str):
    board_pretty = board_str.replace('p', PRETTY_PIECES['p'])
    board_pretty = board_pretty.replace('P', PRETTY_PIECES['P'])
    board_pretty = board_pretty.replace('r', PRETTY_PIECES['r'])
    board_pretty = board_pretty.replace('R', PRETTY_PIECES['R'])
    board_pretty = board_pretty.replace('k', PRETTY_PIECES['k'])
    board_pretty = board_pretty.replace('K', PRETTY_PIECES['K'])
    board_pretty = board_pretty.replace('h', PRETTY_PIECES['h'])
    board_pretty = board_pretty.replace('H', PRETTY_PIECES['H'])
    board_pretty = board_pretty.replace('b', PRETTY_PIECES['b'])
    board_pretty = board_pretty.replace('B', PRETTY_PIECES['B'])
    board_pretty = board_pretty.replace('q', PRETTY_PIECES['q'])
    board_pretty = board_pretty.replace('Q', PRETTY_PIECES['Q'])
    
    return board_pretty