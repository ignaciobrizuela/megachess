# Made by brz
import unittest
from scripts import score
from scripts import pieces


class TestScorePlus(unittest.TestCase):

    def test_get_plus_pawn_double(self):
        pawn1 = pieces.Pawn(True, 12, 5)
        pawn2 = pieces.Pawn(True, 13, 5)
        pawn3 = pieces.Pawn(True, 12, 2)
        pawn4 = pieces.Pawn(True, 12, 13)
        pawn5 = pieces.Pawn(True, 13, 2)
        pawn6 = pieces.Pawn(True, 13, 13)
        pawn7 = pieces.Pawn(True, 12, 8)
        pawn8 = pieces.Pawn(True, 13, 8)
        square1 = pieces.EmptySquare(10, 5)
        square2 = pieces.EmptySquare(11, 5)
        square3 = pieces.EmptySquare(10, 2)
        square4 = pieces.EmptySquare(10, 13)
        square5 = pieces.EmptySquare(11, 2)
        square6 = pieces.EmptySquare(11, 13)
        square7 = pieces.EmptySquare(10, 6)
        square8 = pieces.EmptySquare(11, 6)

        self.assertEqual(62.5, score.get_pawn_plus(pawn1, square1))
        self.assertEqual(61.5, score.get_pawn_plus(pawn2, square2))
        self.assertEqual(59.5, score.get_pawn_plus(pawn3, square3))
        self.assertEqual(59.5, score.get_pawn_plus(pawn4, square4))
        self.assertEqual(58.5, score.get_pawn_plus(pawn5, square5))
        self.assertEqual(58.5, score.get_pawn_plus(pawn6, square6))
        self.assertEqual(57.5, score.get_pawn_plus(pawn7, square7))
        self.assertEqual(56.5, score.get_pawn_plus(pawn8, square8))

    def test_get_plus_pawn_simple(self):
        pawn1 = pieces.Pawn(True, 12, 5)
        pawn2 = pieces.Pawn(True, 13, 5)
        pawn3 = pieces.Pawn(True, 12, 2)
        pawn4 = pieces.Pawn(True, 12, 13)
        pawn5 = pieces.Pawn(True, 13, 2)
        pawn6 = pieces.Pawn(True, 13, 13)
        pawn7 = pieces.Pawn(True, 12, 8)
        pawn8 = pieces.Pawn(True, 13, 8)
        square1 = pieces.EmptySquare(11, 5)
        square2 = pieces.EmptySquare(12, 5)
        square3 = pieces.EmptySquare(11, 2)
        square4 = pieces.EmptySquare(11, 13)
        square5 = pieces.EmptySquare(12, 2)
        square6 = pieces.EmptySquare(12, 13)
        square7 = pieces.EmptySquare(11, 6)
        square8 = pieces.EmptySquare(12, 6)

        self.assertEqual(61.5, score.get_pawn_plus(pawn1, square1))
        self.assertEqual(60.5, score.get_pawn_plus(pawn2, square2))
        self.assertEqual(58.5, score.get_pawn_plus(pawn3, square3))
        self.assertEqual(58.5, score.get_pawn_plus(pawn4, square4))
        self.assertEqual(57.5, score.get_pawn_plus(pawn5, square5))
        self.assertEqual(57.5, score.get_pawn_plus(pawn6, square6))
        self.assertEqual(56.5, score.get_pawn_plus(pawn7, square7))
        self.assertEqual(55.5, score.get_pawn_plus(pawn8, square8))


    def test_get_plus_pawn_advance(self):
        pawn1 = pieces.Pawn(True, 12, 5)
        pawn2 = pieces.Pawn(True, 10, 5)
        pawn3 = pieces.Pawn(True, 9, 5)

        square1 = pieces.EmptySquare(10, 5)
        square2 = pieces.EmptySquare(9, 5)
        square3 = pieces.EmptySquare(8, 5)

        self.assertEqual(62.5, score.get_pawn_plus(pawn1, square1))
        self.assertEqual(68.5, score.get_pawn_plus(pawn2, square2))
        self.assertEqual(69.5, score.get_pawn_plus(pawn3, square3))

    def test_queen_plus(self):
        queen = pieces.Queen(True, 12, 5)
        square1 = pieces.EmptySquare(7, 5)
        square2 = pieces.EmptySquare(3, 5)

        self.assertEqual(500, score.get_queen_plus(queen, square1))
        self.assertEqual(0, score.get_queen_plus(queen, square2))