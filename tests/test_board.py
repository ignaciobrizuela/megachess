# Made by brz
from scripts import board
import unittest

class TestBoard(unittest.TestCase):
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
            
