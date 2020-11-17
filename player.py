import board
import moves
import match
import pieces


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper



def create_match(board_id, turn_token, actual_turn):
    matches.append(match.Match(board_id, turn_token, actual_turn))

def get_match(board_id):
    for index, m in enumerate(matches):
        if m.get_board_id() == board_id:
            return index, m


def gambit_queen(board, color):
    # Check if there is any queen in the board
    queens = actual_board.black_queens if color=='black' else actual_board.white_queens
    # any advanced queen?
    for queen in reversed(queens):
        print(queen.row, queen.col)

        # If there is a queen, get vertical column
        vertical_col = actual_board.board_array[:,queen.col]
        # **** Checking for any rival in VERTICAL column *****
        # Any rival up my piece
        rival_row = rival_up_row(queen, vertical_col)

        if rival_row == None:
            # Any rival down my piece
            rival_row = rival_down_row(queen, vertical_col)
            if rival_row == None:
                ('No rival in the way')
            else:
                print("yes", queen.row, queen.col)
                print(vertical_col)
                print("Can capture piece in row -> {}".format(rival_row))
                return rival_row, queen.col
                break
        else:
            print("yes", queen.row, queen.col)
            print(vertical_col)
            print("Can capture piece in row -> {}".format(rival_row))
            return rival_row, queen.col
            break

    # another queen?

def rival_up_row(piece, my_piece_entire_col):

    for i in reversed(range(0, piece.row)):
        if my_piece_entire_col[i].isupper():
            return i
        elif my_piece_entire_col[i].islower():
            return None


def rival_down_row(piece, my_piece_entire_col):

    for i in range(piece.row+1, 15):
        if my_piece_entire_col[i].isupper():
            return i
        elif my_piece_entire_col[i].islower():
            return None



def next_piece():
    n = 0
    while n < 16:
        yield n
        n += 1

# To find if there is a match with this board_id
# result = any(m.board_id() == board_id for m in matches)

matches = []

board_id = "2d348323-2e79-4961-ac36-1b000e8c42a5"
turn_token = "2d348323-2e79-4961-ac36-1b000e8c42a5"
actual_turn = "black"
board_match = ('rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp' 
        '                                                                ' 
        '                                                                ' 
        'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR')

# Creates a new match
matches.append(match.Match(board_id, turn_token, actual_turn))
# Split the board into rows of 16 pieces length
actual_board = board.Board(board_match)
# print(actual_board.board_array[:,1])
# Get black pawns 
gambit_queen(actual_board, actual_turn)
# Find a pawn to crown
# This selector return columns from 0 to 15
selector = next_piece()
# find_pawn(pawns, next(selector), actual_turn)