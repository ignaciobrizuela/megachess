# Made by brz
from scripts import pieces

class Score():
    def __init__(self):
        self.play_moves = []

    def set_score(self, piece, element_in_square, color):
        factor = 1 if piece.color == color else -1
        score = 0
        p_points = piece.point_move
        e_points = element_in_square.point_been_captured

        zone_piece = get_zone(piece, color)
        zone_element_in_square = get_zone(element_in_square, color)
        zone_diff = zone_difference(zone_piece, zone_element_in_square)
        plus = get_plus(piece, element_in_square)
        
        if factor == 1:
            score = ((p_points * zone_diff) + (e_points * zone_diff) + plus) * factor
        else:
            score = e_points * 10 * factor
         
        play = {'from_row': piece.row, 
                'from_col': piece.col,
                'to_row': element_in_square.row,
                'to_col': element_in_square.col,
                'score': score}
                
        if play['score'] != 0:
            self.play_moves.append(play)

def get_pawn_plus(piece, square):
    points = 0 
    if piece.color == True:
        if (piece.row == 12) or (piece.row == 13):
            if (5 <= piece.col <= 7):
                points = 5
            elif (0 <= piece.col <= 4) or (10 <= piece.col <= 15):
                points = 2
            else: 
                points = 0
        else:
            points = 10

    if piece.color == False:
        if (piece.row == 3) or (piece.row == 2):
            if (5 <= piece.col <= 7):
                points = 5
            elif (0 <= piece.col <= 4) or (10 <= piece.col <= 15):
                points = 2
            else: 
                points = 0
        else:
            points = 0

    plus = 60 - round(abs(7.5 - square.row), 2) + points

    return plus

def get_queen_plus(queen, square):
    plus = 0
    if queen.color == True:
        if (square.row == 7) and (queen.row != 7):
            plus = 500
        else:
            plus = 0
    elif  queen.color == False:
        if (square.row == 8) and (queen.row != 8):
            plus = 500
        if (square.row != 8) and (queen.row == 8):
            plus = - 250
        else:
            plus = 0

    return plus

def get_zone(piece, color):
    if color == True:
        if (0 <= piece.row < 6) and ((0 <= piece.col < 6)or (9 < piece.col <= 15)):
            return 5
        if (0 <= piece.row < 6) and (6 <= piece.col <= 9):
            return 6
        elif (6 <= piece.row <= 9) and ((0 <= piece.col < 6)or (9 < piece.col <= 15)):
            return 7
        elif (9 < piece.row <= 15) and ((0 <= piece.col < 6)or (9 < piece.col <= 15)):
            return 8
        elif (9 < piece.row <= 15) and (6 <= piece.col <= 9):
            return 9
        elif (6 <= piece.row <= 9) and (6 <= piece.col <= 9):
            return 10

    elif color == False:
        if (0 <= piece.row < 6) and ((0 <= piece.col < 6)or (9 < piece.col <= 15)):
            return 8
        if (0 <= piece.row < 6) and (6 <= piece.col <= 9):
            return 9
        elif (6 <= piece.row <= 9) and ((0 <= piece.col < 6)or (9 < piece.col <= 15)):
            return 7
        elif (9 < piece.row <= 15) and ((0 <= piece.col < 6)or (9 < piece.col <= 15)):
            return 5
        elif (9 < piece.row <= 15) and (6 <= piece.col <= 9):
            return 6
        elif (6 <= piece.row <= 9) and (6 <= piece.col <= 9):
            return 10

def zone_difference(piece_zone, element_zone):
    if piece_zone <= element_zone:
        return element_zone
    else:
        if 4 <= element_zone <= 5:
            return 1 / piece_zone
        else:
            return piece_zone

def get_plus(piece, element_in_square):
    if isinstance(piece, pieces.Pawn):
        return get_pawn_plus(piece, element_in_square)
    elif isinstance(piece, pieces.Queen):
        return get_queen_plus(piece, element_in_square)
    else:
        return 0