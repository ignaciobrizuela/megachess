# Made by brz
import unittest
from scripts import score
from scripts import pieces


class TestScoreZones(unittest.TestCase):

    def test_zones_difference_pos(self):
        color = True
        piece  = pieces.Queen(True, 0, 0)
        piece_zone = score.get_zone(piece, color)
        element_in_square  = pieces.Queen(True, 8, 8)
        element_zone = score.get_zone(element_in_square, color)

        self.assertEqual(15, score.zone_difference(piece_zone, element_zone))

    def test_zones_difference_neg(self):
        color = True
        piece  = pieces.Queen(True, 9, 9)
        piece_zone = score.get_zone(piece, color)
        element_in_square  = pieces.Queen(True, 0, 15)
        element_zone = score.get_zone(element_in_square, color)

        self.assertEqual(-15, score.zone_difference(piece_zone, element_zone))

    def test_zones_difference_equal(self):
        color = True
        piece  = pieces.Queen(True, 9, 9)
        piece_zone = score.get_zone(piece, color)
        element_in_square  = pieces.Queen(True, 6, 9)
        element_zone = score.get_zone(element_in_square, color)

        self.assertEqual(20, score.zone_difference(piece_zone, element_zone))

    def test_get_zone_5_white_row0(self):
        piece1  = pieces.Queen(True, 0, 0)
        piece2  = pieces.Queen(True, 0, 1)
        piece3  = pieces.Queen(True, 0, 2)
        piece4  = pieces.Queen(True, 0, 3)
        piece5  = pieces.Queen(True, 0, 4)
        piece6  = pieces.Queen(True, 0, 5)
        piece7  = pieces.Queen(True, 0, 10)
        piece8  = pieces.Queen(True, 0, 11)
        piece9  = pieces.Queen(True, 0, 12)
        piece10 = pieces.Queen(True, 0, 13)
        piece11 = pieces.Queen(True, 0, 14)
        piece12 = pieces.Queen(True, 0, 15)
        color = True

        self.assertEqual(5, score.get_zone(piece1, color))
        self.assertEqual(5, score.get_zone(piece2, color))
        self.assertEqual(5, score.get_zone(piece3, color))
        self.assertEqual(5, score.get_zone(piece4, color))
        self.assertEqual(5, score.get_zone(piece5, color))
        self.assertEqual(5, score.get_zone(piece6, color))
        self.assertEqual(5, score.get_zone(piece7, color))
        self.assertEqual(5, score.get_zone(piece8, color))
        self.assertEqual(5, score.get_zone(piece9, color))
        self.assertEqual(5, score.get_zone(piece10, color))
        self.assertEqual(5, score.get_zone(piece11, color))
        self.assertEqual(5, score.get_zone(piece12, color))

    def test_get_zone_5_white_row1(self):
        piece1  = pieces.Queen(True, 1, 0)
        piece2  = pieces.Queen(True, 1, 1)
        piece3  = pieces.Queen(True, 1, 2)
        piece4  = pieces.Queen(True, 1, 3)
        piece5  = pieces.Queen(True, 1, 4)
        piece6  = pieces.Queen(True, 1, 5)
        piece7  = pieces.Queen(True, 1, 10)
        piece8  = pieces.Queen(True, 1, 11)
        piece9  = pieces.Queen(True, 1, 12)
        piece10 = pieces.Queen(True, 1, 13)
        piece11 = pieces.Queen(True, 1, 14)
        piece12 = pieces.Queen(True, 1, 15)
        color = True

        self.assertEqual(5, score.get_zone(piece1, color))
        self.assertEqual(5, score.get_zone(piece2, color))
        self.assertEqual(5, score.get_zone(piece3, color))
        self.assertEqual(5, score.get_zone(piece4, color))
        self.assertEqual(5, score.get_zone(piece5, color))
        self.assertEqual(5, score.get_zone(piece6, color))
        self.assertEqual(5, score.get_zone(piece7, color))
        self.assertEqual(5, score.get_zone(piece8, color))
        self.assertEqual(5, score.get_zone(piece9, color))
        self.assertEqual(5, score.get_zone(piece10, color))
        self.assertEqual(5, score.get_zone(piece11, color))
        self.assertEqual(5, score.get_zone(piece12, color))

    def test_get_zone_5_white_row2(self):
        piece1  = pieces.Queen(True, 2, 0)
        piece2  = pieces.Queen(True, 2, 1)
        piece3  = pieces.Queen(True, 2, 2)
        piece4  = pieces.Queen(True, 2, 3)
        piece5  = pieces.Queen(True, 2, 4)
        piece6  = pieces.Queen(True, 2, 5)
        piece7  = pieces.Queen(True, 2, 10)
        piece8  = pieces.Queen(True, 2, 11)
        piece9  = pieces.Queen(True, 2, 12)
        piece10 = pieces.Queen(True, 2, 13)
        piece11 = pieces.Queen(True, 2, 14)
        piece12 = pieces.Queen(True, 2, 15)
        color = True

        self.assertEqual(5, score.get_zone(piece1, color))
        self.assertEqual(5, score.get_zone(piece2, color))
        self.assertEqual(5, score.get_zone(piece3, color))
        self.assertEqual(5, score.get_zone(piece4, color))
        self.assertEqual(5, score.get_zone(piece5, color))
        self.assertEqual(5, score.get_zone(piece6, color))
        self.assertEqual(5, score.get_zone(piece7, color))
        self.assertEqual(5, score.get_zone(piece8, color))
        self.assertEqual(5, score.get_zone(piece9, color))
        self.assertEqual(5, score.get_zone(piece10, color))
        self.assertEqual(5, score.get_zone(piece11, color))
        self.assertEqual(5, score.get_zone(piece12, color))

    def test_get_zone_5_white_row3(self):
        piece1  = pieces.Queen(True, 3, 0)
        piece2  = pieces.Queen(True, 3, 1)
        piece3  = pieces.Queen(True, 3, 2)
        piece4  = pieces.Queen(True, 3, 3)
        piece5  = pieces.Queen(True, 3, 4)
        piece6  = pieces.Queen(True, 3, 5)
        piece7  = pieces.Queen(True, 3, 10)
        piece8  = pieces.Queen(True, 3, 11)
        piece9  = pieces.Queen(True, 3, 12)
        piece10 = pieces.Queen(True, 3, 13)
        piece11 = pieces.Queen(True, 3, 14)
        piece12 = pieces.Queen(True, 3, 15)
        color = True

        self.assertEqual(5, score.get_zone(piece1, color))
        self.assertEqual(5, score.get_zone(piece2, color))
        self.assertEqual(5, score.get_zone(piece3, color))
        self.assertEqual(5, score.get_zone(piece4, color))
        self.assertEqual(5, score.get_zone(piece5, color))
        self.assertEqual(5, score.get_zone(piece6, color))
        self.assertEqual(5, score.get_zone(piece7, color))
        self.assertEqual(5, score.get_zone(piece8, color))
        self.assertEqual(5, score.get_zone(piece9, color))
        self.assertEqual(5, score.get_zone(piece10, color))
        self.assertEqual(5, score.get_zone(piece11, color))
        self.assertEqual(5, score.get_zone(piece12, color))

    def test_get_zone_5_white_row4(self):
        piece1  = pieces.Queen(True, 4, 0)
        piece2  = pieces.Queen(True, 4, 1)
        piece3  = pieces.Queen(True, 4, 2)
        piece4  = pieces.Queen(True, 4, 3)
        piece5  = pieces.Queen(True, 4, 4)
        piece6  = pieces.Queen(True, 4, 5)
        piece7  = pieces.Queen(True, 4, 10)
        piece8  = pieces.Queen(True, 4, 11)
        piece9  = pieces.Queen(True, 4, 12)
        piece10 = pieces.Queen(True, 4, 13)
        piece11 = pieces.Queen(True, 4, 14)
        piece12 = pieces.Queen(True, 4, 15)
        color = True

        self.assertEqual(5, score.get_zone(piece1, color))
        self.assertEqual(5, score.get_zone(piece2, color))
        self.assertEqual(5, score.get_zone(piece3, color))
        self.assertEqual(5, score.get_zone(piece4, color))
        self.assertEqual(5, score.get_zone(piece5, color))
        self.assertEqual(5, score.get_zone(piece6, color))
        self.assertEqual(5, score.get_zone(piece7, color))
        self.assertEqual(5, score.get_zone(piece8, color))
        self.assertEqual(5, score.get_zone(piece9, color))
        self.assertEqual(5, score.get_zone(piece10, color))
        self.assertEqual(5, score.get_zone(piece11, color))
        self.assertEqual(5, score.get_zone(piece12, color))

    def test_get_zone_5_white_row5(self):
        piece1  = pieces.Queen(True, 5, 0)
        piece2  = pieces.Queen(True, 5, 1)
        piece3  = pieces.Queen(True, 5, 2)
        piece4  = pieces.Queen(True, 5, 3)
        piece5  = pieces.Queen(True, 5, 4)
        piece6  = pieces.Queen(True, 5, 5)
        piece7  = pieces.Queen(True, 5, 10)
        piece8  = pieces.Queen(True, 5, 11)
        piece9  = pieces.Queen(True, 5, 12)
        piece10 = pieces.Queen(True, 5, 13)
        piece11 = pieces.Queen(True, 5, 14)
        piece12 = pieces.Queen(True, 5, 15)
        color = True

        self.assertEqual(5, score.get_zone(piece1, color))
        self.assertEqual(5, score.get_zone(piece2, color))
        self.assertEqual(5, score.get_zone(piece3, color))
        self.assertEqual(5, score.get_zone(piece4, color))
        self.assertEqual(5, score.get_zone(piece5, color))
        self.assertEqual(5, score.get_zone(piece6, color))
        self.assertEqual(5, score.get_zone(piece7, color))
        self.assertEqual(5, score.get_zone(piece8, color))
        self.assertEqual(5, score.get_zone(piece9, color))
        self.assertEqual(5, score.get_zone(piece10, color))
        self.assertEqual(5, score.get_zone(piece11, color))
        self.assertEqual(5, score.get_zone(piece12, color))

    def test_get_zone_6_white_row0(self):
        piece1  = pieces.Queen(True, 0, 6)
        piece2  = pieces.Queen(True, 0, 7)
        piece3  = pieces.Queen(True, 0, 8)
        piece4  = pieces.Queen(True, 0, 9)

        color = True

        self.assertEqual(6, score.get_zone(piece1, color))
        self.assertEqual(6, score.get_zone(piece2, color))
        self.assertEqual(6, score.get_zone(piece3, color))
        self.assertEqual(6, score.get_zone(piece4, color))

    def test_get_zone_6_white_row1(self):
        piece1  = pieces.Queen(True, 1, 6)
        piece2  = pieces.Queen(True, 1, 7)
        piece3  = pieces.Queen(True, 1, 8)
        piece4  = pieces.Queen(True, 1, 9)

        color = True

        self.assertEqual(6, score.get_zone(piece1, color))
        self.assertEqual(6, score.get_zone(piece2, color))
        self.assertEqual(6, score.get_zone(piece3, color))
        self.assertEqual(6, score.get_zone(piece4, color))

    def test_get_zone_6_white_row2(self):
        piece1  = pieces.Queen(True, 2, 6)
        piece2  = pieces.Queen(True, 2, 7)
        piece3  = pieces.Queen(True, 2, 8)
        piece4  = pieces.Queen(True, 2, 9)

        color = True

        self.assertEqual(6, score.get_zone(piece1, color))
        self.assertEqual(6, score.get_zone(piece2, color))
        self.assertEqual(6, score.get_zone(piece3, color))
        self.assertEqual(6, score.get_zone(piece4, color))

    def test_get_zone_6_white_row3(self):
        piece1  = pieces.Queen(True, 3, 6)
        piece2  = pieces.Queen(True, 3, 7)
        piece3  = pieces.Queen(True, 3, 8)
        piece4  = pieces.Queen(True, 3, 9)

        color = True

        self.assertEqual(6, score.get_zone(piece1, color))
        self.assertEqual(6, score.get_zone(piece2, color))
        self.assertEqual(6, score.get_zone(piece3, color))
        self.assertEqual(6, score.get_zone(piece4, color))

    def test_get_zone_6_white_row4(self):
        piece1  = pieces.Queen(True, 4, 6)
        piece2  = pieces.Queen(True, 4, 7)
        piece3  = pieces.Queen(True, 4, 8)
        piece4  = pieces.Queen(True, 4, 9)

        color = True

        self.assertEqual(6, score.get_zone(piece1, color))
        self.assertEqual(6, score.get_zone(piece2, color))
        self.assertEqual(6, score.get_zone(piece3, color))
        self.assertEqual(6, score.get_zone(piece4, color))

    def test_get_zone_6_white_row5(self):
        piece1  = pieces.Queen(True, 5, 6)
        piece2  = pieces.Queen(True, 5, 7)
        piece3  = pieces.Queen(True, 5, 8)
        piece4  = pieces.Queen(True, 5, 9)

        color = True

        self.assertEqual(6, score.get_zone(piece1, color))
        self.assertEqual(6, score.get_zone(piece2, color))
        self.assertEqual(6, score.get_zone(piece3, color))
        self.assertEqual(6, score.get_zone(piece4, color))

    def test_get_zone_7_white_row6(self):
        piece1  = pieces.Queen(True, 6, 0)
        piece2  = pieces.Queen(True, 6, 1)
        piece3  = pieces.Queen(True, 6, 2)
        piece4  = pieces.Queen(True, 6, 3)
        piece5  = pieces.Queen(True, 6, 4)
        piece6  = pieces.Queen(True, 6, 5)
        piece7  = pieces.Queen(True, 6, 10)
        piece8  = pieces.Queen(True, 6, 11)
        piece9  = pieces.Queen(True, 6, 12)
        piece10 = pieces.Queen(True, 6, 13)
        piece11 = pieces.Queen(True, 6, 14)
        piece12 = pieces.Queen(True, 6, 15)
        color = True

        self.assertEqual(7, score.get_zone(piece1, color))
        self.assertEqual(7, score.get_zone(piece2, color))
        self.assertEqual(7, score.get_zone(piece3, color))
        self.assertEqual(7, score.get_zone(piece4, color))
        self.assertEqual(7, score.get_zone(piece5, color))
        self.assertEqual(7, score.get_zone(piece6, color))
        self.assertEqual(7, score.get_zone(piece7, color))
        self.assertEqual(7, score.get_zone(piece8, color))
        self.assertEqual(7, score.get_zone(piece9, color))
        self.assertEqual(7, score.get_zone(piece10, color))
        self.assertEqual(7, score.get_zone(piece11, color))
        self.assertEqual(7, score.get_zone(piece12, color))

    def test_get_zone_7_white_row7(self):
        piece1  = pieces.Queen(True, 7, 0)
        piece2  = pieces.Queen(True, 7, 1)
        piece3  = pieces.Queen(True, 7, 2)
        piece4  = pieces.Queen(True, 7, 3)
        piece5  = pieces.Queen(True, 7, 4)
        piece6  = pieces.Queen(True, 7, 5)
        piece7  = pieces.Queen(True, 7, 10)
        piece8  = pieces.Queen(True, 7, 11)
        piece9  = pieces.Queen(True, 7, 12)
        piece10 = pieces.Queen(True, 7, 13)
        piece11 = pieces.Queen(True, 7, 14)
        piece12 = pieces.Queen(True, 7, 15)
        color = True

        self.assertEqual(7, score.get_zone(piece1, color))
        self.assertEqual(7, score.get_zone(piece2, color))
        self.assertEqual(7, score.get_zone(piece3, color))
        self.assertEqual(7, score.get_zone(piece4, color))
        self.assertEqual(7, score.get_zone(piece5, color))
        self.assertEqual(7, score.get_zone(piece6, color))
        self.assertEqual(7, score.get_zone(piece7, color))
        self.assertEqual(7, score.get_zone(piece8, color))
        self.assertEqual(7, score.get_zone(piece9, color))
        self.assertEqual(7, score.get_zone(piece10, color))
        self.assertEqual(7, score.get_zone(piece11, color))
        self.assertEqual(7, score.get_zone(piece12, color))

    def test_get_zone_7_white_row7(self):
        piece1  = pieces.Queen(True, 7, 0)
        piece2  = pieces.Queen(True, 7, 1)
        piece3  = pieces.Queen(True, 7, 2)
        piece4  = pieces.Queen(True, 7, 3)
        piece5  = pieces.Queen(True, 7, 4)
        piece6  = pieces.Queen(True, 7, 5)
        piece7  = pieces.Queen(True, 7, 10)
        piece8  = pieces.Queen(True, 7, 11)
        piece9  = pieces.Queen(True, 7, 12)
        piece10 = pieces.Queen(True, 7, 13)
        piece11 = pieces.Queen(True, 7, 14)
        piece12 = pieces.Queen(True, 7, 15)
        color = True

        self.assertEqual(7, score.get_zone(piece1, color))
        self.assertEqual(7, score.get_zone(piece2, color))
        self.assertEqual(7, score.get_zone(piece3, color))
        self.assertEqual(7, score.get_zone(piece4, color))
        self.assertEqual(7, score.get_zone(piece5, color))
        self.assertEqual(7, score.get_zone(piece6, color))
        self.assertEqual(7, score.get_zone(piece7, color))
        self.assertEqual(7, score.get_zone(piece8, color))
        self.assertEqual(7, score.get_zone(piece9, color))
        self.assertEqual(7, score.get_zone(piece10, color))
        self.assertEqual(7, score.get_zone(piece11, color))
        self.assertEqual(7, score.get_zone(piece12, color))

    def test_get_zone_7_white_row8(self):
        piece1  = pieces.Queen(True, 8, 0)
        piece2  = pieces.Queen(True, 8, 1)
        piece3  = pieces.Queen(True, 8, 2)
        piece4  = pieces.Queen(True, 8, 3)
        piece5  = pieces.Queen(True, 8, 4)
        piece6  = pieces.Queen(True, 8, 5)
        piece7  = pieces.Queen(True, 8, 10)
        piece8  = pieces.Queen(True, 8, 11)
        piece9  = pieces.Queen(True, 8, 12)
        piece10 = pieces.Queen(True, 8, 13)
        piece11 = pieces.Queen(True, 8, 14)
        piece12 = pieces.Queen(True, 8, 15)
        color = True

        self.assertEqual(7, score.get_zone(piece1, color))
        self.assertEqual(7, score.get_zone(piece2, color))
        self.assertEqual(7, score.get_zone(piece3, color))
        self.assertEqual(7, score.get_zone(piece4, color))
        self.assertEqual(7, score.get_zone(piece5, color))
        self.assertEqual(7, score.get_zone(piece6, color))
        self.assertEqual(7, score.get_zone(piece7, color))
        self.assertEqual(7, score.get_zone(piece8, color))
        self.assertEqual(7, score.get_zone(piece9, color))
        self.assertEqual(7, score.get_zone(piece10, color))
        self.assertEqual(7, score.get_zone(piece11, color))
        self.assertEqual(7, score.get_zone(piece12, color))

    def test_get_zone_7_white_row9(self):
        piece1  = pieces.Queen(True, 9, 0)
        piece2  = pieces.Queen(True, 9, 1)
        piece3  = pieces.Queen(True, 9, 2)
        piece4  = pieces.Queen(True, 9, 3)
        piece5  = pieces.Queen(True, 9, 4)
        piece6  = pieces.Queen(True, 9, 5)
        piece7  = pieces.Queen(True, 9, 10)
        piece8  = pieces.Queen(True, 9, 11)
        piece9  = pieces.Queen(True, 9, 12)
        piece10 = pieces.Queen(True, 9, 13)
        piece11 = pieces.Queen(True, 9, 14)
        piece12 = pieces.Queen(True, 9, 15)
        color = True

        self.assertEqual(7, score.get_zone(piece1, color))
        self.assertEqual(7, score.get_zone(piece2, color))
        self.assertEqual(7, score.get_zone(piece3, color))
        self.assertEqual(7, score.get_zone(piece4, color))
        self.assertEqual(7, score.get_zone(piece5, color))
        self.assertEqual(7, score.get_zone(piece6, color))
        self.assertEqual(7, score.get_zone(piece7, color))
        self.assertEqual(7, score.get_zone(piece8, color))
        self.assertEqual(7, score.get_zone(piece9, color))
        self.assertEqual(7, score.get_zone(piece10, color))
        self.assertEqual(7, score.get_zone(piece11, color))
        self.assertEqual(7, score.get_zone(piece12, color))

    def test_get_zone_8_white_row10(self):
        piece1  = pieces.Queen(True, 10, 0)
        piece2  = pieces.Queen(True, 10, 1)
        piece3  = pieces.Queen(True, 10, 2)
        piece4  = pieces.Queen(True, 10, 3)
        piece5  = pieces.Queen(True, 10, 4)
        piece6  = pieces.Queen(True, 10, 5)
        piece7  = pieces.Queen(True, 10, 10)
        piece8  = pieces.Queen(True, 10, 11)
        piece9  = pieces.Queen(True, 10, 12)
        piece10 = pieces.Queen(True, 10, 13)
        piece11 = pieces.Queen(True, 10, 14)
        piece12 = pieces.Queen(True, 10, 15)
        color = True

        self.assertEqual(8, score.get_zone(piece1, color))
        self.assertEqual(8, score.get_zone(piece2, color))
        self.assertEqual(8, score.get_zone(piece3, color))
        self.assertEqual(8, score.get_zone(piece4, color))
        self.assertEqual(8, score.get_zone(piece5, color))
        self.assertEqual(8, score.get_zone(piece6, color))
        self.assertEqual(8, score.get_zone(piece7, color))
        self.assertEqual(8, score.get_zone(piece8, color))
        self.assertEqual(8, score.get_zone(piece9, color))
        self.assertEqual(8, score.get_zone(piece10, color))
        self.assertEqual(8, score.get_zone(piece11, color))
        self.assertEqual(8, score.get_zone(piece12, color))

    def test_get_zone_8_white_row11(self):
        piece1  = pieces.Queen(True, 11, 0)
        piece2  = pieces.Queen(True, 11, 1)
        piece3  = pieces.Queen(True, 11, 2)
        piece4  = pieces.Queen(True, 11, 3)
        piece5  = pieces.Queen(True, 11, 4)
        piece6  = pieces.Queen(True, 11, 5)
        piece7  = pieces.Queen(True, 11, 10)
        piece8  = pieces.Queen(True, 11, 11)
        piece9  = pieces.Queen(True, 11, 12)
        piece10 = pieces.Queen(True, 11, 13)
        piece11 = pieces.Queen(True, 11, 14)
        piece12 = pieces.Queen(True, 11, 15)
        color = True

        self.assertEqual(8, score.get_zone(piece1, color))
        self.assertEqual(8, score.get_zone(piece2, color))
        self.assertEqual(8, score.get_zone(piece3, color))
        self.assertEqual(8, score.get_zone(piece4, color))
        self.assertEqual(8, score.get_zone(piece5, color))
        self.assertEqual(8, score.get_zone(piece6, color))
        self.assertEqual(8, score.get_zone(piece7, color))
        self.assertEqual(8, score.get_zone(piece8, color))
        self.assertEqual(8, score.get_zone(piece9, color))
        self.assertEqual(8, score.get_zone(piece10, color))
        self.assertEqual(8, score.get_zone(piece11, color))
        self.assertEqual(8, score.get_zone(piece12, color))

    def test_get_zone_8_white_row12(self):
        piece1  = pieces.Queen(True, 12, 0)
        piece2  = pieces.Queen(True, 12, 1)
        piece3  = pieces.Queen(True, 12, 2)
        piece4  = pieces.Queen(True, 12, 3)
        piece5  = pieces.Queen(True, 12, 4)
        piece6  = pieces.Queen(True, 12, 5)
        piece7  = pieces.Queen(True, 12, 10)
        piece8  = pieces.Queen(True, 12, 11)
        piece9  = pieces.Queen(True, 12, 12)
        piece10 = pieces.Queen(True, 12, 13)
        piece11 = pieces.Queen(True, 12, 14)
        piece12 = pieces.Queen(True, 12, 15)
        color = True

        self.assertEqual(8, score.get_zone(piece1, color))
        self.assertEqual(8, score.get_zone(piece2, color))
        self.assertEqual(8, score.get_zone(piece3, color))
        self.assertEqual(8, score.get_zone(piece4, color))
        self.assertEqual(8, score.get_zone(piece5, color))
        self.assertEqual(8, score.get_zone(piece6, color))
        self.assertEqual(8, score.get_zone(piece7, color))
        self.assertEqual(8, score.get_zone(piece8, color))
        self.assertEqual(8, score.get_zone(piece9, color))
        self.assertEqual(8, score.get_zone(piece10, color))
        self.assertEqual(8, score.get_zone(piece11, color))
        self.assertEqual(8, score.get_zone(piece12, color))

    def test_get_zone_8_white_row13(self):
        piece1  = pieces.Queen(True, 13, 0)
        piece2  = pieces.Queen(True, 13, 1)
        piece3  = pieces.Queen(True, 13, 2)
        piece4  = pieces.Queen(True, 13, 3)
        piece5  = pieces.Queen(True, 13, 4)
        piece6  = pieces.Queen(True, 13, 5)
        piece7  = pieces.Queen(True, 13, 10)
        piece8  = pieces.Queen(True, 13, 11)
        piece9  = pieces.Queen(True, 13, 12)
        piece10 = pieces.Queen(True, 13, 13)
        piece11 = pieces.Queen(True, 13, 14)
        piece12 = pieces.Queen(True, 13, 15)
        color = True

        self.assertEqual(8, score.get_zone(piece1, color))
        self.assertEqual(8, score.get_zone(piece2, color))
        self.assertEqual(8, score.get_zone(piece3, color))
        self.assertEqual(8, score.get_zone(piece4, color))
        self.assertEqual(8, score.get_zone(piece5, color))
        self.assertEqual(8, score.get_zone(piece6, color))
        self.assertEqual(8, score.get_zone(piece7, color))
        self.assertEqual(8, score.get_zone(piece8, color))
        self.assertEqual(8, score.get_zone(piece9, color))
        self.assertEqual(8, score.get_zone(piece10, color))
        self.assertEqual(8, score.get_zone(piece11, color))
        self.assertEqual(8, score.get_zone(piece12, color))

    def test_get_zone_8_white_row14(self):
        piece1  = pieces.Queen(True, 14, 0)
        piece2  = pieces.Queen(True, 14, 1)
        piece3  = pieces.Queen(True, 14, 2)
        piece4  = pieces.Queen(True, 14, 3)
        piece5  = pieces.Queen(True, 14, 4)
        piece6  = pieces.Queen(True, 14, 5)
        piece7  = pieces.Queen(True, 14, 10)
        piece8  = pieces.Queen(True, 14, 11)
        piece9  = pieces.Queen(True, 14, 12)
        piece10 = pieces.Queen(True, 14, 13)
        piece11 = pieces.Queen(True, 14, 14)
        piece12 = pieces.Queen(True, 14, 15)
        color = True

        self.assertEqual(8, score.get_zone(piece1, color))
        self.assertEqual(8, score.get_zone(piece2, color))
        self.assertEqual(8, score.get_zone(piece3, color))
        self.assertEqual(8, score.get_zone(piece4, color))
        self.assertEqual(8, score.get_zone(piece5, color))
        self.assertEqual(8, score.get_zone(piece6, color))
        self.assertEqual(8, score.get_zone(piece7, color))
        self.assertEqual(8, score.get_zone(piece8, color))
        self.assertEqual(8, score.get_zone(piece9, color))
        self.assertEqual(8, score.get_zone(piece10, color))
        self.assertEqual(8, score.get_zone(piece11, color))
        self.assertEqual(8, score.get_zone(piece12, color))

    def test_get_zone_8_white_row15(self):
        piece1  = pieces.Queen(True, 15, 0)
        piece2  = pieces.Queen(True, 15, 1)
        piece3  = pieces.Queen(True, 15, 2)
        piece4  = pieces.Queen(True, 15, 3)
        piece5  = pieces.Queen(True, 15, 4)
        piece6  = pieces.Queen(True, 15, 5)
        piece7  = pieces.Queen(True, 15, 10)
        piece8  = pieces.Queen(True, 15, 11)
        piece9  = pieces.Queen(True, 15, 12)
        piece10 = pieces.Queen(True, 15, 13)
        piece11 = pieces.Queen(True, 15, 14)
        piece12 = pieces.Queen(True, 15, 15)
        color = True

        self.assertEqual(8, score.get_zone(piece1, color))
        self.assertEqual(8, score.get_zone(piece2, color))
        self.assertEqual(8, score.get_zone(piece3, color))
        self.assertEqual(8, score.get_zone(piece4, color))
        self.assertEqual(8, score.get_zone(piece5, color))
        self.assertEqual(8, score.get_zone(piece6, color))
        self.assertEqual(8, score.get_zone(piece7, color))
        self.assertEqual(8, score.get_zone(piece8, color))
        self.assertEqual(8, score.get_zone(piece9, color))
        self.assertEqual(8, score.get_zone(piece10, color))
        self.assertEqual(8, score.get_zone(piece11, color))
        self.assertEqual(8, score.get_zone(piece12, color))

    def test_get_zone_9_white_row10(self):
        piece1  = pieces.Queen(True, 10, 6)
        piece2  = pieces.Queen(True, 10, 7)
        piece3  = pieces.Queen(True, 10, 8)
        piece4  = pieces.Queen(True, 10, 9)

        color = True

        self.assertEqual(9, score.get_zone(piece1, color))
        self.assertEqual(9, score.get_zone(piece2, color))
        self.assertEqual(9, score.get_zone(piece3, color))
        self.assertEqual(9, score.get_zone(piece4, color))

    def test_get_zone_9_white_row11(self):
        piece1  = pieces.Queen(True, 11, 6)
        piece2  = pieces.Queen(True, 11, 7)
        piece3  = pieces.Queen(True, 11, 8)
        piece4  = pieces.Queen(True, 11, 9)

        color = True

        self.assertEqual(9, score.get_zone(piece1, color))
        self.assertEqual(9, score.get_zone(piece2, color))
        self.assertEqual(9, score.get_zone(piece3, color))
        self.assertEqual(9, score.get_zone(piece4, color))

    def test_get_zone_9_white_row12(self):
        piece1  = pieces.Queen(True, 12, 6)
        piece2  = pieces.Queen(True, 12, 7)
        piece3  = pieces.Queen(True, 12, 8)
        piece4  = pieces.Queen(True, 12, 9)

        color = True

        self.assertEqual(9, score.get_zone(piece1, color))
        self.assertEqual(9, score.get_zone(piece2, color))
        self.assertEqual(9, score.get_zone(piece3, color))
        self.assertEqual(9, score.get_zone(piece4, color))

    def test_get_zone_9_white_row13(self):
        piece1  = pieces.Queen(True, 13, 6)
        piece2  = pieces.Queen(True, 13, 7)
        piece3  = pieces.Queen(True, 13, 8)
        piece4  = pieces.Queen(True, 13, 9)

        color = True

        self.assertEqual(9, score.get_zone(piece1, color))
        self.assertEqual(9, score.get_zone(piece2, color))
        self.assertEqual(9, score.get_zone(piece3, color))
        self.assertEqual(9, score.get_zone(piece4, color))

    def test_get_zone_9_white_row14(self):
        piece1  = pieces.Queen(True, 14, 6)
        piece2  = pieces.Queen(True, 14, 7)
        piece3  = pieces.Queen(True, 14, 8)
        piece4  = pieces.Queen(True, 14, 9)

        color = True

        self.assertEqual(9, score.get_zone(piece1, color))
        self.assertEqual(9, score.get_zone(piece2, color))
        self.assertEqual(9, score.get_zone(piece3, color))
        self.assertEqual(9, score.get_zone(piece4, color))

    def test_get_zone_9_white_row15(self):
        piece1  = pieces.Queen(True, 15, 6)
        piece2  = pieces.Queen(True, 15, 7)
        piece3  = pieces.Queen(True, 15, 8)
        piece4  = pieces.Queen(True, 15, 9)

        color = True

        self.assertEqual(9, score.get_zone(piece1, color))
        self.assertEqual(9, score.get_zone(piece2, color))
        self.assertEqual(9, score.get_zone(piece3, color))
        self.assertEqual(9, score.get_zone(piece4, color))

    def test_get_zone_10_white_row6(self):
        piece1  = pieces.Queen(True, 6, 6)
        piece2  = pieces.Queen(True, 6, 7)
        piece3  = pieces.Queen(True, 6, 8)
        piece4  = pieces.Queen(True, 6, 9)

        color = True

        self.assertEqual(10, score.get_zone(piece1, color))
        self.assertEqual(10, score.get_zone(piece2, color))
        self.assertEqual(10, score.get_zone(piece3, color))
        self.assertEqual(10, score.get_zone(piece4, color))

    def test_get_zone_10_white_row7(self):
        piece1  = pieces.Queen(True, 7, 6)
        piece2  = pieces.Queen(True, 7, 7)
        piece3  = pieces.Queen(True, 7, 8)
        piece4  = pieces.Queen(True, 7, 9)

        color = True

        self.assertEqual(10, score.get_zone(piece1, color))
        self.assertEqual(10, score.get_zone(piece2, color))
        self.assertEqual(10, score.get_zone(piece3, color))
        self.assertEqual(10, score.get_zone(piece4, color))

    def test_get_zone_10_white_row8(self):
        piece1  = pieces.Queen(True, 8, 6)
        piece2  = pieces.Queen(True, 8, 7)
        piece3  = pieces.Queen(True, 8, 8)
        piece4  = pieces.Queen(True, 8, 9)

        color = True

        self.assertEqual(10, score.get_zone(piece1, color))
        self.assertEqual(10, score.get_zone(piece2, color))
        self.assertEqual(10, score.get_zone(piece3, color))
        self.assertEqual(10, score.get_zone(piece4, color))

    def test_get_zone_10_white_row9(self):
        piece1  = pieces.Queen(True, 9, 6)
        piece2  = pieces.Queen(True, 9, 7)
        piece3  = pieces.Queen(True, 9, 8)
        piece4  = pieces.Queen(True, 9, 9)

        color = True

        self.assertEqual(10, score.get_zone(piece1, color))
        self.assertEqual(10, score.get_zone(piece2, color))
        self.assertEqual(10, score.get_zone(piece3, color))
        self.assertEqual(10, score.get_zone(piece4, color))