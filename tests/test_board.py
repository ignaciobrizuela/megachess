import sys
import os
sys.path.append(os.path.abspath('../scripts'))

import board
import unittest

class boardTest(unittest.TestCase):
    board_game = None

    def setUp(self):
        board_str = ('rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp' 
                    '                                                                ' 
                    '                                                                ' 
                    'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR')
        self.board_game = board.Board(board_str)

    def test_shape_board(self):
        self.assertEqual((16, 16), self.board_game.matrix.shape, "Must be a 16x16 board")

    def test_pieces_quantity(self):
        # Black pieces
        self.assertEqual(32, len(self.board_game.black_pawns), 'Must be 32 pawns at the beginning of the game')
        self.assertEqual(8, len(self.board_game.black_horses), 'Must be 8 horses at the beginning of the game')
        self.assertEqual(8, len(self.board_game.black_bishops), 'Must be 8 bishops at the beginning of the game')
        self.assertEqual(8, len(self.board_game.black_rooks), 'Must be 8 rooks at the beginning of the game')
        self.assertEqual(4, len(self.board_game.black_queens), 'Must be 4 queens at the beginning of the game')
        self.assertEqual(4, len(self.board_game.black_kings), 'Must be 4 kings at the beginning of the game')
        # White pieces
        self.assertEqual(32, len(self.board_game.white_pawns), 'Must be 32 pawns at the beginning of the game')
        self.assertEqual(8, len(self.board_game.white_horses), 'Must be 8 horses at the beginning of the game')
        self.assertEqual(8, len(self.board_game.white_bishops), 'Must be 8 bishops at the beginning of the game')
        self.assertEqual(8, len(self.board_game.white_rooks), 'Must be 8 rooks at the beginning of the game')
        self.assertEqual(4, len(self.board_game.white_queens), 'Must be 4 queens at the beginning of the game')
        self.assertEqual(4, len(self.board_game.white_kings), 'Must be 4 kings at the beginning of the game')


if __name__ == "__main__":
     unittest.main()
            
