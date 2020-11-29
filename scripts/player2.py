# Made by brz
import asyncio
from scripts import board
from scripts import moves
from scripts import pieces
import numpy as np 


def minimax(actual_board, color):
    rivals = []
    rival = None

    for i in range(16):
        for j in range(16):
            piece = actual_board.matrix_pieces[i][j]
            if not isinstance(piece, pieces.EmptySquare):
                piece.rivals.append(moves.scan_up(actual_board, piece))
                piece.rivals.append(moves.scan_up_right(actual_board, piece))
                piece.rivals.append(moves.scan_right(actual_board, piece))
                piece.rivals.append(moves.scan_down_right(actual_board, piece))
                piece.rivals.append(moves.scan_down(actual_board, piece))
                piece.rivals.append(moves.scan_down_left(actual_board, piece))
                piece.rivals.append(moves.scan_left(actual_board, piece))
                piece.rivals.append(moves.scan_up_left(actual_board, piece))

                for r in piece.rivals:
                    print(piece.row, piece.col, r)
                    try:
                        row, col = r
                        rival = actual_board.matrix_pieces[row][col]
                    except Exception as e:
                        rival = None

                    if rival != None:
                        if not isinstance(rival, pieces.EmptySquare):
                            # If I can capture my oponent piece
                            if moves.can_capture(piece, rival):
                                set_score(piece, rival, color)
                            # If I my oponent can capture my piece
                            if moves.can_capture(rival, piece):
                                set_score(rival, piece, color)
                            rival = None
                        


board1 = (  'rrhhbbqqkkbbhhrr'
            'rrhhbbqqkkbbhhrr'
            ' ppppppppppppppp'
            ' ppppppppppppppp' 
            '      Q         '
            '       b        '
            '                '
            ' p              ' 
            'P              q'
            '                '
            '        Kr      '
            '                ' 
            'PPPPPPPPPPPPPPPP'
            'PPPPPPPPPPPPPPPP'
            'RRHHBBQQKKBBHHRR'
            'RRHHBBQQKKBBHHRR')
            
color = 'white'

def play(actual_board, color):
    actual_board = board.Board(actual_board)
    print(actual_board.matrix)
    minimax(actual_board, color)
    scores = get_score()

    for s in scores:
        print(s)

# play(board1, color)

pawn = pieces.Pawn('white', 12, 1)
rival = pieces.Pawn('black', 11, 2)

print(pawn.valid_move(rival))