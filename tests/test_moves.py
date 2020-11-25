from scripts import  board
from scripts import  pieces
from scripts import  moves
import unittest
import numpy as np

class TestMoves(unittest.TestCase):
    board_game = []

    def setUp(self):
        board_str = ('                '
                    '                '
                    '                '
                    '                ' 
                    '                '
                    '                '
                    '                '
                    '                ' 
                    '                '
                    '                '
                    '                '
                    '                ' 
                    '                '
                    '                '
                    '                '
                    '                ')
        self.board_game = board.Board(board_str)

    def test_rival_up_pawn_vs_Pawn(self):
        black_pawn      = pieces.Pawn('p', 'black', 15, 0)
        self.board_game.matrix[15][0] = 'p'

        white_pawn      = pieces.Pawn('P', 'white', 10, 0)
        self.board_game.matrix[10][0] = 'P'

        self.assertEqual((10, 0), (moves.rival_up(self.board_game, black_pawn)))

    def test_rival_up_pawn_vs_pawn(self):
        black_pawn1      = pieces.Pawn('p', 'black', 15, 0)
        self.board_game.matrix[15][0] = 'p'

        black_pawn2     = pieces.Pawn('p', 'black', 10, 0)
        self.board_game.matrix[10][0] = 'p'

        self.assertIsNone((moves.rival_up(self.board_game, black_pawn1)))

    def test_rival_up_pawn_vs_empty(self):
        black_pawn1      = pieces.Pawn('p', 'black', 15, 0)
        self.board_game.matrix[15][0] = 'p'

        self.assertIsNone((moves.rival_up(self.board_game, black_pawn1)))
        

# Run the Tests
if __name__ == 'main':
    unittest.main()