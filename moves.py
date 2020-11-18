# Made by brz
import asyncio
import board
import pieces


def rival_up(board, piece):
    column = board.board_array[:,piece.col]

    for row in reversed(range(0, piece.row)):
        if column[row].isupper():
            return row, piece.col
        elif column[row].islower():
            return None
    
    return None


def rival_down(board, piece):
    column = board.board_array[:,piece.col]

    for row in range(piece.row+1, 16):
        if column[row].isupper():
            return row, piece.col
        elif column[row].islower():
            return None

    return None

def rival_right(board, piece):
    row = board.board_array[piece.row]

    for col in range(piece.col+1, 16):
        if row[col].isupper():
            return piece.row, col
        elif row[col].islower():
            return None
    
    return None

def rival_left(board, piece):
    row = board.board_array[piece.row]

    for col in reversed(range(0, piece.col)):
        if row[col].isupper():
            return piece.row, col
        elif row[col].islower():
            return None
    
    return None
