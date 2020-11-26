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

    ################################################################################################################
    #                                                RIVAL UP                                                      #
    ################################################################################################################

    # ------------- Pawn (white)---------------------#
    # Rival pieces above
    def test_rival_up_Pawn_vs_king(self):
        white_pawn = pieces.Pawn('white', 11, 7)
        self.board_game.matrix[11][7] = 'P'

        black_king = pieces.King('black', 10, 7)
        self.board_game.matrix[10][7] = 'k'

        self.assertEqual((10, 7), (moves.rival_up(self.board_game, white_pawn)), 'There is not a king above the Pawn')

    def test_rival_up_Pawn_vs_queen(self):
        white_pawn = pieces.Pawn('white', 12, 0)
        self.board_game.matrix[12][0] = 'P'

        black_queen = pieces.Queen('black', 10, 0)
        self.board_game.matrix[10][0] = 'q'

        self.assertEqual((10, 0), (moves.rival_up(self.board_game, white_pawn)), 'There is not a queen above the Pawn')

    def test_rival_up_Pawn_vs_rook(self):
        white_pawn = pieces.Pawn('white', 12, 14)
        self.board_game.matrix[12][14] = 'P'

        black_rook = pieces.Rook('black', 2, 14)
        self.board_game.matrix[2][14] = 'r'

        self.assertEqual((2, 14), (moves.rival_up(self.board_game, white_pawn)), 'There is not a rook above the Pawn')

    def test_rival_up_Pawn_vs_bishop(self):
        white_pawn = pieces.Pawn('white', 10, 8)
        self.board_game.matrix[10][8] = 'P'

        black_bishop = pieces.Bishop('black', 9, 8)
        self.board_game.matrix[9][8] = 'b'

        self.assertEqual((9, 8), (moves.rival_up(self.board_game, white_pawn)), 'There is not a bishop above the Pawn')

    def test_rival_up_Pawn_vs_Horse(self):
        white_pawn = pieces.Pawn('white', 11, 9)
        self.board_game.matrix[11][9] = 'P'

        black_horse = pieces.Horse('black', 9, 9)
        self.board_game.matrix[9][9] = 'h'

        self.assertEqual((9, 9), (moves.rival_up(self.board_game, white_pawn)), 'There is not a horse above the Pawn')
    
    # Team pieces above Pawn
    def test_rival_up_Pawn_vs_King(self):
        white_pawn = pieces.Pawn('white', 12, 7)
        self.board_game.matrix[12][7] = 'P'

        white_king = pieces.King('white', 10, 7)
        self.board_game.matrix[10][7] = 'K'

        self.assertIsNone(moves.rival_up(self.board_game, white_pawn), 'There is a rival above the Pawn')
    
    def test_rival_up_Pawn_vs_Queen(self):
        white_pawn = pieces.Pawn('white', 11, 6)
        self.board_game.matrix[11][6] = 'P'

        white_queen = pieces.Queen('white', 1, 6)
        self.board_game.matrix[1][6] = 'Q'

        self.assertIsNone(moves.rival_up(self.board_game, white_pawn), 'There is a rival above the Pawn')

    def test_rival_up_Pawn_vs_Rook(self):
        white_pawn = pieces.Pawn('white', 12, 15)
        self.board_game.matrix[12][15] = 'P'

        white_rook = pieces.Rook('white', 0, 15)
        self.board_game.matrix[0][15] = 'R'

        self.assertIsNone(moves.rival_up(self.board_game, white_pawn), 'There is a rival above the Pawn')
    
    def test_rival_up_Pawn_vs_bishop(self):
        white_pawn = pieces.Pawn('white', 12, 13)
        self.board_game.matrix[12][13] = 'P'

        white_bishop = pieces.Bishop('white', 1, 13)
        self.board_game.matrix[1][13] = 'B'

        self.assertIsNone(moves.rival_up(self.board_game, white_pawn), 'There is a rival above the Pawn')

    def test_rival_up_Queen_vs_Horse(self):
        white_pawn = pieces.Pawn('white', 10, 11)
        self.board_game.matrix[10][11] = 'Q'

        white_horse = pieces.Horse('white', 7, 11)
        self.board_game.matrix[7][11] = 'H'

        self.assertIsNone (moves.rival_up(self.board_game, white_pawn), 'There is a rival above the Pawn')

    def test_rival_up_Pawn_vs_Pawn(self):
        white_pawn = pieces.Pawn('white', 8, 7)
        self.board_game.matrix[8][7] = 'P'

        white_pawn = pieces.Pawn('white', 5, 7)
        self.board_game.matrix[5][7] = 'P'

        self.assertIsNone(moves.rival_up(self.board_game, white_pawn), 'There is a rival above the Pawn')



    # ------------- Queen (white)---------------------#
    # Rival pieces above Queen
    def test_rival_up_Queen_vs_king(self):
        white_queen = pieces.Queen('white', 6, 7)
        self.board_game.matrix[6][7] = 'Q'

        black_king = pieces.King('black', 1, 7)
        self.board_game.matrix[1][7] = 'k'

        self.assertEqual((1, 7), (moves.rival_up(self.board_game, white_queen)), 'There is not a king above the Queen')
    
    def test_rival_up_Queen_vs_queen(self):
        white_queen = pieces.Queen('white', 11, 6)
        self.board_game.matrix[11][6] = 'Q'

        black_queen = pieces.Queen('black', 1, 6)
        self.board_game.matrix[1][6] = 'q'

        self.assertEqual((1, 6), (moves.rival_up(self.board_game, white_queen)), 'There is not a queen above the Queen')

    def test_rival_up_Queen_vs_rook(self):
        white_queen = pieces.Queen('white', 12, 15)
        self.board_game.matrix[12][15] = 'Q'

        black_rook = pieces.Rook('black', 0, 15)
        self.board_game.matrix[0][15] = 'r'

        self.assertEqual((0, 15), (moves.rival_up(self.board_game, white_queen)), 'There is not a rook above the Queen')
    
    def test_rival_up_Queen_vs_bishop(self):
        white_queen = pieces.Queen('white', 12, 13)
        self.board_game.matrix[12][13] = 'Q'

        black_bishop = pieces.Bishop('black', 1, 13)
        self.board_game.matrix[1][13] = 'b'

        self.assertEqual((1, 13), (moves.rival_up(self.board_game, white_queen)), 'There is not a bishop above the Queen')

    def test_rival_up_Queen_vs_horse(self):
        white_queen = pieces.Queen('white', 10, 11)
        self.board_game.matrix[10][11] = 'Q'

        black_horse = pieces.Horse('black', 7, 11)
        self.board_game.matrix[7][11] = 'h'

        self.assertEqual((7, 11), (moves.rival_up(self.board_game, white_queen)), 'There is not a horse above the Queen')

    def test_rival_up_Queen_vs_pawn(self):
        white_queen = pieces.Queen('white', 8, 7)
        self.board_game.matrix[8][7] = 'Q'

        black_pawn = pieces.Pawn('black', 5, 7)
        self.board_game.matrix[5][7] = 'p'

        self.assertEqual((5, 7), (moves.rival_up(self.board_game, white_queen)), 'There is not a pawn above the Queen')

    # Team pieces above Queen
    def test_rival_up_Queen_vs_King(self):
        white_queen = pieces.Queen('white', 6, 7)
        self.board_game.matrix[6][7] = 'Q'

        white_king = pieces.King('white', 1, 7)
        self.board_game.matrix[1][7] = 'K'

        self.assertIsNone(moves.rival_up(self.board_game, white_queen), 'There is a rival above the Queen')
    
    def test_rival_up_Queen_vs_Queen(self):
        white_queen1 = pieces.Queen('white', 11, 6)
        self.board_game.matrix[11][6] = 'Q'

        white_queen2 = pieces.Queen('white', 1, 6)
        self.board_game.matrix[1][6] = 'Q'

        self.assertIsNone(moves.rival_up(self.board_game, white_queen1), 'There is a rival above the Queen')

    def test_rival_up_Queen_vs_Rook(self):
        white_queen = pieces.Queen('white', 12, 15)
        self.board_game.matrix[12][15] = 'Q'

        white_rook = pieces.Rook('white', 0, 15)
        self.board_game.matrix[0][15] = 'R'

        self.assertIsNone(moves.rival_up(self.board_game, white_queen), 'There is a rival above the Queen')
    
    def test_rival_up_Queen_vs_Bishop(self):
        white_queen = pieces.Queen('white', 12, 13)
        self.board_game.matrix[12][13] = 'Q'

        white_bishop = pieces.Bishop('white', 1, 13)
        self.board_game.matrix[1][13] = 'B'

        self.assertIsNone(moves.rival_up(self.board_game, white_queen), 'There is a rival above the Queen')

    def test_rival_up_Queen_vs_Horse(self):
        white_queen = pieces.Queen('white', 10, 11)
        self.board_game.matrix[10][11] = 'Q'

        white_horse = pieces.Horse('white', 7, 11)
        self.board_game.matrix[7][11] = 'H'

        self.assertIsNone (moves.rival_up(self.board_game, white_queen), 'There is a rival above the Queen')

    def test_rival_up_Queen_vs_Pawn(self):
        white_queen = pieces.Queen('white', 8, 7)
        self.board_game.matrix[8][7] = 'Q'

        white_pawn = pieces.Pawn('white', 5, 7)
        self.board_game.matrix[5][7] = 'P'

        self.assertIsNone(moves.rival_up(self.board_game, white_queen), 'There is a rival above the Queen')
    


    # ------------- King (white)---------------------#
    # Rival pieces above King
    def test_rival_up_King_vs_king(self):
        white_king = pieces.King('white', 6, 7)
        self.board_game.matrix[6][7] = 'K'

        black_king = pieces.King('black', 1, 7)
        self.board_game.matrix[1][7] = 'k'

        self.assertEqual((1, 7), (moves.rival_up(self.board_game, white_king)), 'There is not a king above the King')
    
    def test_rival_up_King_vs_queen(self):
        white_king = pieces.King('white', 11, 6)
        self.board_game.matrix[11][6] = 'K'

        black_queen = pieces.King('black', 1, 6)
        self.board_game.matrix[1][6] = 'q'

        self.assertEqual((1, 6), (moves.rival_up(self.board_game, white_king)), 'There is not a queen above the King')

    def test_rival_up_King_vs_rook(self):
        white_king = pieces.King('white', 12, 15)
        self.board_game.matrix[12][15] = 'K'

        black_rook = pieces.Rook('black', 0, 15)
        self.board_game.matrix[0][15] = 'r'

        self.assertEqual((0, 15), (moves.rival_up(self.board_game, white_king)), 'There is not a rook above the King')
    
    def test_rival_up_King_vs_bishop(self):
        white_king = pieces.King('white', 12, 13)
        self.board_game.matrix[12][13] = 'K'

        black_bishop = pieces.Bishop('black', 1, 13)
        self.board_game.matrix[1][13] = 'b'

        self.assertEqual((1, 13), (moves.rival_up(self.board_game, white_king)), 'There is not a bishop above the King')

    def test_rival_up_King_vs_horse(self):
        white_king = pieces.King('white', 10, 11)
        self.board_game.matrix[10][11] = 'K'

        black_horse = pieces.Horse('black', 7, 11)
        self.board_game.matrix[7][11] = 'h'

        self.assertEqual((7, 11), (moves.rival_up(self.board_game, white_king)), 'There is not a horse above the King')

    def test_rival_up_King_vs_pawn(self):
        white_king = pieces.King('white', 8, 7)
        self.board_game.matrix[8][7] = 'K'

        black_pawn = pieces.Pawn('black', 5, 7)
        self.board_game.matrix[5][7] = 'p'

        self.assertEqual((5, 7), (moves.rival_up(self.board_game, white_king)), 'There is not a pawn above the King')

    # Team pieces above King
    def test_rival_up_King_vs_King(self):
        white_king1 = pieces.King('white', 6, 7)
        self.board_game.matrix[6][7] = 'K'

        white_king2 = pieces.King('white', 1, 7)
        self.board_game.matrix[1][7] = 'K'

        self.assertIsNone(moves.rival_up(self.board_game, white_king1), 'There is a rival above the King')
    
    def test_rival_up_King_vs_Queen(self):
        white_king = pieces.King('white', 11, 6)
        self.board_game.matrix[11][6] = 'K'

        white_queen = pieces.King('white', 1, 6)
        self.board_game.matrix[1][6] = 'Q'

        self.assertIsNone(moves.rival_up(self.board_game, white_king), 'There is a rival above the King')

    def test_rival_up_King_vs_Rook(self):
        white_king = pieces.King('white', 12, 15)
        self.board_game.matrix[12][15] = 'K'

        white_rook = pieces.Rook('white', 0, 15)
        self.board_game.matrix[0][15] = 'R'

        self.assertIsNone(moves.rival_up(self.board_game, white_king), 'There is a rival above the King')
    
    def test_rival_up_King_vs_Bishop(self):
        white_king = pieces.King('white', 12, 13)
        self.board_game.matrix[12][13] = 'K'

        white_bishop = pieces.Bishop('white', 1, 13)
        self.board_game.matrix[1][13] = 'B'

        self.assertIsNone(moves.rival_up(self.board_game, white_king), 'There is a rival above the King')

    def test_rival_up_King_vs_Horse(self):
        white_king = pieces.King('white', 10, 11)
        self.board_game.matrix[10][11] = 'K'

        white_horse = pieces.Horse('white', 7, 11)
        self.board_game.matrix[7][11] = 'H'

        self.assertIsNone (moves.rival_up(self.board_game, white_king), 'There is a rival above the King')

    def test_rival_up_King_vs_Pawn(self):
        white_king = pieces.King('white', 8, 7)
        self.board_game.matrix[8][7] = 'K'

        white_pawn = pieces.Pawn('white', 5, 7)
        self.board_game.matrix[5][7] = 'P'

        self.assertIsNone(moves.rival_up(self.board_game, white_king), 'There is a rival above the King')


    # ------------- Rook (white)---------------------#
    # Rival pieces above Rook
    def test_rival_up_Rook_vs_king(self):
        white_rook = pieces.Rook('white', 6, 7)
        self.board_game.matrix[6][7] = 'R'

        black_rook = pieces.King('black', 1, 7)
        self.board_game.matrix[1][7] = 'k'

        self.assertEqual((1, 7), (moves.rival_up(self.board_game, white_rook)), 'There is not a king above the Rook')
    
    def test_rival_up_Rook_vs_queen(self):
        white_rook = pieces.Rook('white', 11, 6)
        self.board_game.matrix[11][6] = 'R'

        black_queen = pieces.Queen('black', 1, 6)
        self.board_game.matrix[1][6] = 'q'

        self.assertEqual((1, 6), (moves.rival_up(self.board_game, white_rook)), 'There is not a queen above the Rook')

    def test_rival_up_Rook_vs_rook(self):
        white_rook = pieces.Rook('white', 12, 15)
        self.board_game.matrix[12][15] = 'R'

        black_rook = pieces.Rook('black', 0, 15)
        self.board_game.matrix[0][15] = 'r'

        self.assertEqual((0, 15), (moves.rival_up(self.board_game, white_rook)), 'There is not a rook above the Rook')
    
    def test_rival_up_Rook_vs_bishop(self):
        white_rook = pieces.Rook('white', 12, 13)
        self.board_game.matrix[12][13] = 'R'

        black_bishop = pieces.Bishop('black', 1, 13)
        self.board_game.matrix[1][13] = 'b'

        self.assertEqual((1, 13), (moves.rival_up(self.board_game, white_rook)), 'There is not a bishop above the Rook')

    def test_rival_up_Rook_vs_horse(self):
        white_rook = pieces.Rook('white', 10, 11)
        self.board_game.matrix[10][11] = 'R'

        black_horse = pieces.Horse('black', 7, 11)
        self.board_game.matrix[7][11] = 'h'

        self.assertEqual((7, 11), (moves.rival_up(self.board_game, white_rook)), 'There is not a horse above the Rook')

    def test_rival_up_Rook_vs_pawn(self):
        white_rook = pieces.Rook('white', 8, 7)
        self.board_game.matrix[8][7] = 'R'

        black_pawn = pieces.Pawn('black', 5, 7)
        self.board_game.matrix[5][7] = 'p'

        self.assertEqual((5, 7), (moves.rival_up(self.board_game, white_rook)), 'There is not a pawn above the Rook')

    # Team pieces above Rook
    def test_rival_up_Rook_vs_King(self):
        white_rook = pieces.Rook('white', 6, 7)
        self.board_game.matrix[6][7] = 'R'

        white_king = pieces.King('white', 1, 7)
        self.board_game.matrix[1][7] = 'K'

        self.assertIsNone(moves.rival_up(self.board_game, white_rook), 'There is a rival above the Rook')
    
    def test_rival_up_Rook_vs_Queen(self):
        white_rook = pieces.Rook('white', 11, 6)
        self.board_game.matrix[11][6] = 'R'

        white_queen = pieces.Rook('white', 1, 6)
        self.board_game.matrix[1][6] = 'Q'

        self.assertIsNone(moves.rival_up(self.board_game, white_rook), 'There is a rival above the Rook')

    def test_rival_up_Rook_vs_Rook(self):
        white_rook1 = pieces.Rook('white', 12, 15)
        self.board_game.matrix[12][15] = 'R'

        white_rook2 = pieces.Rook('white', 0, 15)
        self.board_game.matrix[0][15] = 'R'

        self.assertIsNone(moves.rival_up(self.board_game, white_rook1), 'There is a rival above the Rook')
    
    def test_rival_up_Rook_vs_Bishop(self):
        white_rook = pieces.Rook('white', 12, 13)
        self.board_game.matrix[12][13] = 'R'

        white_bishop = pieces.Bishop('white', 1, 13)
        self.board_game.matrix[1][13] = 'B'

        self.assertIsNone(moves.rival_up(self.board_game, white_rook), 'There is a rival above the Rook')

    def test_rival_up_Rook_vs_Horse(self):
        white_rook = pieces.Rook('white', 10, 11)
        self.board_game.matrix[10][11] = 'R'

        white_horse = pieces.Horse('white', 7, 11)
        self.board_game.matrix[7][11] = 'H'

        self.assertIsNone (moves.rival_up(self.board_game, white_rook), 'There is a rival above the Rook')

    def test_rival_up_Rook_vs_Pawn(self):
        white_rook = pieces.Rook('white', 8, 7)
        self.board_game.matrix[8][7] = 'R'

        white_pawn = pieces.Pawn('white', 5, 7)
        self.board_game.matrix[5][7] = 'P'

        self.assertIsNone(moves.rival_up(self.board_game, white_rook), 'There is a rival above the Rook')


    # ------------- Bishop (white)---------------------#
    # Rival pieces above Bishop
    def test_rival_up_Bishop_vs_King(self):
        white_bishop = pieces.Bishop('white', 6, 7)
        self.board_game.matrix[6][7] = 'B'

        black_King = pieces.King('black', 1, 7)
        self.board_game.matrix[1][7] = 'k'

        self.assertEqual((1, 7), (moves.rival_up(self.board_game, white_bishop)), 'There is not a King above the Bishop')
    
    def test_rival_up_Bishop_vs_queen(self):
        white_bishop = pieces.Bishop('white', 11, 6)
        self.board_game.matrix[11][6] = 'B'

        black_queen = pieces.Queen('black', 1, 6)
        self.board_game.matrix[1][6] = 'q'

        self.assertEqual((1, 6), (moves.rival_up(self.board_game, white_bishop)), 'There is not a queen above the Bishop')

    def test_rival_up_Bishop_vs_rook(self):
        white_bishop = pieces.Bishop('white', 12, 15)
        self.board_game.matrix[12][15] = 'B'

        black_rook = pieces.Rook('black', 0, 15)
        self.board_game.matrix[0][15] = 'r'

        self.assertEqual((0, 15), (moves.rival_up(self.board_game, white_bishop)), 'There is not a rook above the Bishop')
    
    def test_rival_up_Bishop_vs_bishop(self):
        white_bishop = pieces.Bishop('white', 12, 13)
        self.board_game.matrix[12][13] = 'B'

        black_bishop = pieces.Bishop('black', 1, 13)
        self.board_game.matrix[1][13] = 'b'

        self.assertEqual((1, 13), (moves.rival_up(self.board_game, white_bishop)), 'There is not a bishop above the Bishop')

    def test_rival_up_Bishop_vs_horse(self):
        white_bishop = pieces.Bishop('white', 10, 11)
        self.board_game.matrix[10][11] = 'B'

        black_horse = pieces.Horse('black', 7, 11)
        self.board_game.matrix[7][11] = 'h'

        self.assertEqual((7, 11), (moves.rival_up(self.board_game, white_bishop)), 'There is not a horse above the Bishop')

    def test_rival_up_Bishop_vs_pawn(self):
        white_bishop = pieces.Bishop('white', 8, 7)
        self.board_game.matrix[8][7] = 'B'

        black_pawn = pieces.Pawn('black', 5, 7)
        self.board_game.matrix[5][7] = 'p'

        self.assertEqual((5, 7), (moves.rival_up(self.board_game, white_bishop)), 'There is not a pawn above the Bishop')

    # Team pieces above Bishop
    def test_rival_up_Rook_vs_King(self):
        white_bishop = pieces.Bishop('white', 6, 7)
        self.board_game.matrix[6][7] = 'R'

        white_King = pieces.King('white', 1, 7)
        self.board_game.matrix[1][7] = 'K'

        self.assertIsNone(moves.rival_up(self.board_game, white_bishop), 'There is a rival above the Bishop')
    
    def test_rival_up_Rook_vs_Queen(self):
        white_bishop = pieces.Bishop('white', 11, 6)
        self.board_game.matrix[11][6] = 'R'

        white_queen = pieces.Bishop('white', 1, 6)
        self.board_game.matrix[1][6] = 'Q'

        self.assertIsNone(moves.rival_up(self.board_game, white_bishop), 'There is a rival above the Bishop')

    def test_rival_up_Rook_vs_Rook(self):
        white_rook1 = pieces.Bishop('white', 12, 15)
        self.board_game.matrix[12][15] = 'R'

        white_rook2 = pieces.Bishop('white', 0, 15)
        self.board_game.matrix[0][15] = 'R'

        self.assertIsNone(moves.rival_up(self.board_game, white_rook1), 'There is a rival above the Bishop')
    
    def test_rival_up_Rook_vs_Bishop(self):
        white_bishop = pieces.Bishop('white', 12, 13)
        self.board_game.matrix[12][13] = 'R'

        white_bishop = pieces.Bishop('white', 1, 13)
        self.board_game.matrix[1][13] = 'B'

        self.assertIsNone(moves.rival_up(self.board_game, white_bishop), 'There is a rival above the Bishop')

    def test_rival_up_Rook_vs_Horse(self):
        white_bishop = pieces.Bishop('white', 10, 11)
        self.board_game.matrix[10][11] = 'R'

        white_horse = pieces.Horse('white', 7, 11)
        self.board_game.matrix[7][11] = 'H'

        self.assertIsNone (moves.rival_up(self.board_game, white_bishop), 'There is a rival above the Bishop')

    def test_rival_up_Rook_vs_Pawn(self):
        white_bishop = pieces.Bishop('white', 8, 7)
        self.board_game.matrix[8][7] = 'R'

        white_pawn = pieces.Pawn('white', 5, 7)
        self.board_game.matrix[5][7] = 'P'

        self.assertIsNone(moves.rival_up(self.board_game, white_bishop), 'There is a rival above the Bishop')



    # queen (black)
    def test_rival_up_queen_vs_Pawn(self):
        black_queen = pieces.Queen('black', 13, 5)
        self.board_game.matrix[13][5] = 'q'

        white_pawn = pieces.Pawn('white', 10, 5)
        self.board_game.matrix[10][5] = 'P'

        self.assertEqual((10, 5), (moves.rival_up(self.board_game, black_queen)), 'There is not a pawn above')

    def test_rival_up_Pawn_vs_Pawn(self):
        white_pawn1 = pieces.Pawn('white', 15, 0)
        self.board_game.matrix[15][0] = 'P'

        white_pawn2 = pieces.Pawn('white', 4, 0)
        self.board_game.matrix[4][0] = 'P'

        self.assertIsNone((moves.rival_up(self.board_game, white_pawn1)), 'There is not a Pawn above')

    def test_rival_up_Pawn_vs_empty(self):
        white_pawn      = pieces.Pawn('white', 15, 0)
        self.board_game.matrix[15][0] = 'P'

        self.assertIsNone((moves.rival_up(self.board_game, white_pawn)), 'There are not empty squares above')
        

# Run the Tests
if __name__ == 'main':
    unittest.main()