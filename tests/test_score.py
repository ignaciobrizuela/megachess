# Made by brz
import unittest
from scripts import pieces
from scripts import score


class TestScore(unittest.TestCase):

    def test_jump_blackpawn(self):
        factor = 1
        black_pawn1 = pieces.Pawn(False, 3, 6)       # center-front
        black_pawn2 = pieces.Pawn(False, 2, 6)       # center-back
        black_pawn3 = pieces.Pawn(False, 3, 2)       # side-front
        black_pawn4 = pieces.Pawn(False, 3, 12)      # side-front
        black_pawn5 = pieces.Pawn(False, 2, 2)       # side-back
        black_pawn6 = pieces.Pawn(False, 2, 12)      # side-back
        black_pawn7 = pieces.Pawn(False, 3, 9)      # king-front
        black_pawn8 = pieces.Pawn(False, 2, 9)      # king-back

        square1 = pieces.EmptySquare(4, 6)       
        square2 = pieces.EmptySquare(3, 6)       
        square3 = pieces.EmptySquare(4, 2)   
        square4 = pieces.EmptySquare(4, 12)   
        square5 = pieces.EmptySquare(3, 2)     
        square6 = pieces.EmptySquare(3, 12) 
        square7 = pieces.EmptySquare(4, 9)   
        square8 = pieces.EmptySquare(3, 9)  

        self.assertEqual(62.29, score.jump_pawn(black_pawn1, square1,factor))
        self.assertEqual(61.22, score.jump_pawn(black_pawn2, square2,factor))
        self.assertEqual(60.29, score.jump_pawn(black_pawn3, square3,factor))
        self.assertEqual(60.29, score.jump_pawn(black_pawn4, square4,factor))
        self.assertEqual(60.22, score.jump_pawn(black_pawn5, square5,factor))
        self.assertEqual(60.22, score.jump_pawn(black_pawn6, square6,factor))
        self.assertEqual(62.29, score.jump_pawn(black_pawn7, square7,factor))
        self.assertEqual(62.22, score.jump_pawn(black_pawn8, square8,factor))

    def test_jump_rival_blackpawn(self):
        factor = -1
        black_pawn1 = pieces.Pawn(False, 3, 6)       # center-front
        black_pawn2 = pieces.Pawn(False, 2, 6)       # center-back
        black_pawn3 = pieces.Pawn(False, 3, 2)       # side-front
        black_pawn4 = pieces.Pawn(False, 3, 12)      # side-front
        black_pawn5 = pieces.Pawn(False, 2, 2)       # side-back
        black_pawn6 = pieces.Pawn(False, 2, 12)      # side-back
        black_pawn7 = pieces.Pawn(False, 3, 9)      # king-front
        black_pawn8 = pieces.Pawn(False, 2, 9)      # king-back

        square1 = pieces.EmptySquare(4, 6)       
        square2 = pieces.EmptySquare(3, 6)       
        square3 = pieces.EmptySquare(4, 2)   
        square4 = pieces.EmptySquare(4, 12)   
        square5 = pieces.EmptySquare(3, 2)     
        square6 = pieces.EmptySquare(3, 12) 
        square7 = pieces.EmptySquare(4, 9)   
        square8 = pieces.EmptySquare(3, 9)  

        self.assertEqual(-62.29, score.jump_pawn(black_pawn1, square1,factor))
        self.assertEqual(-61.22, score.jump_pawn(black_pawn2, square2,factor))
        self.assertEqual(-60.29, score.jump_pawn(black_pawn3, square3,factor))
        self.assertEqual(-60.29, score.jump_pawn(black_pawn4, square4,factor))
        self.assertEqual(-60.22, score.jump_pawn(black_pawn5, square5,factor))
        self.assertEqual(-60.22, score.jump_pawn(black_pawn6, square6,factor))
        self.assertEqual(-62.29, score.jump_pawn(black_pawn7, square7,factor))
        self.assertEqual(-62.22, score.jump_pawn(black_pawn8, square8,factor))

    
    def test_jump_whitepawn(self):
        factor = 1
        white_pawn1 = pieces.Pawn(True, 12, 6)       # center-front
        white_pawn2 = pieces.Pawn(True, 13, 6)       # center-back
        white_pawn3 = pieces.Pawn(True, 12, 2)       # side-front
        white_pawn4 = pieces.Pawn(True, 12, 12)      # side-front
        white_pawn5 = pieces.Pawn(True, 13, 2)       # side-back
        white_pawn6 = pieces.Pawn(True, 13, 12)      # side-back
        white_pawn7 = pieces.Pawn(True, 12, 9)      # king-front
        white_pawn8 = pieces.Pawn(True, 13, 9)      # king-back

        square1 = pieces.EmptySquare(11, 6)       
        square2 = pieces.EmptySquare(12, 6)       
        square3 = pieces.EmptySquare(11, 2)   
        square4 = pieces.EmptySquare(11, 12)   
        square5 = pieces.EmptySquare(12, 2)     
        square6 = pieces.EmptySquare(12, 12) 
        square7 = pieces.EmptySquare(11, 9)   
        square8 = pieces.EmptySquare(12, 9)  

        self.assertEqual(62.29, score.jump_pawn(white_pawn1, square1,factor))
        self.assertEqual(61.22, score.jump_pawn(white_pawn2, square2,factor))
        self.assertEqual(60.29, score.jump_pawn(white_pawn3, square3,factor))
        self.assertEqual(60.29, score.jump_pawn(white_pawn4, square4,factor))
        self.assertEqual(60.22, score.jump_pawn(white_pawn5, square5,factor))
        self.assertEqual(60.22, score.jump_pawn(white_pawn6, square6,factor))
        self.assertEqual(62.29, score.jump_pawn(white_pawn7, square7,factor))
        self.assertEqual(62.22, score.jump_pawn(white_pawn8, square8,factor))


    def test_jump_rival_whitepawn(self):
        factor = -1
        white_pawn1 = pieces.Pawn(True, 12, 6)       # center-front
        white_pawn2 = pieces.Pawn(True, 13, 6)       # center-back
        white_pawn3 = pieces.Pawn(True, 12, 2)       # side-front
        white_pawn4 = pieces.Pawn(True, 12, 12)      # side-front
        white_pawn5 = pieces.Pawn(True, 13, 2)       # side-back
        white_pawn6 = pieces.Pawn(True, 13, 12)      # side-back
        white_pawn7 = pieces.Pawn(True, 12, 9)      # king-front
        white_pawn8 = pieces.Pawn(True, 13, 9)      # king-back

        square1 = pieces.EmptySquare(11, 6)       
        square2 = pieces.EmptySquare(12, 6)       
        square3 = pieces.EmptySquare(11, 2)   
        square4 = pieces.EmptySquare(11, 12)   
        square5 = pieces.EmptySquare(12, 2)     
        square6 = pieces.EmptySquare(12, 12) 
        square7 = pieces.EmptySquare(11, 9)   
        square8 = pieces.EmptySquare(12, 9)  

        self.assertEqual(-62.29, score.jump_pawn(white_pawn1, square1,factor))
        self.assertEqual(-61.22, score.jump_pawn(white_pawn2, square2,factor))
        self.assertEqual(-60.29, score.jump_pawn(white_pawn3, square3,factor))
        self.assertEqual(-60.29, score.jump_pawn(white_pawn4, square4,factor))
        self.assertEqual(-60.22, score.jump_pawn(white_pawn5, square5,factor))
        self.assertEqual(-60.22, score.jump_pawn(white_pawn6, square6,factor))
        self.assertEqual(-62.29, score.jump_pawn(white_pawn7, square7,factor))
        self.assertEqual(-62.22, score.jump_pawn(white_pawn8, square8,factor))

    def test_jump_horse(self):
        factor = 1
        horse = pieces.Horse(True, 8, 8)
        
        self.assertEqual(7, score.jump_piece(horse, factor))

    def test_jump_rival_horse(self):
        factor = -1
        horse = pieces.Horse(True, 8, 8)
        
        self.assertEqual(-7, score.jump_piece(horse, factor))

    def test_jump_bishop(self):
        factor = 1
        bishop = pieces.Bishop(True, 8, 8)
        
        self.assertEqual(8, score.jump_piece(bishop, factor))

    def test_jump_rival_bishop(self):
        factor = -1
        bishop = pieces.Bishop(True, 8, 8)
        
        self.assertEqual(-8, score.jump_piece(bishop, factor))


    def test_jump_rook(self):
        factor = 1
        rook = pieces.Rook(True, 8, 8)
        
        self.assertEqual(9, score.jump_piece(rook, factor))

    def test_jump_rival_rook(self):
        factor = -1
        rook = pieces.Rook(True, 8, 8)
        
        self.assertEqual(-9, score.jump_piece(rook, factor))

    def test_jump_queen(self):
        factor = 1
        queen = pieces.Queen(True, 8, 8)
        
        self.assertEqual(6, score.jump_piece(queen, factor))

    def test_jump_rival_queen(self):
        factor = -1
        queen = pieces.Queen(True, 8, 8)
        
        self.assertEqual(-6, score.jump_piece(queen, factor))


    def test_jump_king(self):
        factor = 1
        king = pieces.King(True, 8, 8)
        
        self.assertEqual(5, score.jump_piece(king, factor))

    def test_jump_rival_king(self):
        factor = -1
        king = pieces.King(True, 8, 8)
        
        self.assertEqual(-5, score.jump_piece(king, factor))

    
    def test_protect_center_10(self):
        white_queen = pieces.Queen(True, 15, 15)
        black_queen = pieces.Queen(False, 8, 8)

        self.assertEqual(10, score.protect_center(white_queen, black_queen))

    
    def test_protect_center_5(self):
        white_queen = pieces.Queen(True, 9, 9)
        black_queen = pieces.Queen(False, 8, 8)

        self.assertEqual(5, score.protect_center(white_queen, black_queen))


    def test_protect_center_3(self):
        white_queen = pieces.Queen(True, 15,15)
        black_queen = pieces.Queen(False, 0, 15)

        self.assertEqual(3, score.protect_center(white_queen, black_queen))

    
    def test_protect_center_1(self):
        white_queen = pieces.Queen(True, 8, 8)
        black_queen = pieces.Queen(False, 15, 15)

        self.assertEqual(1, score.protect_center(white_queen, black_queen))

    
    def test_capture_piece_pawn_good(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_pawn = pieces.Pawn(True, 7, 8)

        self.assertEqual(105, score.capture_piece(black_queen, white_pawn, factor))


    def test_capture_piece_pawn_bad(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_pawn = pieces.Pawn(True, 12, 8)

        self.assertEqual(11, score.capture_piece(black_queen, white_pawn, factor))


    def test_capture_piece_horse_good(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_horse = pieces.Horse(True, 9, 8)

        self.assertEqual(305, score.capture_piece(black_queen, white_horse, factor))


    def test_capture_piece_horse_bad(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_horse = pieces.Horse(True, 12, 8)

        self.assertEqual(31, score.capture_piece(black_queen, white_horse, factor))

    
    def test_capture_piece_bishop_good(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_bishop = pieces.Bishop(True, 9, 8)

        self.assertEqual(405, score.capture_piece(black_queen, white_bishop, factor))

    
    def test_capture_piece_bishop_bad(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_bishop = pieces.Bishop(True, 12, 8)

        self.assertEqual(41, score.capture_piece(black_queen, white_bishop, factor))

    
    def test_capture_piece_rook_good(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_rook = pieces.Rook(True, 9, 8)

        self.assertEqual(605, score.capture_piece(black_queen, white_rook, factor))

    
    def test_capture_piece_rook_bad(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_rook = pieces.Rook(True, 12, 8)

        self.assertEqual(61, score.capture_piece(black_queen, white_rook, factor))

    
    def test_capture_piece_queen_good(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_queen = pieces.Queen(True, 9, 8)

        self.assertEqual(805, score.capture_piece(black_queen, white_queen, factor))

    
    def test_capture_piece_queen_bad(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_queen = pieces.Queen(True, 12, 8)

        self.assertEqual(81, score.capture_piece(black_queen, white_queen, factor))

    
    def test_capture_piece_king_good(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_king = pieces.King(True, 9, 8)

        self.assertEqual(995, score.capture_piece(black_queen, white_king, factor))

    
    def test_capture_piece_king_bad(self):
        factor = 1
        black_queen = pieces.Queen(False, 8, 8)
        white_king = pieces.King(True, 12, 8)

        self.assertEqual(100, score.capture_piece(black_queen, white_king, factor))

    
    def test_set_score(self):
        score_new = score.Score()
        color = True
        white_queen = pieces.Queen(True, 8, 8)
        black_king = pieces.King(False, 0, 8)
        move = [{'from_row': 8, 'from_col': 8, 'to_row': 0, 'to_col': 8, 'score': 100.0}]

        score_new.set_score(white_queen, black_king, color)

        self.assertEqual(move, score_new.play_moves)
