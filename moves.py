# Made by brz
import asyncio
import board
import pieces


def rival_up(board, piece):
    column = board.board_array[:,piece.col]

    for i in reversed(range(0, piece.row)):
        if piece.color == 'black':
            if column[i].isupper():
                return i, piece.col
            elif column[i].islower():
                return None
        elif piece.color == 'white':
            if column[i].islower():
                return i, piece.col
            elif column[i].isupper():
                return None
            
    return None


def rival_down(board, piece):
    column = board.board_array[:,piece.col]

    for row in range(piece.row+1, 16):
        if piece.color == 'black':
            if column[row].isupper():
                return row, piece.col
            elif column[row].islower():
                return None
        elif piece.color == 'white':
            if column[row].islower():
                return row, piece.col
            elif column[row].isupper():
                return None

    return None

def rival_right(board, piece):
    row = board.board_array[piece.row]

    for col in range(piece.col+1, 16):
        if piece.color == 'black':
            if row[col].isupper():
                return piece.row, col
            elif row[col].islower():
                return None
        elif piece.color == 'white':
            if row[col].islower():
                return piece.row, col
            elif row[col].isupper():
                return None
    
    return None

def rival_left(board, piece):
    row = board.board_array[piece.row]

    for col in reversed(range(0, piece.col)):
        if piece.color == 'black':
            if row[col].isupper():
                return piece.row, col
            elif row[col].islower():
                return None
        elif piece.color == 'white':
            if row[col].islower():
                return piece.row, col
            elif row[col].isupper():
                return None
    
    return None

def rival_up_right(board, piece):
    n = min(piece.row, 15-piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.board_array[piece.row-i][piece.col+i].isupper():
                return piece.row-i, piece.col+i
            elif board.board_array[piece.row-i][piece.col+i].islower():
                return None
        elif piece.color == 'white':
            if board.board_array[piece.row-i][piece.col+i].islower():
                return piece.row-i, piece.col+i
            elif board.board_array[piece.row-i][piece.col+i].isupper():
                return None
            
    return None

def rival_up_left(board, piece):
    n = min(piece.row, piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.board_array[piece.row-i][piece.col-i].isupper():
                return piece.row-i, piece.col+i
            elif board.board_array[piece.row-i][piece.col-i].islower():
                return None
        elif piece.color == 'white':
            if board.board_array[piece.row-i][piece.col-i].islower():
                return piece.row-i, piece.col-i
            elif board.board_array[piece.row-i][piece.col-i].isupper():
                return None
            
    return None

def rival_down_right(board, piece):
    n = min(15-piece.row, 15-piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.board_array[piece.row+i][piece.col+i].isupper():
                return piece.row+i, piece.col+i
            elif board.board_array[piece.row+i][piece.col+i].islower():
                return None
        elif piece.color == 'white':
            if board.board_array[piece.row+i][piece.col+i].islower():
                return piece.row+i, piece.col+i
            elif board.board_array[piece.row+i][piece.col+i].isupper():
                return None

    return None

def rival_down_left(board, piece):
    n = min(15-piece.row, piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.board_array[piece.row+i][piece.col-i].isupper():
                return piece.row+i, piece.col-i
            elif board.board_array[piece.row+i][piece.col-i].islower():
                return None
        elif piece.color == 'white':
            if board.board_array[piece.row+i][piece.col-i].islower():
                return piece.row+i, piece.col-i
            elif board.board_array[piece.row+i][piece.col-i].isupper():
                return None

    return None