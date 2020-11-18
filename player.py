# Made by brz
import asyncio
import board
import moves
import match
import pieces
import numpy as np 


def create_match(board_id, turn_token, actual_turn):
    matches.append(match.Match(board_id, turn_token, actual_turn))


def get_match(board_id):
    for index, m in enumerate(matches):
        if m.get_board_id() == board_id:
            return index, m


def gambit_queen(board, color):
    # Check if there is any queen in the board
    queens = board.black_queens if color=='black' else board.white_queens
    i = len(queens) -1

    # any advanced queen?
    for queen in reversed(queens):

        # print(moves.rival_up(board, queen))
        # print(moves.rival_down(board, queen))
        # print(moves.rival_right(board, queen))
        # print(moves.rival_left(board, queen))
        queens[i].rivals.append(moves.rival_up(board, queen))
        queens[i].rivals.append(moves.rival_down(board, queen))
        queens[i].rivals.append(moves.rival_right(board, queen))
        queens[i].rivals.append(moves.rival_left(board, queen))

        i -= 1

    for queen in reversed(queens):
        for rival in queen.rivals:
            if rival != None:
                return queen.row, queen.col, rival[0], rival[1]
    return None


def crown_a_pawn(board, color):
    pawns = board.black_pawns if color=='black' else board.white_pawns
    i = len(pawns) - 1 if color=='black' else 0

    n = pawns[i].valid_move_jump()

    to_row = pawns[i].row + n
    to_col = pawns[i].col

    return pawns[i].row, pawns[i].col, to_row, to_col


# To find if there is a match with this board_id
# result = any(m.board_id() == board_id for m in matches)

matches = []

# board_id = "2d348323-2e79-4961-ac36-1b000e8c42a5"
# turn_token = "2d348323-2e79-4961-ac36-1b000e8c42a5"
# actual_turn = "white"
# board_match = ('rrhhbbqqkkBbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp' 
#                 '                                                                ' 
#                 '                                                                ' 
#                 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR')

def play(actual_board, color):
    # Creates a new match
    # matches.append(match.Match(board_id, turn_token, color))
    # Split the board into rows of 16 pieces length
    actual_board = board.Board(actual_board)
    # print(actual_board.board_array)
    # Get black pawns 
    try:
        from_row, from_col, to_row, to_col = gambit_queen(actual_board, color)
        return from_row, from_col, to_row, to_col

    except Exception as e:
        from_row, from_col, to_row, to_col = crown_a_pawn(actual_board, color)
        return from_row, from_col, to_row, to_col
    
