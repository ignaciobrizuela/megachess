
def split_board(board):
    n = 16
    board_split_rows = [board[i:i+n] for i in range(0, len(board), n)]
    board_split_pieces = []
    for row in board_split_rows:
        selected_row = [row[i:i+1] for i in range(0, len(row), 1)]
        board_split_pieces.append(selected_row)

    return board_split_pieces
