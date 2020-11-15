# Made by brz

def n_square_line(obj, n, direction):
    try:
        tag = obj.get_tag()
        row, col = obj.get_position()
    except Exception as e:
        print("Object error: is not a chess piece.")

    if direction == 'up':
        row -= n
    elif direction == 'down':
        row += n
    elif direction == 'rigth':
        col += n
    elif direction == 'left':
        col -= n
    else:
        print("Wrong direction: must be up, down, right, left")

    return row, col

def n_square_diagonal(obj, n, direction):
    try:
        tag = obj.get_tag()
        row, col = obj.get_position()
    except Exception as e:
        print("Object error: is not a chess piece.")

    if direction == 'ur': # ur = up-right
        row -= n
        col += n
    elif direction == 'ul': # ul = up-left
        row -= n
        col -= n
    elif direction == 'dr': # dr = down-right
        row += n
        col += n
    elif direction == 'dl': # dl = down-left
        row += n
        col -= n
    else:
        print("Wrong direction: must be up, down, right, left")
    

    return row, col

def check_constrains(obj, n, direction):
    try:
        tag = obj.get_tag()
        row, col = obj.get_position()
    except Exception as e:
        print("Object error: is not a chess piece.")

    print(tag,row,col,n,direction)
    # <<< PAWN >>>
    if tag == 'p' or tag =='P':
        # Double square move
        if tag =='p' and row ==3 and n==2 and direction=='down':
            return True
        elif tag == 'P' and row == 12 and n==2 and direction=='up':
            return True
        # Single square move
        elif tag =='p' and row >=3 and n==1 and direction=='down':
            return True
        elif tag == 'P' and row <= 12 and n==1 and direction=='up':
            return True
        # Capture piece, one diagonal square
        # elif tag =='p' and row >=3 and n==1:
        #     return True
        # elif tag == 'P' and row <= 12 and n==1:
        #     return True
        else:
            return False