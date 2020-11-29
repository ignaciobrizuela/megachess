# Made by brz
from scripts import pieces

class Score():
    def __init__(self):
        self.play_moves = []

    def set_score(self, piece, element_in_square, color):
        factor = 1 if piece.color == color else -1
        
        if isinstance(element_in_square, pieces.EmptySquare):
            points = piece.points 
            score = points * factor
        else:
            score = element_in_square.points * 10 * factor

        play = {'from_row': piece.row, 
                'from_col': piece.col,
                'to_row': element_in_square.row,
                'to_col': element_in_square.col,
                'score': score}
        self.play_moves.append(play)

    def get_score(self):
        return self.play_moves


    def clear_score(self):
        self.play_moves = []