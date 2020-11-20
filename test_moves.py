import board 
import numpy as np
import moves
import pieces
import unittest


class TestMoves(unittest.TestCase):

    def test_rival_up(self):
        board_str = ('PPPPPP    pppppp'
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
                    'phbrqk  p PHBRQK')

        board_test = board.Board(board_str)

        black_pawn      = pieces.Pawn('p', 'black', 15, 0)
        black_horse     = pieces.Horse('h', 'black', 15, 1)
        black_bishop    = pieces.Bishop('b', 'black', 15, 2)
        black_rook      = pieces.Rook('r', 'black', 15, 3)
        black_queen     = pieces.Queen('q', 'black', 15, 4)
        black_king      = pieces.King('k', 'black', 15, 5)

        self.assertEqual((0, 0), (moves.rival_up(board_test, black_pawn)))
        self.assertEqual((0, 1), (moves.rival_up(board_test, black_horse)))
        self.assertEqual((0, 2), (moves.rival_up(board_test, black_bishop)))
        self.assertEqual((0, 3), (moves.rival_up(board_test, black_rook)))
        self.assertEqual((0, 4), (moves.rival_up(board_test, black_queen)))
        self.assertEqual((0, 5), (moves.rival_up(board_test, black_king)))

        white_pawn      = pieces.Pawn('P', 'white', 15, 10)
        white_horse     = pieces.Horse('H', 'white', 15, 11)
        white_bishop    = pieces.Bishop('B', 'white', 15, 12)
        white_rook      = pieces.Rook('P', 'white', 15, 13)
        white_queen     = pieces.Queen('P', 'white', 15, 14)
        white_king      = pieces.King('P', 'white', 15, 15)

        self.assertEqual((0, 10), (moves.rival_up(board_test, white_pawn)))
        self.assertEqual((0, 11), (moves.rival_up(board_test, white_horse)))
        self.assertEqual((0, 12), (moves.rival_up(board_test, white_bishop)))
        self.assertEqual((0, 13), (moves.rival_up(board_test, white_rook)))
        self.assertEqual((0, 14), (moves.rival_up(board_test, white_queen)))
        self.assertEqual((0, 15), (moves.rival_up(board_test, white_king)))

        black_pawn      = pieces.Pawn('p', 'black', 15, 8)
        self.assertIsNone((moves.rival_up(board_test, black_pawn)))

# Run the Tests
if __name__ == 'main':
    unittest.main()