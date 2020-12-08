# Made by brz
import asyncio
from scripts import board
import numpy as np 
from scripts import pieces
from scripts import scans
from scripts import score
from copy import deepcopy
import operator

def scan(new_score, scan_function, piece, color):
    stop = False

    while stop == False:
        try:
            result = next(scan_function)
        except Exception as e:
            break
        
        # If the destiny is an empty square, keep looking
        if isinstance(result, pieces.EmptySquare):
            if piece.valid_move(result):
                new_score.set_score(piece, result, color)

        # If there is a piece in the square ask which one it is.
        else:
            # If it is a horse, look at every L move.
            if isinstance(piece, pieces.Horse):
                if result.color != piece.color:
                    if piece.valid_move(result):
                        new_score.set_score(piece, result, color)
            # If there is a rival piece set_score and stop
            elif result.color != piece.color:
                if piece.valid_move(result):
                    new_score.set_score(piece, result, color)
                    stop = True
                # If it is a team piece do nothing and stop
                else:
                    stop = True
            # If there is a team piece do nothing and stop
            else:
                stop = True


def evaluate_moves(actual_board, actual_score, color):
    move_score = ([])
    max_move_now, _ = minimax(actual_score)

    for s in actual_score.play_moves:
        # print('move',s)
        next_board = deepcopy(actual_board)
        if s['score'] > 0:
            piece_from = next_board.matrix_pieces[s['from_row']][s['from_col']]
            piece_from.row = s['to_row']
            piece_from.col = s['to_col']
            next_board.matrix_pieces[s['to_row']][s['to_col']] = piece_from
            next_board.matrix_pieces[s['from_row']][s['from_col']] = pieces.EmptySquare(s['from_row'],s['from_col'])

            next_score = scan_posible_moves(next_board, color)   #####################
            # for m in next_score.play_moves:
            #     print(m)
            
            max_move, min_move = minimax(next_score)
            points = s['score'] * 2 + max_move['score'] + min_move['score']
            move_score.append([s, round(points, 2)])
            # print('aca', s, max_move , min_move)
            # for m in move_score:
            #     print(m)

    return move_score


def best_move(moves):
    return max(moves, key=operator.itemgetter(1))

def scan_posible_moves(next_board, color):
    new_score = score.Score()

    for i in range(16):
        for j in range(16):
            piece = next_board.matrix_pieces[i][j]
            if not isinstance(piece, pieces.EmptySquare):
                up          = scans.scan_up(next_board, piece)
                up_right    = scans.scan_up_right(next_board, piece)
                right       = scans.scan_right(next_board, piece)
                down_right  = scans.scan_down_right(next_board, piece)
                down        = scans.scan_down(next_board, piece)
                down_left   = scans.scan_down_left(next_board, piece)
                left        = scans.scan_left(next_board, piece)
                up_left     = scans.scan_up_left(next_board, piece)
                L           = scans.scan_L(next_board, piece)

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
                        
# def show_board(board_pretty):
#     for row in range(0, 256, 16):
#         print(board_pretty[row:row+16])

writer = open('game.txt', 'w')

def play(board_str, color):

    from_row, from_col, to_row, to_col = (0, 0, 0, 0)

    board_pretty = board.transform_pretty_pieces(board_str)
    actual_board = board.Board(board_pretty)
    writer.write(str(actual_board.matrix))
    writer.write('\n')

    print(actual_board.matrix)

    scores = scan_posible_moves(actual_board, color)
    # for s in scores.play_moves:
    #     print(s)

    moves = evaluate_moves(actual_board, scores, color)
    # for m in moves:
    #     print(m)

    b_move = best_move(moves)
    move = b_move[0]
    print(move)

    writer.write(str(move))
    writer.write('\n')

    return move['from_row'], move['from_col'], move['to_row'], move['to_col']