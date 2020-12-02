# Made by brz
import unittest
from scripts import board
from scripts import pieces
from scripts import player2
from scripts import scans
from scripts import score


class TestPlayer(unittest.TestCase):

    def setUp(self):
        board1 = (  'RP              '
                    'P             b '
                    '             PK '
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

        self.actual_board = board.Board(board1)

        moves = ({'from_row': 1, 'from_col': 14, 'to_row': 0, 'to_col': 15, 'score': -8},
                {'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': -8},
                {'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 13, 'score': -100},
                {'from_row': 1, 'from_col': 14, 'to_row': 0, 'to_col': 13, 'score': -8},
                {'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15},
                {'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0},
                {'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 14, 'score': 40.0},
                {'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 15, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 15, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 14, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 13, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 13, 'score': 5})
        
        self.actual_score = score.Score()
        self.actual_score.play_moves = moves

    def test_scan_Pawn(self):
        new_score = score.Score()
        pawn = pieces.Pawn(True, 2, 13)
        moves = [{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15},
                {'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0}]
        
        up          = scans.scan_up(self.actual_board, pawn)
        up_right    = scans.scan_up_right(self.actual_board, pawn)
        right       = scans.scan_right(self.actual_board, pawn)
        down_right  = scans.scan_down_right(self.actual_board, pawn)
        down        = scans.scan_down(self.actual_board, pawn)
        down_left   = scans.scan_down_left(self.actual_board, pawn)
        left        = scans.scan_left(self.actual_board, pawn)
        up_left     = scans.scan_up_left(self.actual_board, pawn)
        L           = scans.scan_L(self.actual_board, pawn)

        player2.scan(new_score, up, pawn, True)
        player2.scan(new_score, up_right, pawn, True)
        player2.scan(new_score, right, pawn, True)
        player2.scan(new_score, down_right, pawn, True)
        player2.scan(new_score, down, pawn, True)
        player2.scan(new_score, down_left, pawn, True)
        player2.scan(new_score, left, pawn, True)
        player2.scan(new_score, up_left, pawn, True)
        player2.scan(new_score, L, pawn, True)

        self.assertEqual(moves, new_score.play_moves)

    def test_scan_King(self):
        new_score = score.Score()
        king = pieces.King(True, 2, 14)
        moves = [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 14, 'score': 40.0},
                {'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 15, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 15, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 14, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 13, 'score': 5},
                {'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 13, 'score': 5}]
        
        up          = scans.scan_up(self.actual_board, king)
        up_right    = scans.scan_up_right(self.actual_board, king)
        right       = scans.scan_right(self.actual_board, king)
        down_right  = scans.scan_down_right(self.actual_board, king)
        down        = scans.scan_down(self.actual_board, king)
        down_left   = scans.scan_down_left(self.actual_board, king)
        left        = scans.scan_left(self.actual_board, king)
        up_left     = scans.scan_up_left(self.actual_board, king)
        L           = scans.scan_L(self.actual_board, king)

        player2.scan(new_score, up, king, True)
        player2.scan(new_score, up_right, king, True)
        player2.scan(new_score, right, king, True)
        player2.scan(new_score, down_right, king, True)
        player2.scan(new_score, down, king, True)
        player2.scan(new_score, down_left, king, True)
        player2.scan(new_score, left, king, True)
        player2.scan(new_score, up_left, king, True)
        player2.scan(new_score, L, king, True)

        self.assertEqual(moves, new_score.play_moves)

    def test_scan_bishop(self):
        new_score = score.Score()
        bishop = pieces.Bishop(False, 1, 14)
        moves = [{'from_row': 1, 'from_col': 14, 'to_row': 0, 'to_col': 15, 'score': -8},
                {'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': -8},
                {'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 13, 'score': -100},
                {'from_row': 1, 'from_col': 14, 'to_row': 0, 'to_col': 13, 'score': -8}]
        
        up          = scans.scan_up(self.actual_board, bishop)
        up_right    = scans.scan_up_right(self.actual_board, bishop)
        right       = scans.scan_right(self.actual_board, bishop)
        down_right  = scans.scan_down_right(self.actual_board, bishop)
        down        = scans.scan_down(self.actual_board, bishop)
        down_left   = scans.scan_down_left(self.actual_board, bishop)
        left        = scans.scan_left(self.actual_board, bishop)
        up_left     = scans.scan_up_left(self.actual_board, bishop)
        L           = scans.scan_L(self.actual_board, bishop)

        player2.scan(new_score, up, bishop, True)
        player2.scan(new_score, up_right, bishop, True)
        player2.scan(new_score, right, bishop, True)
        player2.scan(new_score, down_right, bishop, True)
        player2.scan(new_score, down, bishop, True)
        player2.scan(new_score, down_left, bishop, True)
        player2.scan(new_score, left, bishop, True)
        player2.scan(new_score, up_left, bishop, True)
        player2.scan(new_score, L, bishop, True)

        self.assertEqual(moves, new_score.play_moves)

    def test_evaluate_moves(self):
        moves = [[{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15}, 60.3],
                [{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15],
                [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15],
                [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 15, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 15, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 14, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 13, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 13, 'score': 5}, -50.0]]
        
        scores = player2.evaluate_moves(self.actual_board, self.actual_score, True)

        self.assertEqual(moves, scores)

    def test_best_move(self):
        moves = [[{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15}, 60.3],
                [{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15],
                [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15],
                [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 15, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 15, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 14, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 13, 'score': 5}, -29.85],
                [{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 13, 'score': 5}, -50.0]]

        b_move_expected = [{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15]
        b_move = player2.best_move(moves)

        self.assertEqual(b_move_expected , b_move)

    def test_minimax(self):
        max_move_expected = {'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15}
        min_move_expected = {'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 13, 'score': -100}
        
        max_move, min_move = player2.minimax(self.actual_score)

        self.assertEqual(max_move_expected, max_move)
        self.assertEqual(min_move_expected, min_move)

# if __name__ == 'main':
#     unittest.main()
            
        