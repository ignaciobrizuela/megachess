class Match():

    def __init__(self, board_id, turn_token, actual_turn):
        self.board_id = board_id
        self.turn_token = turn_token
        self.actual_turn = actual_turn

# board_id = "2d348323-2e79-4961-ac36-1b000e8c42a5"
# color = 'black'
# board = ('rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp' 
#         '                                                                ' 
#         '                                                                ' 
#         'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR')
# # board_split = split_pieces(board)

# match1 = Match(board_id)
# match1.get_pieces_from_board(board)
# pawns= match1.black_pawns
# for pawn in pawns:
#     print(pawn.row, pawn.col)