# Made by brz
import asyncio
from scripts import board
from scripts import moves
from scripts import pieces
import numpy as np 

play_moves = []
play = {}

def set_score(piece, rival):
    print(rival.points)
    score = rival.points * 10
    play = {'piece_row': piece.row, 
            'piece_col': piece.col,
            'rival_row': rival.row,
            'rival_col': rival.col,
            'score': score}
    play_moves.append(play)

def get_score():
    return play_moves

def minimax(actual_board, color):
    rival = None

    for i in range(16):
        for j in range(16):
            piece = actual_board.matrix_pieces[i][j]
            if not isinstance(piece, pieces.EmptySquare):
                # print('piece', piece.row, piece.col)
                try:
                    row, col = moves.rival_up_right(actual_board, piece)
                    rival = actual_board.matrix_pieces[row][col]
                    print(rival.row, rival.col)
                except Exception as e:
                    rival = None

            if rival != None:
                if moves.can_capture(piece, rival):
                    set_score(piece, rival)
                elif moves.can_capture(rival, piece):
                    set_score(rival, piece)
            
            rival = None


board1 = (  'rrhhbbqqkkbbhhrr'
            'rrhhbbqqkkbbhhrr'
            ' ppppppppppppppp'
            ' ppppppppppppppp' 
            '                '
            '                '
            '                '
            ' p              ' 
            'P              q'
            '                '
            '                '
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
        print(s['score'])

play(board1, color)
# actual_board = board.Board(board1)
# pawn = pieces.Pawn('white', 8, 0)
# row, col = moves.rival_up_right(actual_board, pawn)
# rival = actual_board.matrix_pieces[row][col]
# print(moves.can_capture(pawn, rival))
# print(moves.can_capture(rival, pawn))
# print(actual_board.matrix_pieces)