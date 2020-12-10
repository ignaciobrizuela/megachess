# Made by brz
from scripts import pieces
from scripts import score


def scan_up(board, piece):
    for row in reversed(range(0, piece.row)):
        yield board.matrix_pieces[row][piece.col]


def scan_L(board, piece):
    s = ([-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1])
    for i in range(len(s)):
        yield board.matrix_pieces[piece.row+s[i][0]][piece.col+s[i][1]]


def scan_up_right(board, piece):
    n = min(piece.row, 15-piece.col)

    for i in range(1, n+1):
        yield board.matrix_pieces[piece.row-i][piece.col+i]


def scan_right(board, piece):
    for col in range(piece.col+1, 16):
        yield board.matrix_pieces[piece.row][col]


def scan_down_right(board, piece):
    n = min(15-piece.row, 15-piece.col)

    for i in range(1, n+1):
        yield board.matrix_pieces[piece.row+i][piece.col+i]


def scan_down(board, piece):
    for row in range(piece.row+1, 16):
        yield board.matrix_pieces[row][piece.col]


def scan_down_left(board, piece):
    n = min(15-piece.row, piece.col)

    for i in range(1, n+1):
        yield board.matrix_pieces[piece.row+i][piece.col-i]


def scan_left(board, piece):
    for col in reversed(range(0, piece.col)):
        yield board.matrix_pieces[piece.row][col]


def scan_up_left(board, piece):
    n = min(piece.row, piece.col)

    for i in range(1, n+1):
        yield board.matrix_pieces[piece.row-i][piece.col-i]
