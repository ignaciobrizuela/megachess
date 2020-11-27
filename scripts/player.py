# Made by brz
import asyncio
from scripts import board
from scripts import moves
from scripts import match
from scripts import pieces
import numpy as np 


def gambit_king(board, color):
    kings   = board.black_kings   if color == 'black' else board.white_kings
    kings = kings[::-1]           if color=='black'   else kings
    i = 0

    for king in kings:
        if color == 'black':
            kings[i].rivals.append(moves.rival_down(board, king))
            kings[i].rivals.append(moves.rival_down_right(board, king))
            kings[i].rivals.append(moves.rival_down_left(board, king))
            kings[i].rivals.append(moves.rival_right(board, king))
            kings[i].rivals.append(moves.rival_left(board, king))
            kings[i].rivals.append(moves.rival_up(board, king))
            kings[i].rivals.append(moves.rival_up_right(board, king))
            kings[i].rivals.append(moves.rival_up_left(board, king))

        elif color == 'white':
            kings[i].rivals.append(moves.rival_up(board, king))
            kings[i].rivals.append(moves.rival_up_right(board, king))
            kings[i].rivals.append(moves.rival_up_left(board, king))
            kings[i].rivals.append(moves.rival_left(board, king))
            kings[i].rivals.append(moves.rival_right(board, king))
            kings[i].rivals.append(moves.rival_down(board, king))
            kings[i].rivals.append(moves.rival_down_left(board, king))
            kings[i].rivals.append(moves.rival_down_right(board, king))

        i += 1

    return moves.can_capture(kings)

def gambit_rook(board, color):
    rooks   = board.black_rooks   if color == 'black' else board.white_rooks
    rooks = rooks[::-1]           if color=='black'   else rooks
    i = 0

    
    for rook in rooks:
        if color == 'black':
            rooks[i].rivals.append(moves.rival_down(board, rook))
            rooks[i].rivals.append(moves.rival_up(board, rook))
            rooks[i].rivals.append(moves.rival_left(board, rook))
            rooks[i].rivals.append(moves.rival_right(board, rook))

        elif color == 'white':
            rooks[i].rivals.append(moves.rival_up(board, rook))
            rooks[i].rivals.append(moves.rival_down(board, rook))
            rooks[i].rivals.append(moves.rival_right(board, rook))
            rooks[i].rivals.append(moves.rival_left(board, rook))

        i += 1

    return moves.can_capture(rooks)

def gambit_bishop(board, color):
    bishops   = board.black_bishops if color == 'black' else board.white_bishops
    bishops = bishops[::-1]         if color=='black'   else bishops
    i = 0


    for bishop in bishops:
        if color == 'black':
            bishops[i].rivals.append(moves.rival_down_left(board, bishop))
            bishops[i].rivals.append(moves.rival_down_right(board, bishop))
            bishops[i].rivals.append(moves.rival_up_left(board, bishop))
            bishops[i].rivals.append(moves.rival_up_right(board, bishop))
        
        elif color == 'white':
            bishops[i].rivals.append(moves.rival_up_right(board, bishop))
            bishops[i].rivals.append(moves.rival_up_left(board, bishop))
            bishops[i].rivals.append(moves.rival_down_right(board, bishop))
            bishops[i].rivals.append(moves.rival_down_left(board, bishop))

        i += 1

    return moves.can_capture(bishops)

def gambit_pawn(board, color):
    pawns   = board.black_pawns   if color == 'black' else board.white_pawns
    pawns   = pawns[::-1]         if color=='black'   else pawns
    i = 0

    
    for pawn in pawns:
        if color == 'black':
            pawns[i].rivals.append(moves.rival_down_left(board, pawn))
            pawns[i].rivals.append(moves.rival_down_right(board, pawn))

        elif color == 'white':
            pawns[i].rivals.append(moves.rival_up_right(board, pawn))
            pawns[i].rivals.append(moves.rival_up_left(board, pawn))

        i += 1

    return moves.can_capture(pawns)



def gambit_queen(board, color):
    # Check if there is any queen in the board
    queens = board.black_queens if color=='black' else board.white_queens
    queens = queens[::-1]       if color=='black' else queens
    i = 0

    # any advanced queen?
    
    for queen in queens:
        if color == 'black':
            queens[i].rivals.append(moves.rival_down(board, queen))
            queens[i].rivals.append(moves.rival_down_right(board, queen))
            queens[i].rivals.append(moves.rival_down_left(board, queen))
            queens[i].rivals.append(moves.rival_right(board, queen))
            queens[i].rivals.append(moves.rival_left(board, queen))
            queens[i].rivals.append(moves.rival_up(board, queen))
            queens[i].rivals.append(moves.rival_up_right(board, queen))
            queens[i].rivals.append(moves.rival_up_left(board, queen))

        elif color == 'white':
            queens[i].rivals.append(moves.rival_up(board, queen))
            queens[i].rivals.append(moves.rival_up_right(board, queen))
            queens[i].rivals.append(moves.rival_up_left(board, queen))
            queens[i].rivals.append(moves.rival_left(board, queen))
            queens[i].rivals.append(moves.rival_right(board, queen))
            queens[i].rivals.append(moves.rival_down(board, queen))
            queens[i].rivals.append(moves.rival_down_left(board, queen))
            queens[i].rivals.append(moves.rival_down_right(board, queen))
        
        i += 1
        

    return moves.can_capture(queens)

    
def crown_a_pawn(board, color):
    pawns = board.black_pawns if color=='black' else board.white_pawns
    i = len(pawns) - 1 if color=='black' else 0

    n = pawns[i].make_a_jump()

    to_row = pawns[i].row + n
    to_col = pawns[i].col

    return pawns[i].row, pawns[i].col, to_row, to_col





writer = open('game.txt', 'w')

def play(actual_board, color):
    # Split the board into rows of 16 pieces length
    actual_board = board.Board(actual_board)
    writer.write(str(actual_board.matrix))
    writer.write('\n')

    print(actual_board.matrix)
    # Check if there is any queen abble to moves.can_capture pieces
    try:
        from_row, from_col, to_row, to_col = gambit_king(actual_board, color)
    except Exception as e:
        try:
            from_row, from_col, to_row, to_col = gambit_rook(actual_board, color)
        except Exception as e:
            try:
                from_row, from_col, to_row, to_col = gambit_bishop(actual_board, color)
            except Exception as e:
                try:
                    from_row, from_col, to_row, to_col = gambit_pawn(actual_board, color)
                except Exception as e:
                    try:
                        from_row, from_col, to_row, to_col = gambit_queen(actual_board, color)
                    except Exception as e:
                        try:
                            from_row, from_col, to_row, to_col = crown_a_pawn(actual_board, color)
                        except Exception as e:
                            print('It cannot move')
                            
    # writer.write(str(from_row, from_col, to_row, to_col))
    print(from_row, from_col, to_row, to_col)
    return from_row, from_col, to_row, to_col
    # try:
    #     try:
    #         try:
    #             from_row, from_col, to_row, to_col = gambit_king(actual_board, color)
    #             return from_row, from_col, to_row, to_col
    #         except Exception as e:
    #             pass
    #             from_row, from_col, to_row, to_col = gambit_rook(actual_board, color)
    #             return from_row, from_col, to_row, to_col
    #     except Exception as e:
    #         from_row, from_col, to_row, to_col = gambit_queen(actual_board, color)
    #         return from_row, from_col, to_row, to_col
    # If there is not, try to crown a pawn
    # except Exception as e:
    #     from_row, from_col, to_row, to_col = crown_a_pawn(actual_board, color)
    #     return from_row, from_col, to_row, to_col
    
