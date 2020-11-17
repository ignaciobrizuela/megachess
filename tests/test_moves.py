# Made by brz

import unittest
import pieces
import moves

class TestMoves(unittest.TestCase):

    def test_n_square_line(self):
        pawn = pieces.Pawn('white', 12, 8)
        self.assertEqual(moves.n_square_line(pawn, 1, 'up'), (11,8))
        self.assertEqual(moves.n_square_diagonal(pawn, 1, 'ur'), (11,9))

if __name__ == "__main__":
    unittest.main()