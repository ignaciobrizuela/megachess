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
                score = jump_pawn(piece, element_in_square, factor)
            else:
                score = jump_piece(piece, factor)
            
        else:
            score = capture_piece(piece, element_in_square, factor)

        play = {'from_row': piece.row, 
                'from_col': piece.col,
                'to_row': element_in_square.row,
                'to_col': element_in_square.col,
                'score': score}
                
        if play['score'] != 0:
            self.play_moves.append(play)


def jump_pawn(piece, element_in_square, factor):
    if (piece.row == 3 or piece.row == 12) and (5 <= piece.col <= 9):
        plus = plus = round(1 / abs(7.5 - element_in_square.row), 2) + 2
    elif (piece.row == 2 or piece.row == 13) and (5 <= piece.col <= 7):
        plus = round(1 / abs(7.5 - element_in_square.row), 2) + 1
    elif 5 <= piece.col <= 9:
        plus = round(1 / abs(7.5 - element_in_square.row), 2) + 2
    else:
        plus = round(1 / abs(7.5 - element_in_square.row), 2)
    score = (60 + plus) * factor 

    return score


def jump_piece(piece, factor):
    return piece.point_move  * factor


def capture_piece(piece, element_in_square, factor):
    if (piece.color == False) and (element_in_square.color == True):
        if element_in_square.row < 11:
            score = element_in_square.point_been_captured * factor + protect_center(piece, element_in_square)
        else:
            score = element_in_square.point_been_captured / 10 * factor + protect_center(piece, element_in_square)

    elif (piece.color == True) and (element_in_square.color == False):
        if element_in_square.row > 4:
            score = element_in_square.point_been_captured * factor + protect_center(piece, element_in_square)
        else:
            score = element_in_square.point_been_captured / 10 * factor + protect_center(piece, element_in_square)

    return score


def protect_center(piece, element_in_square):
    if (6 <= element_in_square.row <= 9) and (5 <= element_in_square.col <= 10):
        if (6 <= piece.row <= 9) and (5 <= piece.col <= 10):
            return 5
        else:
            return 10
    else:
        if (6 <= piece.row <= 9) and (5 <= piece.col <= 10):
            return 1
        else:
            return 3