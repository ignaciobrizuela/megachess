# Made by brz
from scripts import pieces

class Score():
    def __init__(self):
        self.play_moves = []

    def set_score(self, piece, element_in_square, color):
        factor = 1 if piece.color == color else -1
        score = 0
        
        if isinstance(element_in_square, pieces.EmptySquare):
            if isinstance(piece, pieces.Pawn):
                if (piece.row == 3 or 12) and 5 <= piece.col <= 9:
                    plus = plus = round(1 / abs(7.5 - element_in_square.row), 2) + 2
                elif (piece.row == 2 or 13) and 5 <= piece.col <= 7:
                    plus = round(1 / abs(7.5 - element_in_square.row), 2) + 1
                else:
                    plus = round(1 / abs(7.5 - element_in_square.row), 2)
                score = (60 + plus) * factor 
            else:
                score = piece.point_move  * factor

        elif piece.color == False and element_in_square.color == True:
            if element_in_square.row < 11:
                score = element_in_square.point_been_captured * factor
            else:
                score = element_in_square.point_been_captured / 10 * factor

        elif piece.color == True and element_in_square.color == False:
            if element_in_square.row > 4:
                score = element_in_square.point_been_captured * factor
            else:
                score = element_in_square.point_been_captured / 10 * factor

        play = {'from_row': piece.row, 
                'from_col': piece.col,
                'to_row': element_in_square.row,
                'to_col': element_in_square.col,
                'score': score}
                
        if play['score'] != 0:
            self.play_moves.append(play)