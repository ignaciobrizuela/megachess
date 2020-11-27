# Made by brz
import asyncio
from scripts import pieces


def rival_up(board, piece):
    # Get the whole piece column
    column = board.matrix[:,piece.col]

    # Iterate each item from the piece row until zero
    for i in reversed(range(0, piece.row)):
        # If my piece is black, look for a white piece
        if piece.color == 'black':
            if column[i].isupper():
                return i, piece.col
            # If there is one black piece on the way, there is no rival
            elif column[i].islower():
                return None
        elif piece.color == 'white':
            if column[i].islower():
                return i, piece.col
            elif column[i].isupper():
                return None
            
    return None


def rival_down(board, piece):
    # Get the whole piece column
    column = board.matrix[:,piece.col]

    # Iterate each item from the piece row until 16
    for row in range(piece.row+1, 16):
        # If my piece is black, look for a white piece
        if piece.color == 'black':
            if column[row].isupper():
                return row, piece.col
            # If there is one black piece on the way, there is no rival
            elif column[row].islower():
                return None
        elif piece.color == 'white':
            if column[row].islower():
                return row, piece.col
            elif column[row].isupper():
                return None

    return None

def rival_right(board, piece):
    row = board.matrix[piece.row]

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
    row = board.matrix[piece.row]

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
    # Get the maximun diagonal number of squares that it can move
    n = min(piece.row, 15-piece.col)

    # i is the squares distance from my piece position
    for i in range(1, n+1):
        if piece.color == 'black':
            # Look for pieces in diagonal i distance from my piece position
            if board.matrix[piece.row-i][piece.col+i].isupper():
                return piece.row-i, piece.col+i
            elif board.matrix[piece.row-i][piece.col+i].islower():
                return None
        elif piece.color == 'white':
            if board.matrix[piece.row-i][piece.col+i].islower():
                return piece.row-i, piece.col+i
            elif board.matrix[piece.row-i][piece.col+i].isupper():
                return None
            
    return None

def rival_up_left(board, piece):
    n = min(piece.row, piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.matrix[piece.row-i][piece.col-i].isupper():
                return piece.row-i, piece.col+i
            elif board.matrix[piece.row-i][piece.col-i].islower():
                return None
        elif piece.color == 'white':
            if board.matrix[piece.row-i][piece.col-i].islower():
                return piece.row-i, piece.col-i
            elif board.matrix[piece.row-i][piece.col-i].isupper():
                return None
            
    return None

def rival_down_right(board, piece):
    n = min(15-piece.row, 15-piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.matrix[piece.row+i][piece.col+i].isupper():
                return piece.row+i, piece.col+i
            elif board.matrix[piece.row+i][piece.col+i].islower():
                return None
        elif piece.color == 'white':
            if board.matrix[piece.row+i][piece.col+i].islower():
                return piece.row+i, piece.col+i
            elif board.matrix[piece.row+i][piece.col+i].isupper():
                return None

    return None

def rival_down_left(board, piece):
    n = min(15-piece.row, piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.matrix[piece.row+i][piece.col-i].isupper():
                return piece.row+i, piece.col-i
            elif board.matrix[piece.row+i][piece.col-i].islower():
                return None
        elif piece.color == 'white':
            if board.matrix[piece.row+i][piece.col-i].islower():
                return piece.row+i, piece.col-i
            elif board.matrix[piece.row+i][piece.col-i].isupper():
                return None

    return None


def can_capture(pieces):
    for piece in pieces:
        for rival in piece.rivals:
            # print(piece.tag, piece.row, piece.col)
            # print('rival', rival[0], rival[1])
            # print(piece.valid_move_capture(rival[0], rival[1]))
            if rival != None and piece.valid_move_capture(rival[0], rival[1]):
                return piece.row, piece.col, rival[0], rival[1]
        
    return None