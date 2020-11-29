# Made by brz
import unittest
from scripts import board
from scripts import scans
from scripts import pieces

class Testscans(unittest.TestCase):

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

    def test_scan_up(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 5, 8)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[5][8] = pawn

        up = scans.scan_up(self.board_game, queen)

        self.assertIsInstance(next(up), pieces.EmptySquare)
        self.assertIsInstance(next(up), pieces.EmptySquare)
        self.assertIsInstance(next(up), pieces.Pawn)

    
    def test_scan_up_right(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 5, 11)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[5][11] = pawn

        up_right = scans.scan_up_right(self.board_game, queen)

        self.assertIsInstance(next(up_right), pieces.EmptySquare)
        self.assertIsInstance(next(up_right), pieces.EmptySquare)
        self.assertIsInstance(next(up_right), pieces.Pawn)

    
    def test_scan_right(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 8, 11)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[8][11] = pawn

        right = scans.scan_right(self.board_game, queen)

        self.assertIsInstance(next(right), pieces.EmptySquare)
        self.assertIsInstance(next(right), pieces.EmptySquare)
        self.assertIsInstance(next(right), pieces.Pawn)

    def test_scan_down_right(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 11, 11)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[11][11] = pawn

        down_right = scans.scan_down_right(self.board_game, queen)

        self.assertIsInstance(next(down_right), pieces.EmptySquare)
        self.assertIsInstance(next(down_right), pieces.EmptySquare)
        self.assertIsInstance(next(down_right), pieces.Pawn)

    def test_scan_down(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 11, 8)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[11][8] = pawn

        down = scans.scan_down(self.board_game, queen)

        self.assertIsInstance(next(down), pieces.EmptySquare)
        self.assertIsInstance(next(down), pieces.EmptySquare)
        self.assertIsInstance(next(down), pieces.Pawn)

    def test_scan_down_left(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 11, 5)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[11][5] = pawn

        down_left = scans.scan_down_left(self.board_game, queen)

        self.assertIsInstance(next(down_left), pieces.EmptySquare)
        self.assertIsInstance(next(down_left), pieces.EmptySquare)
        self.assertIsInstance(next(down_left), pieces.Pawn)

    def test_scan_left(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 8, 5)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[8][5] = pawn

        left = scans.scan_left(self.board_game, queen)

        self.assertIsInstance(next(left), pieces.EmptySquare)
        self.assertIsInstance(next(left), pieces.EmptySquare)
        self.assertIsInstance(next(left), pieces.Pawn)

    def test_scan_up_left(self):
        queen = pieces.Queen(False, 8, 8)
        pawn = pieces.Pawn(True, 5, 5)

        self.board_game.matrix_pieces[8][8] = queen
        self.board_game.matrix_pieces[5][5] = pawn

        up_left = scans.scan_up_left(self.board_game, queen)

        self.assertIsInstance(next(up_left), pieces.EmptySquare)
        self.assertIsInstance(next(up_left), pieces.EmptySquare)
        self.assertIsInstance(next(up_left), pieces.Pawn)

if __name__ == 'main':
    unittest.main()
            