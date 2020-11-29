# Made by brz
import asyncio
from scripts import pieces


play_moves = []

def set_score(piece, element_in_square, color):
    factor = 1 if piece.color == color else -1
    
    if isinstance(element_in_square, pieces.EmptySquare):
        points = piece.points 
        score = points * factor
    else:
        score = element_in_square.points * 10 * factor

    play = {'piece_row': piece.row, 
            'piece_col': piece.col,
            'rival_row': element_in_square.row,
            'rival_col': element_in_square.col,
            'score': score}
    play_moves.append(play)


def get_score():
    return play_moves


def clear_score():
    play_moves = []


def scan_up(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'

    for row in reversed(range(0, piece.row)):
        element_in_square = board.matrix_pieces[row][piece.col]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break


def scan_down(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'

    for row in range(piece.row+1, 16):
        element_in_square = board.matrix_pieces[row][piece.col]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break


def scan_right(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'

    for col in range(piece.col+1, 16):
        element_in_square = board.matrix_pieces[piece.row][col]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break


def scan_left(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'

    for col in reversed(range(0, piece.col-1)):
        element_in_square = board.matrix_pieces[piece.row][col]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break

def scan_up_right(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'
    n = min(piece.row, 15-piece.col)

    for i in range(1, n+1):
        element_in_square = board.matrix_pieces[piece.row-i][piece.col+i]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break

def scan_up_left(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'
    n = min(piece.row, piece.col)

    for i in range(1, n+1):
        element_in_square = board.matrix_pieces[piece.row-i][piece.col-i]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break

def scan_down_right(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'
    n = min(15-piece.row, 15-piece.col)

    for i in range(1, n+1):
        element_in_square = board.matrix_pieces[piece.row+i][piece.col+i]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break


def scan_down_left(board, piece, color):
    rival_color = 'black' if color == 'white' else 'white'
    n = min(15-piece.row, piece.col)

    for i in range(1, n+1):
        element_in_square = board.matrix_pieces[piece.row+i][piece.col-i]
        if element_in_square.color == rival_color:
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
                break
        elif isinstance(element_in_square, pieces.EmptySquare):
            if piece.valid_move(element_in_square):
                set_score(piece, element_in_square, color)
        else:
            break


def can_capture(piece, rival):
    if piece.valid_move(rival):
        return True
    else:
        return False