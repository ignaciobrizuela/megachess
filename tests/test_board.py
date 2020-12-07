# Made by brz
from scripts import board
import unittest

class TestBoard(unittest.TestCase):
    board_game = None

    def setUp(self):
        self.board_pretty = ('♜♜♞♞♝♝♛♛♚♚♝♝♞♞♜♜♜♜♞♞♝♝♛♛♚♚♝♝♞♞♜♜♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟♟'
        '                                                                '
        '                                                                '
        '♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♙♖♖♘♘♗♗♕♕♔♔♗♗♘♘♖♖♖♖♘♘♗♗♕♕♔♔♗♗♘♘♖♖')
        self.board_game = board.Board(self.board_pretty)

    def test_transform_pretty_pieces(self):
        board_str = (  'rrhhbbqqkkbbhhrr'
            'rrhhbbqqkkbbhhrr'
            'pppppppppppppppp'
            'pppppppppppppppp' 
            '                '
            '                '
            '                '
            '                ' 
            '                '
            '                '
            '                '
            '                ' 
            'PPPPPPPPPPPPPPPP'
            'PPPPPPPPPPPPPPPP'
            'RRHHBBQQKKBBHHRR'
            'RRHHBBQQKKBBHHRR')

        board_pieces = board.transform_pretty_pieces(board_str)

        self.assertEqual(8, board_pieces.count('♜'))
        self.assertEqual(8, board_pieces.count('♞'))
        self.assertEqual(8, board_pieces.count('♝'))
        self.assertEqual(4, board_pieces.count('♛'))
        self.assertEqual(4, board_pieces.count('♚'))
        self.assertEqual(32, board_pieces.count('♟'))
        self.assertEqual(8, board_pieces.count('♖'))
        self.assertEqual(8, board_pieces.count('♘'))
        self.assertEqual(8, board_pieces.count('♗'))
        self.assertEqual(4, board_pieces.count('♕'))
        self.assertEqual(4, board_pieces.count('♔'))
        self.assertEqual(32, board_pieces.count('♙'))
    
    def test_convert_board_matrix(self):
        matrix_pieces = board.convert_board_matrix(self.board_pretty)
        self.assertEqual((16, 16), matrix_pieces.shape, "Must be a 16x16 board")

    def test_pieces_quantity(self):
        white_pieces = []
        black_pieces = []
        empty_pieces = []

        for row_pieces in self.board_game.matrix_pieces:
            for piece in row_pieces:
                if piece.color == True:
                    white_pieces.append(piece)
                elif piece.color == False:
                    black_pieces.append(piece)
                else:
                    empty_pieces.append(piece)

        # White pieces
        self.assertEqual(64, len(white_pieces))
        self.assertEqual(64, len(black_pieces))
        self.assertEqual(128, len(empty_pieces))


# if __name__ == "__main__":
#      unittest.main()
            
