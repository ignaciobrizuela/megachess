# Made by brz
import asyncio
from scripts import pieces


play_moves = []

def set_score(piece, rival, color):
    factor = 1 if piece.color == color else -1
    score = rival.points * 10 * factor

    play = {'piece_row': piece.row, 
            'piece_col': piece.col,
            'rival_row': rival.row,
            'rival_col': rival.col,
            'score': score}
    play_moves.append(play)

def set_score_jump(piece, rival, color):
    score = piece.points 

    play = {'piece_row': piece.row, 
            'piece_col': piece.col,
            'rival_row': rival.row,
            'rival_col': rival.col,
            'score': score}
    play_moves.append(play)

def get_score():
    return play_moves

def scan_up(board, piece):
    # Get the whole piece column
    column = board.matrix[:,piece.col]

    # Iterate each item from the piece row until zero
    for i in reversed(range(0, piece.row)):
        # If my piece is black, look for a white piece
        if piece.color == 'black':
            if column[i].isupper():
                board.matrix_pieces[i][piece.col]
                if can_capture(piece, rival):
                    set_score(piece, rival, color)
            # If there is one black piece on the way, there is no rival
            elif column[i] == ' ':
                piece.valid_move()
        elif piece.color == 'white':
            if column[i].islower():
                return i, piece.col
            elif column[i].isupper():
                return None
            
    return None


def scan_down(board, piece):
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

def scan_right(board, piece):
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

def scan_left(board, piece):
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

def scan_up_right(board, piece):
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

def scan_up_left(board, piece):
    n = min(piece.row, piece.col)

    for i in range(1, n+1):
        if piece.color == 'black':
            if board.matrix[piece.row-i][piece.col-i].isupper():
                return piece.row-i, piece.col-i
            elif board.matrix[piece.row-i][piece.col-i].islower():
                return None
        elif piece.color == 'white':
            if board.matrix[piece.row-i][piece.col-i].islower():
                return piece.row-i, piece.col-i
            elif board.matrix[piece.row-i][piece.col-i].isupper():
                return None
            
    return None

def scan_down_right(board, piece):
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

def scan_down_left(board, piece):
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


def can_capture(piece, rival):
    if piece.valid_move(rival):
        return True
    else:
        return False