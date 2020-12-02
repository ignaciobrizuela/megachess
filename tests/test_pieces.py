# Made by brz
import unittest
from scripts import pieces

class TestPieces(unittest.TestCase):

    ################################################################################################################
    #                                            VALID PARAMETERS                                                  #
    ################################################################################################################
    def throw_exception_color():
        pawn = pieces.Pawn('asdd', 0, 0)

    def test_valid_color(self):
        with self.assertRaises(Exception) as context:
            throw_exception_color()
            
            self.assertTrue('Color must be True(white) or False(black)' in  context.exception)

    def throw_exception_row_neg():
        pawn = pieces.Pawn(True, -1, 0)

    def test_valid_row(self):
        with self.assertRaises(Exception) as context:
            throw_exception_row_neg()
            
            self.assertTrue('Row must be an integer from 0 to 15' in  context.exception)

    def throw_exception_row_higher():
        pawn = pieces.Pawn(True, 50, 0)

    def test_valid_col(self):
        with self.assertRaises(Exception) as context:
            thcol_exception_col_higher()
            
            self.assertTrue('Col must be an integer from 0 to 15' in  context.exception)

    def throw_exception_col_neg():
        pawn = pieces.Pawn(True, -1, 0)

    def test_valid_col(self):
        with self.assertRaises(Exception) as context:
            thcol_exception_col_neg()
            
            self.assertTrue('Col must be an integer from 0 to 15' in  context.exception)

    def throw_exception_col_higher():
        pawn = pieces.Pawn(True, 50, 0)

    def test_valid_col(self):
        with self.assertRaises(Exception) as context:
            thcol_exception_col_higher()
            
            self.assertTrue('Col must be an integer from 0 to 15' in  context.exception)
            
    ################################################################################################################
    #                                                  PAWN                                                        #
    ################################################################################################################

    def test_blackpawn_valid_move_capture(self):
        pawn = pieces.Pawn(False, 3, 1)

        rival1 = pieces.Pawn(True, 4, 2)     # down_right
        rival2 = pieces.Pawn(True, 4, 0)     # down_left

        self.assertTrue(pawn.valid_move(rival1))
        self.assertTrue(pawn.valid_move(rival2))

    def test_blackpawn_invalid_move_capture(self):
        pawn = pieces.Pawn(False, 3, 1)

        rival1 = pieces.Pawn(True, 2, 1)     # up
        rival2 = pieces.Pawn(True, 2, 2)     # up_right
        rival3 = pieces.Pawn(True, 3, 2)     # right
        rival4 = pieces.Pawn(True, 2, 1)     # down
        rival5 = pieces.Pawn(True, 3, 0)     # left
        rival6 = pieces.Pawn(True, 2, 0)     # up_left

        self.assertFalse(pawn.valid_move(rival1))
        self.assertFalse(pawn.valid_move(rival2))
        self.assertFalse(pawn.valid_move(rival3))
        self.assertFalse(pawn.valid_move(rival4))
        self.assertFalse(pawn.valid_move(rival5))
        self.assertFalse(pawn.valid_move(rival6))

    def test_blackpawn_valid_move_jump(self):
        pawn = pieces.Pawn(False, 3, 1)

        empty_square1 = pieces.EmptySquare(4, 1)    # down
        empty_square2 = pieces.EmptySquare(5, 1)    # down

        self.assertTrue(pawn.valid_move(empty_square1))
        self.assertTrue(pawn.valid_move(empty_square2))

    def test_blackpawn_invalid_move_jump(self):
        pawn = pieces.Pawn(False, 3, 1)

        empty_square1 = pieces.EmptySquare(2, 1)    # up
        empty_square2 = pieces.EmptySquare(2, 2)    # up_right
        empty_square3 = pieces.EmptySquare(3, 2)    # right
        empty_square4 = pieces.EmptySquare(4, 2)    # down_right
        empty_square5 = pieces.EmptySquare(4, 0)    # down_left
        empty_square6 = pieces.EmptySquare(3, 0)    # left
        empty_square7 = pieces.EmptySquare(2, 0)    # up_left

        self.assertFalse(pawn.valid_move(empty_square1))
        self.assertFalse(pawn.valid_move(empty_square2))
        self.assertFalse(pawn.valid_move(empty_square3))
        self.assertFalse(pawn.valid_move(empty_square4))
        self.assertFalse(pawn.valid_move(empty_square5))
        self.assertFalse(pawn.valid_move(empty_square6))
        self.assertFalse(pawn.valid_move(empty_square7))

    
    def test_whitepawn_valid_move_jump(self):
        pawn = pieces.Pawn(True, 12, 1)

        empty_square1 = pieces.EmptySquare(11, 1)   # up
        empty_square2 = pieces.EmptySquare(10, 1)   # up

        self.assertTrue(pawn.valid_move(empty_square1))
        self.assertTrue(pawn.valid_move(empty_square2))

    def test_whitepawn_invalid_move_jump(self):
        pawn = pieces.Pawn(True, 12, 1)

        empty_square1 = pieces.EmptySquare(11, 2)   # up_right
        empty_square2 = pieces.EmptySquare(12, 2)   # rigth
        empty_square3 = pieces.EmptySquare(13, 2)   # down_right    
        empty_square4 = pieces.EmptySquare(13, 1)   # down
        empty_square5 = pieces.EmptySquare(13, 0)   # down_left
        empty_square6 = pieces.EmptySquare(12, 0)   # left
        empty_square7 = pieces.EmptySquare(11, 0)   # up_left

        self.assertFalse(pawn.valid_move(empty_square1))
        self.assertFalse(pawn.valid_move(empty_square2))
        self.assertFalse(pawn.valid_move(empty_square3))
        self.assertFalse(pawn.valid_move(empty_square4))
        self.assertFalse(pawn.valid_move(empty_square5))
        self.assertFalse(pawn.valid_move(empty_square6))
        self.assertFalse(pawn.valid_move(empty_square7))

    def test_whitepawn_valid_move_capture(self):
        pawn = pieces.Pawn(True, 12, 1)

        rival1 = pieces.Pawn(False, 11, 2)    # up_right
        rival2 = pieces.Pawn(False, 11, 0)    # up_left

        self.assertTrue(pawn.valid_move(rival1))
        self.assertTrue(pawn.valid_move(rival2))


    def test_whitepawn_invalid_move_capture(self):
        pawn = pieces.Pawn(True, 12, 1)

        rival1 = pieces.Pawn(False, 13, 1)     # up
        rival2 = pieces.Pawn(False, 12, 2)     # right
        rival3 = pieces.Pawn(False, 13, 2)     # down_right
        rival4 = pieces.Pawn(False, 13, 1)     # down
        rival5 = pieces.Pawn(False, 13, 0)     # down_left
        rival6 = pieces.Pawn(False, 12, 0)     # left

        self.assertFalse(pawn.valid_move(rival1))
        self.assertFalse(pawn.valid_move(rival2))
        self.assertFalse(pawn.valid_move(rival3))
        self.assertFalse(pawn.valid_move(rival4))
        self.assertFalse(pawn.valid_move(rival5))
        self.assertFalse(pawn.valid_move(rival6))
    
    ################################################################################################################
    #                                                  HORSE                                                       #
    ################################################################################################################

    def test_blackhorse_valid_move_capture(self):
        horse = pieces.Horse(False, 8, 8)

        rival1 = pieces.Pawn(True, 6, 9)     # up_right
        rival2 = pieces.Pawn(True, 10, 9)    # down_right
        rival3 = pieces.Pawn(True, 10, 7)    # down_left
        rival4 = pieces.Pawn(True, 6, 7)     # up_left

        self.assertTrue(horse.valid_move(rival1))
        self.assertTrue(horse.valid_move(rival2))
        self.assertTrue(horse.valid_move(rival3))
        self.assertTrue(horse.valid_move(rival4))

    def test_blackhorse_invalid_move_capture(self):
        horse = pieces.Horse(False, 8, 8)

        rival1 = pieces.Pawn(True, 7, 8)     # up
        rival2 = pieces.Pawn(True, 8, 9)     # right
        rival3 = pieces.Pawn(True, 9, 8)     # down
        rival4 = pieces.Pawn(True, 8, 7)     # left

        self.assertFalse(horse.valid_move(rival1))
        self.assertFalse(horse.valid_move(rival2))
        self.assertFalse(horse.valid_move(rival3))
        self.assertFalse(horse.valid_move(rival4))

    def test_blackhorse_valid_move_jump(self):
        horse = pieces.Horse(False, 8, 8)

        empty_square1 = pieces.EmptySquare(6, 9)     # up_right
        empty_square2 = pieces.EmptySquare(10, 9)    # down_right
        empty_square3 = pieces.EmptySquare(10, 7)    # down_left
        empty_square4 = pieces.EmptySquare(6, 7)     # up_left

        self.assertTrue(horse.valid_move(empty_square1))
        self.assertTrue(horse.valid_move(empty_square2))
        self.assertTrue(horse.valid_move(empty_square3))
        self.assertTrue(horse.valid_move(empty_square4))

    def test_blackhorse_invalid_move_jump(self):
        horse = pieces.Horse(False, 8, 8)

        empty_square1 = pieces.EmptySquare(7, 8)     # up
        empty_square2 = pieces.EmptySquare(8, 9)     # right
        empty_square3 = pieces.EmptySquare(9, 8)     # down
        empty_square4 = pieces.EmptySquare(8, 7)     # left

        self.assertFalse(horse.valid_move(empty_square1))
        self.assertFalse(horse.valid_move(empty_square2))
        self.assertFalse(horse.valid_move(empty_square3))
        self.assertFalse(horse.valid_move(empty_square4))

    def test_whitehorse_valid_move_capture(self):
        horse = pieces.Horse(True, 8, 8)

        rival1 = pieces.Pawn(False, 6, 9)     # up_right
        rival2 = pieces.Pawn(False, 10, 9)    # down_right
        rival3 = pieces.Pawn(False, 10, 7)    # down_left
        rival4 = pieces.Pawn(False, 6, 7)     # up_left

        self.assertTrue(horse.valid_move(rival1))
        self.assertTrue(horse.valid_move(rival2))
        self.assertTrue(horse.valid_move(rival3))
        self.assertTrue(horse.valid_move(rival4))

    def test_whitehorse_invalid_move_capture(self):
        horse = pieces.Horse(True, 8, 8)

        rival1 = pieces.Pawn(False, 7, 8)     # up
        rival2 = pieces.Pawn(False, 8, 9)     # right
        rival3 = pieces.Pawn(False, 9, 8)     # down
        rival4 = pieces.Pawn(False, 8, 7)     # left

        self.assertFalse(horse.valid_move(rival1))
        self.assertFalse(horse.valid_move(rival2))
        self.assertFalse(horse.valid_move(rival3))
        self.assertFalse(horse.valid_move(rival4))

    def test_whitehorse_valid_move_jump(self):
        horse = pieces.Horse(True, 8, 8)

        empty_square1 = pieces.EmptySquare(6, 9)     # up_right
        empty_square2 = pieces.EmptySquare(10, 9)    # down_right
        empty_square3 = pieces.EmptySquare(10, 7)    # down_left
        empty_square4 = pieces.EmptySquare(6, 7)     # up_left

        self.assertTrue(horse.valid_move(empty_square1))
        self.assertTrue(horse.valid_move(empty_square2))
        self.assertTrue(horse.valid_move(empty_square3))
        self.assertTrue(horse.valid_move(empty_square4))

    def test_whitehorse_invalid_move_jump(self):
        horse = pieces.Horse(True, 8, 8)

        empty_square1 = pieces.EmptySquare(7, 8)     # up
        empty_square2 = pieces.EmptySquare(8, 9)     # right
        empty_square3 = pieces.EmptySquare(9, 8)     # down
        empty_square4 = pieces.EmptySquare(8, 7)     # left

        self.assertFalse(horse.valid_move(empty_square1))
        self.assertFalse(horse.valid_move(empty_square2))
        self.assertFalse(horse.valid_move(empty_square3))
        self.assertFalse(horse.valid_move(empty_square4))

    ################################################################################################################
    #                                                  BISHOP                                                      #
    ################################################################################################################

    def test_blackbishop_valid_move_capture(self):
        bishop = pieces.Bishop(False, 7, 7)

        rival1 = pieces.Pawn(True, 3, 3)     # up_left
        rival2 = pieces.Pawn(True, 5, 9)     # up_right
        rival3 = pieces.Pawn(True, 11, 11)   # down_right
        rival4 = pieces.Pawn(True, 8, 6)     # down_left

        self.assertTrue(bishop.valid_move(rival1))
        self.assertTrue(bishop.valid_move(rival2))
        self.assertTrue(bishop.valid_move(rival3))
        self.assertTrue(bishop.valid_move(rival4))

    def test_blackbishop_invalid_move_capture(self):
        bishop = pieces.Bishop(False, 7, 7)

        rival1 = pieces.Pawn(True, 6, 7)     # up
        rival2 = pieces.Pawn(True, 7, 9)     # right
        rival3 = pieces.Pawn(True, 11, 7)    # down
        rival4 = pieces.Pawn(True, 7, 1)     # left

        self.assertFalse(bishop.valid_move(rival1))
        self.assertFalse(bishop.valid_move(rival2))
        self.assertFalse(bishop.valid_move(rival3))
        self.assertFalse(bishop.valid_move(rival4))

    def test_blackbishop_valid_move_jump(self):
        bishop = pieces.Bishop(False, 7, 7)

        empty_square1 = pieces.EmptySquare(3, 3)        # up_left
        empty_square2 = pieces.EmptySquare(5, 9)        # up_right
        empty_square3 = pieces.EmptySquare(11, 11)      # down_right
        empty_square4 = pieces.EmptySquare(8, 6)        # down_left

        self.assertTrue(bishop.valid_move(empty_square1))
        self.assertTrue(bishop.valid_move(empty_square2))
        self.assertTrue(bishop.valid_move(empty_square3))
        self.assertTrue(bishop.valid_move(empty_square4))

    def test_blackbishop_invalid_move_jump(self):
        bishop = pieces.Bishop(False, 7, 7)

        empty_square1 = pieces.EmptySquare(6, 7)     # up
        empty_square2 = pieces.EmptySquare(7, 9)     # right
        empty_square3 = pieces.EmptySquare(11, 7)    # down
        empty_square4 = pieces.EmptySquare(7, 1)     # left

        self.assertFalse(bishop.valid_move(empty_square1))
        self.assertFalse(bishop.valid_move(empty_square2))
        self.assertFalse(bishop.valid_move(empty_square3))
        self.assertFalse(bishop.valid_move(empty_square4))

    def test_whitebishop_valid_move_capture(self):
        bishop = pieces.Bishop(True, 7, 7)

        rival1 = pieces.Pawn(False, 3, 3)     # up_left
        rival2 = pieces.Pawn(False, 5, 9)     # up_right
        rival3 = pieces.Pawn(False, 11, 11)   # down_right
        rival4 = pieces.Pawn(False, 8, 6)     # down_left

        self.assertTrue(bishop.valid_move(rival1))
        self.assertTrue(bishop.valid_move(rival2))
        self.assertTrue(bishop.valid_move(rival3))
        self.assertTrue(bishop.valid_move(rival4))

    def test_whitebishop_invalid_move_capture(self):
        bishop = pieces.Bishop(True, 7, 7)

        rival1 = pieces.Pawn(False, 6, 7)     # up
        rival2 = pieces.Pawn(False, 7, 9)     # right
        rival3 = pieces.Pawn(False, 11, 7)   # down
        rival4 = pieces.Pawn(False, 7, 1)     # left

        self.assertFalse(bishop.valid_move(rival1))
        self.assertFalse(bishop.valid_move(rival2))
        self.assertFalse(bishop.valid_move(rival3))
        self.assertFalse(bishop.valid_move(rival4))

    def test_whitebishop_valid_move_jump(self):
        bishop = pieces.Bishop(True, 7, 7)

        empty_square1 = pieces.EmptySquare(3, 3)        # up_left
        empty_square2 = pieces.EmptySquare(5, 9)        # up_right
        empty_square3 = pieces.EmptySquare(11, 11)      # down_right
        empty_square4 = pieces.EmptySquare(8, 6)        # down_left

        self.assertTrue(bishop.valid_move(empty_square1))
        self.assertTrue(bishop.valid_move(empty_square2))
        self.assertTrue(bishop.valid_move(empty_square3))
        self.assertTrue(bishop.valid_move(empty_square4))

    def test_whitebishop_invalid_move_jump(self):
        bishop = pieces.Bishop(True, 7, 7)

        empty_square1 = pieces.EmptySquare(6, 7)     # up
        empty_square2 = pieces.EmptySquare(7, 9)     # right
        empty_square3 = pieces.EmptySquare(11, 7)    # down
        empty_square4 = pieces.EmptySquare(7, 1)     # left

        self.assertFalse(bishop.valid_move(empty_square1))
        self.assertFalse(bishop.valid_move(empty_square2))
        self.assertFalse(bishop.valid_move(empty_square3))
        self.assertFalse(bishop.valid_move(empty_square4))

    ################################################################################################################
    #                                                  ROOK                                                        #
    ################################################################################################################

    def test_blackrook_valid_move_capture(self):
        rook = pieces.Rook(False, 7, 7)

        rival1 = pieces.Pawn(True, 0, 7)     # up
        rival2 = pieces.Pawn(True, 7, 5)     # right
        rival3 = pieces.Pawn(True, 12, 7)    # down
        rival4 = pieces.Pawn(True, 7, 1)     # left

        self.assertTrue(rook.valid_move(rival1))
        self.assertTrue(rook.valid_move(rival2))
        self.assertTrue(rook.valid_move(rival3))
        self.assertTrue(rook.valid_move(rival4))

    def test_blackrook_invalid_move_capture(self):
        rook = pieces.Rook(False, 7, 7)

        rival1 = pieces.Pawn(True, 5, 5)     # up_rigth
        rival2 = pieces.Pawn(True, 9, 9)     # down_right
        rival3 = pieces.Pawn(True, 9, 5)     # down_left
        rival4 = pieces.Pawn(True, 3, 3)     # up_left

        self.assertFalse(rook.valid_move(rival1))
        self.assertFalse(rook.valid_move(rival2))
        self.assertFalse(rook.valid_move(rival3))
        self.assertFalse(rook.valid_move(rival4))

    def test_blackrook_valid_move_jump(self):
        rook = pieces.Rook(False, 7, 7)

        empty_square1 = pieces.EmptySquare(0, 7)     # up
        empty_square2 = pieces.EmptySquare(7, 5)     # right
        empty_square3 = pieces.EmptySquare(12, 7)    # down
        empty_square4 = pieces.EmptySquare(7, 1)     # left

        self.assertTrue(rook.valid_move(empty_square1))
        self.assertTrue(rook.valid_move(empty_square2))
        self.assertTrue(rook.valid_move(empty_square3))
        self.assertTrue(rook.valid_move(empty_square4))

    def test_blackrook_invalid_move_jump(self):
        rook = pieces.Rook(False, 7, 7)

        empty_square1 = pieces.EmptySquare(5, 5)     # up_rigth
        empty_square2 = pieces.EmptySquare(9, 9)     # down_right
        empty_square3 = pieces.EmptySquare(9, 5)     # down_left
        empty_square4 = pieces.EmptySquare(3, 3)     # up_left

        self.assertFalse(rook.valid_move(empty_square1))
        self.assertFalse(rook.valid_move(empty_square2))
        self.assertFalse(rook.valid_move(empty_square3))
        self.assertFalse(rook.valid_move(empty_square4))

    def test_whiterook_valid_move_capture(self):
        rook = pieces.Rook(True, 7, 7)

        rival1 = pieces.Pawn(False, 0, 7)     # up
        rival2 = pieces.Pawn(False, 7, 5)     # right
        rival3 = pieces.Pawn(False, 12, 7)     # down
        rival4 = pieces.Pawn(False, 7, 1)     # left

        self.assertTrue(rook.valid_move(rival1))
        self.assertTrue(rook.valid_move(rival2))
        self.assertTrue(rook.valid_move(rival3))
        self.assertTrue(rook.valid_move(rival4))

    def test_whiterook_invalid_move_capture(self):
        rook = pieces.Rook(True, 7, 7)

        rival1 = pieces.Pawn(False, 5, 5)     # up_rigth
        rival2 = pieces.Pawn(False, 9, 9)     # down_right
        rival3 = pieces.Pawn(False, 9, 5)     # down_left
        rival4 = pieces.Pawn(False, 3, 3)     # up_left

        self.assertFalse(rook.valid_move(rival1))
        self.assertFalse(rook.valid_move(rival2))
        self.assertFalse(rook.valid_move(rival3))
        self.assertFalse(rook.valid_move(rival4))

    def test_whiterook_valid_move_jump(self):
        rook = pieces.Rook(True, 7, 7)

        empty_square1 = pieces.EmptySquare(0, 7)     # up
        empty_square2 = pieces.EmptySquare(7, 5)     # right
        empty_square3 = pieces.EmptySquare(12, 7)    # down
        empty_square4 = pieces.EmptySquare(7, 1)     # left

        self.assertTrue(rook.valid_move(empty_square1))
        self.assertTrue(rook.valid_move(empty_square2))
        self.assertTrue(rook.valid_move(empty_square3))
        self.assertTrue(rook.valid_move(empty_square4))

    def test_whiterook_invalid_move_jump(self):
        rook = pieces.Rook(True, 7, 7)

        empty_square1 = pieces.EmptySquare(5, 5)     # up_rigth
        empty_square2 = pieces.EmptySquare(9, 9)     # down_right
        empty_square3 = pieces.EmptySquare(9, 5)     # down_left
        empty_square4 = pieces.EmptySquare(3, 3)     # up_left

        self.assertFalse(rook.valid_move(empty_square1))
        self.assertFalse(rook.valid_move(empty_square2))
        self.assertFalse(rook.valid_move(empty_square3))
        self.assertFalse(rook.valid_move(empty_square4))

    ################################################################################################################
    #                                                  QUEEN                                                       #
    ################################################################################################################

    def test_blackqueen_valid_move_capture(self):
        queen = pieces.Queen(False, 8, 8)

        rival1 = pieces.Pawn(True, 1, 8)     # up
        rival2 = pieces.Pawn(True, 5, 11)    # up_right
        rival3 = pieces.Pawn(True, 8, 15)    # right
        rival4 = pieces.Pawn(True, 11, 11)   # down_right
        rival5 = pieces.Pawn(True, 12, 8)    # down
        rival6 = pieces.Pawn(True, 10, 6)    # down_left
        rival7 = pieces.Pawn(True, 8, 3)     # left
        rival8 = pieces.Pawn(True, 5, 5)     # up_left

        self.assertTrue(queen.valid_move(rival1))
        self.assertTrue(queen.valid_move(rival2))
        self.assertTrue(queen.valid_move(rival3))
        self.assertTrue(queen.valid_move(rival4))
        self.assertTrue(queen.valid_move(rival5))
        self.assertTrue(queen.valid_move(rival6))
        self.assertTrue(queen.valid_move(rival7))
        self.assertTrue(queen.valid_move(rival8))
    
    def test_blackqueen_valid_move_jump(self):
        queen = pieces.Queen(False, 8, 8)

        empty_square1 = pieces.EmptySquare(1, 8)     # up
        empty_square2 = pieces.EmptySquare(5, 11)    # up_right
        empty_square3 = pieces.EmptySquare(8, 15)    # right
        empty_square4 = pieces.EmptySquare(11, 11)   # down_right
        empty_square5 = pieces.EmptySquare(12, 8)    # down
        empty_square6 = pieces.EmptySquare(10, 6)    # down_left
        empty_square7 = pieces.EmptySquare(8, 3)     # left
        empty_square8 = pieces.EmptySquare(5, 5)     # up_left

        self.assertTrue(queen.valid_move(empty_square1))
        self.assertTrue(queen.valid_move(empty_square2))
        self.assertTrue(queen.valid_move(empty_square3))
        self.assertTrue(queen.valid_move(empty_square4))
        self.assertTrue(queen.valid_move(empty_square5))
        self.assertTrue(queen.valid_move(empty_square6))
        self.assertTrue(queen.valid_move(empty_square7))
        self.assertTrue(queen.valid_move(empty_square8))

    def test_whitekqueen_valid_move_capture(self):
        queen = pieces.Queen(True, 8, 8)

        rival1 = pieces.Pawn(False, 1, 8)     # up
        rival2 = pieces.Pawn(False, 5, 11)    # up_right
        rival3 = pieces.Pawn(False, 8, 15)    # right
        rival4 = pieces.Pawn(False, 11, 11)   # down_right
        rival5 = pieces.Pawn(False, 12, 8)    # down
        rival6 = pieces.Pawn(False, 10, 6)    # down_left
        rival7 = pieces.Pawn(False, 8, 3)     # left
        rival8 = pieces.Pawn(False, 5, 5)     # up_left

        self.assertTrue(queen.valid_move(rival1))
        self.assertTrue(queen.valid_move(rival2))
        self.assertTrue(queen.valid_move(rival3))
        self.assertTrue(queen.valid_move(rival4))
        self.assertTrue(queen.valid_move(rival5))
        self.assertTrue(queen.valid_move(rival6))
        self.assertTrue(queen.valid_move(rival7))
        self.assertTrue(queen.valid_move(rival8))

    def test_whitekqueen_valid_move_jump(self):
        queen = pieces.Queen(True, 8, 8)

        empty_square1 = pieces.EmptySquare(1, 8)     # up
        empty_square2 = pieces.EmptySquare(5, 11)    # up_right
        empty_square3 = pieces.EmptySquare(8, 15)    # right
        empty_square4 = pieces.EmptySquare(11, 11)   # down_right
        empty_square5 = pieces.EmptySquare(12, 8)    # down
        empty_square6 = pieces.EmptySquare(10, 6)   # down_left
        empty_square7 = pieces.EmptySquare(8, 3)     # left
        empty_square8 = pieces.EmptySquare(5, 5)     # up_left

        self.assertTrue(queen.valid_move(empty_square1))
        self.assertTrue(queen.valid_move(empty_square2))
        self.assertTrue(queen.valid_move(empty_square3))
        self.assertTrue(queen.valid_move(empty_square4))
        self.assertTrue(queen.valid_move(empty_square5))
        self.assertTrue(queen.valid_move(empty_square6))
        self.assertTrue(queen.valid_move(empty_square7))
        self.assertTrue(queen.valid_move(empty_square8))    

    ################################################################################################################
    #                                                  KING                                                       #
    ################################################################################################################

    def test_blackking_valid_move_capture(self):
        king = pieces.King(False, 8, 8)

        rival1 = pieces.Pawn(True, 7, 8)     # up
        rival2 = pieces.Pawn(True, 7, 9)     # up_right
        rival3 = pieces.Pawn(True, 8, 9)     # right
        rival4 = pieces.Pawn(True, 9, 9)     # down_right
        rival5 = pieces.Pawn(True, 9, 8)    # down
        rival6 = pieces.Pawn(True, 9, 7)    # down_left
        rival7 = pieces.Pawn(True, 8, 7)     # left
        rival8 = pieces.Pawn(True, 7, 7)     # up_left

        self.assertTrue(king.valid_move(rival1))
        self.assertTrue(king.valid_move(rival2))
        self.assertTrue(king.valid_move(rival3))
        self.assertTrue(king.valid_move(rival4))
        self.assertTrue(king.valid_move(rival5))
        self.assertTrue(king.valid_move(rival6))
        self.assertTrue(king.valid_move(rival7))
        self.assertTrue(king.valid_move(rival8))
    
    def test_blackking_valid_move_jump(self):
        king = pieces.King(False, 8, 8)

        empty_square1 = pieces.EmptySquare(7, 8)     # up
        empty_square2 = pieces.EmptySquare(7, 9)     # up_right
        empty_square3 = pieces.EmptySquare(8, 9)     # right
        empty_square4 = pieces.EmptySquare(9, 9)     # down_right
        empty_square5 = pieces.EmptySquare(9, 8)    # down
        empty_square6 = pieces.EmptySquare(9, 7)    # down_left
        empty_square7 = pieces.EmptySquare(8, 7)     # left
        empty_square8 = pieces.EmptySquare(7, 7)     # up_left

        self.assertTrue(king.valid_move(empty_square1))
        self.assertTrue(king.valid_move(empty_square2))
        self.assertTrue(king.valid_move(empty_square3))
        self.assertTrue(king.valid_move(empty_square4))
        self.assertTrue(king.valid_move(empty_square5))
        self.assertTrue(king.valid_move(empty_square6))
        self.assertTrue(king.valid_move(empty_square7))
        self.assertTrue(king.valid_move(empty_square8))

    def test_whitekking_valid_move_capture(self):
        king = pieces.King(True, 8, 8)

        rival1 = pieces.Pawn(False, 7, 8)     # up
        rival2 = pieces.Pawn(False, 7, 9)     # up_right
        rival3 = pieces.Pawn(False, 8, 9)     # right
        rival4 = pieces.Pawn(False, 9, 9)     # down_right
        rival5 = pieces.Pawn(False, 9, 8)    # down
        rival6 = pieces.Pawn(False, 9, 7)    # down_left
        rival7 = pieces.Pawn(False, 8, 7)     # left
        rival8 = pieces.Pawn(False, 7, 7)     # up_left

        self.assertTrue(king.valid_move(rival1))
        self.assertTrue(king.valid_move(rival2))
        self.assertTrue(king.valid_move(rival3))
        self.assertTrue(king.valid_move(rival4))
        self.assertTrue(king.valid_move(rival5))
        self.assertTrue(king.valid_move(rival6))
        self.assertTrue(king.valid_move(rival7))
        self.assertTrue(king.valid_move(rival8))

    def test_whitekking_valid_move_jump(self):
        king = pieces.King(True, 8, 8)

        empty_square1 = pieces.EmptySquare(7, 8)     # up
        empty_square2 = pieces.EmptySquare(7, 9)     # up_right
        empty_square3 = pieces.EmptySquare(8, 9)     # right
        empty_square4 = pieces.EmptySquare(9, 9)     # down_right
        empty_square5 = pieces.EmptySquare(9, 8)    # down
        empty_square6 = pieces.EmptySquare(9, 7)    # down_left
        empty_square7 = pieces.EmptySquare(8, 7)     # left
        empty_square8 = pieces.EmptySquare(7, 7)     # up_left

        self.assertTrue(king.valid_move(empty_square1))
        self.assertTrue(king.valid_move(empty_square2))
        self.assertTrue(king.valid_move(empty_square3))
        self.assertTrue(king.valid_move(empty_square4))
        self.assertTrue(king.valid_move(empty_square5))
        self.assertTrue(king.valid_move(empty_square6))
        self.assertTrue(king.valid_move(empty_square7))
        self.assertTrue(king.valid_move(empty_square8))


# if __name__ == 'main':
#     unittest.main()