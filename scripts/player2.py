# Made by brz
import asyncio
from scripts import board
import numpy as np 
from scripts import pieces
from scripts import scans
from scripts import score
from copy import deepcopy
import operator

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
            if isinstance(piece, pieces.Horse):
                if result.color != piece.color:
                    if piece.valid_move(result):
                        actual_score.set_score(piece, result, color)

            elif result.color != piece.color:
                if piece.valid_move(result):
                    actual_score.set_score(piece, result, color)
                    stop = True
                else:
                    stop = True

            else:
                if piece.valid_move(result):
                    actual_score.set_score(piece, result, color)
                    stop = True
                else:
                    stop = True


def evaluate_better_move(actual_board, actual_score, color):
    move_score = ([])
    next_score = score.Score()

    for s in actual_score.play_moves:
        if s['score'] > 0:
            next_board = deepcopy(actual_board)
            next_board.matrix_pieces[s['to_row']][s['to_col']] = next_board.matrix_pieces[s['from_row']][s['from_col']]
            next_board.matrix_pieces[s['from_row']][s['from_col']] = pieces.EmptySquare(s['from_row'],s['from_col'])
            next_score = scan_posible_moves(next_board, color)
            
            max_move_now, _ = minimax(actual_score)
            max_move, min_move = minimax(next_score)
            points = s['score'] * 2 + max_move['score'] + min_move['score']
            move_score.append([s, points])

    return move_score


def scan_posible_moves(actual_board, color):
    new_score = score.Score()

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
                L           = scans.scan_L(actual_board, piece)

                scan(new_score, up, piece, color)
                scan(new_score, up_right, piece, color)
                scan(new_score, right, piece, color)
                scan(new_score, down_right, piece, color)
                scan(new_score, down, piece, color)
                scan(new_score, down_left, piece, color)
                scan(new_score, left, piece, color)
                scan(new_score, up_left, piece, color)
                scan(new_score, L, piece, color)

    return new_score


def minimax(actual_score):
    scores = [s['score'] for s in actual_score.play_moves]
    play_max_score = scores.index(max(scores))
    play_min_score = scores.index(min(scores))

    return  actual_score.play_moves[play_max_score], actual_score.play_moves[play_min_score]
                        


writer = open('game.txt', 'w')

def play(actual_board, color):

    from_row, from_col, to_row, to_col = (0, 0, 0, 0)
    actual_board = board.Board(actual_board)
    writer.write(str(actual_board.matrix))
    writer.write('\n')

    print(actual_board.matrix)

    scores = scan_posible_moves(actual_board, color)

    max_move, min_move = minimax(scores)

    moves = evaluate_better_move(actual_board, scores, color)

    better_move = max(moves, key=operator.itemgetter(1))
    move = better_move[0]
    print(move)


    writer.write(str(move))
    writer.write('\n')

    return move['from_row'], move['from_col'], move['to_row'], move['to_col']