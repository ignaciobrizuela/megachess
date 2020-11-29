# Made by brz
import asyncio
from scripts import board
import numpy as np 
from scripts import pieces
from scripts import scans
from scripts import score

def scan(actual_score, scan_function, piece, color):
    stop = False

    while stop == False:
        try:
            result = next(scan_function)
        except Exception as e:
            break

        if isinstance(result, pieces.EmptySquare):
            if piece.valid_move(result):
                actual_score.set_score(piece, result, color)
            else:
                stop = True

        elif result.color != piece.color:
            if piece.valid_move(result):
                actual_score.set_score(piece, result, color)
                stop = True
            else:
                stop = True

        else:
            stop = True

def minimax(actual_board, color):
    actual_score = score.Score()

    for i in range(16):
        for j in range(16):
            piece = actual_board.matrix_pieces[i][j]
            if not isinstance(piece, pieces.EmptySquare):
                up          = scans.scan_up(actual_board, piece)
                up_right    = scans.scan_up_right(actual_board, piece)
                right       = scans.scan_right(actual_board, piece)
                down_right  = scans.scan_down_right(actual_board, piece)
                down        = scans.scan_down(actual_board, piece)
                down_left   = scans.scan_down_left(actual_board, piece)
                left        = scans.scan_left(actual_board, piece)
                up_left     = scans.scan_up_left(actual_board, piece)

                scan(actual_score, up, piece, color)
                scan(actual_score, up_right, piece, color)
                scan(actual_score, right, piece, color)
                scan(actual_score, down_right, piece, color)
                scan(actual_score, down, piece, color)
                scan(actual_score, down_left, piece, color)
                scan(actual_score, left, piece, color)
                scan(actual_score, up_left, piece, color)

    for s in actual_score.get_score():
        print(s)
                        


board1 = (  'rrhhbbqqkkbbhhrr'
            'rrhhbbqqkkbbhhrr'
            ' ppppppppppppppp'
            ' ppppppppppppppp' 
            '      Q         '
            '       b        '
            '                '
            ' p        p     ' 
            'P              q'
            '      Q   R b   '
            '         K      '
            '                ' 
            'PPPPPPPPPPPPPPPP'
            'PPPPPPPPPPPPPPPP'
            'RRHHBBQQKKBBHHRR'
            'RRHHBBQQKKBBHHRR')
            
color = True

def play(actual_board, color):
    actual_board = board.Board(actual_board)
    print(actual_board.matrix)
    minimax(actual_board, color)

play(board1, color)

# actual_board = board.Board(board1)

# piece = pieces.Rook(False, 1, 1)

# up          = scans.scan_up(actual_board, piece)
# up_right    = scans.scan_up_right(actual_board, piece)
# right       = scans.scan_right(actual_board, piece)
# down_right  = scans.scan_down_right(actual_board, piece)
# down        = scans.scan_down(actual_board, piece)
# down_left   = scans.scan_down_left(actual_board, piece)
# left        = scans.scan_left(actual_board, piece)
# up_left     = scans.scan_up_left(actual_board, piece)

# actual_score = score.Score()

# scan(actual_score, up, piece, color)
# scan(actual_score, up_right, piece, color)
# scan(actual_score, right, piece, color)
# scan(actual_score, down_right, piece, color)
# scan(actual_score, down, piece, color)
# scan(actual_score, down_left, piece, color)
# scan(actual_score, left, piece, color)
# scan(actual_score, up_left, piece, color)

# for s in actual_score.get_score():
#     print(s)

