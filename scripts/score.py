# Made by brz
from scripts import pieces

class Score():
    def __init__(self):
        self.play_moves = []

    def set_score(self, piece, element_in_square, color):
        factor = 1 if piece.color == color else -1
        score = 0
        
        if isinstance(element_in_square, pieces.EmptySquare):
            if isinstance(piece, pieces.Queen):
                score = (jump(piece, element_in_square) + attack_crown_enemy_row(element_in_square, color)) * factor
            else:
                score = jump(piece, element_in_square) * factor

        else:
            score = capture_piece(piece, element_in_square, color) * factor
         
        play = {'from_row': piece.row, 
                'from_col': piece.col,
                'to_row': element_in_square.row,
                'to_col': element_in_square.col,
                'score': score}
                
        if play['score'] != 0:
            self.play_moves.append(play)

def protect_center(piece, element_in_square):
    if (6 <= element_in_square.row <= 9) and (5 <= element_in_square.col <= 10):
        # center vs center
        if (6 <= piece.row <= 9) and (5 <= piece.col <= 10):
            return 5
        # out vs center
        else:
            return 10
    else:
        # center vs out
        if (6 <= piece.row <= 9) and (5 <= piece.col <= 10):
            return 1
        # out vs out
        else:
            return 3

def attack_crown_enemy_row(square, color):
    if (color == True) and (square.row == 7):
        return 80
    elif (color == False) and (square.row == 8):
        return 80
    else:
        return 0

def jump(piece, element_in_square):
    if isinstance(piece, pieces.Pawn):
        if ((piece.row == 12) or (piece.row == 3))  and (5 <= piece.col <= 9):
            plus = plus = round(1 / abs(7.5 - element_in_square.row), 2) + 2
        elif ((piece.row == 13) or (piece.row == 2)) and (5 <= piece.col <= 7):
            plus = round(1 / abs(7.5 - element_in_square.row), 2) + 1
        elif ((piece.row != 13) or (piece.row == 2)) and 5 <= piece.col <= 9:
            plus = round(1 / abs(7.5 - element_in_square.row), 2) + 3
        else:
            plus = round(1 / abs(7.5 - element_in_square.row), 2)
        points = 60 + plus
    else:
        points = piece.point_move

    return points

def jump_to_square(piece, element_in_square):
    if isinstance(piece, pieces.Pawn):
        if piece.color == True:
            if (piece.row == 12) and (5 <= piece.col <= 9):
                plus = plus = round(1 / abs(7.5 - element_in_square.row), 2) + 2
            elif (piece.row == 13) and (5 <= piece.col <= 7):
                plus = round(1 / abs(7.5 - element_in_square.row), 2) + 1
            elif (piece.row != 13) and 5 <= piece.col <= 9:
                plus = round(1 / abs(7.5 - element_in_square.row), 2) + 3
            else:
                plus = round(1 / abs(7.5 - element_in_square.row), 2)
        if piece.color == False:
            if (piece.row == 3) and (5 <= piece.col <= 9):
                plus = plus = round(1 / abs(7.5 - element_in_square.row), 2) + 2
            elif (piece.row == 2) and 5 <= piece.col <= 7:
                plus = round(1 / abs(7.5 - element_in_square.row), 2) + 1
            else:
                plus = round(1 / abs(7.5 - element_in_square.row), 2)
        points = 60 + plus
    else:
        points = piece.point_move

    return points

def capture_piece(piece, element_in_square, color):
    if (piece.color == False) and (element_in_square.color == True):
        if element_in_square.row < 11:
            points = (element_in_square.point_been_captured + piece.point_move + protect_center(piece, element_in_square)) 
        else:
            if isinstance(element_in_square, pieces.King):
                points = (element_in_square.point_been_captured + piece.point_move + protect_center(piece, element_in_square)) / 1.5
            else:
                points = (element_in_square.point_been_captured + piece.point_move + protect_center(piece, element_in_square)) / 10  

    elif (piece.color == True) and (element_in_square.color == False):
        if element_in_square.row > 4:
            points = (element_in_square.point_been_captured + piece.point_move + protect_center(piece, element_in_square))  
        else:
            if isinstance(element_in_square, pieces.King):
                points = (element_in_square.point_been_captured + piece.point_move + protect_center(piece, element_in_square)) / 1.5
            else:
                points = (element_in_square.point_been_captured + piece.point_move  + protect_center(piece, element_in_square)) / 10

    return points

