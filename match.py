import pieces
import moves

class Match():
    def __init__(self, board_id):
        self.board_id = board_id
        self.color = None

        # Black pieces
        self.black_pawns      = []
        self.black_horses     = []
        self.black_bishops    = []
        self.black_rooks      = []
        self.black_queens     = []
        self.black_kings      = []
        # White pieces
        self.white_pawns      = []
        self.white_horses     = []
        self.white_bishops    = []
        self.white_rooks      = []
        self.white_queens     = []
        self.white_kings      = []
        # Empty squares
        self.empty_squares    = []
    
    def create_pieces(self,board):

        for row, pieces_row in enumerate(board):
            for col, piece in enumerate(pieces_row):
                # Creates a list with black objects
                if piece == 'p':
                    self.black_pawns.append(pieces.Pawn('black', row, col))
                elif piece == 'h':
                    self.black_horses.append(pieces.Horse('black', row, col))
                elif piece == 'b':
                    self.black_bishops.append(pieces.Bishop('black', row, col))
                elif piece == 'r':
                    self.black_rooks.append(pieces.Rook('black', row, col))
                elif piece == 'q':
                    self.black_queens.append(pieces.Queen('black', row, col))
                elif piece == 'k':
                    self.black_kings.append(pieces.King('black', row, col))

                # Creates a list with white objects
                elif piece == 'P':
                    self.white_pawns.append(pieces.Pawn('white', row, col))
                elif piece == 'H':
                    self.white_horses.append(pieces.Horse('white', row, col))
                elif piece == 'B':
                    self.white_bishops.append(pieces.Bishop('white', row, col))
                elif piece == 'R':
                    self.white_rooks.append(pieces.Rook('white', row, col))
                elif piece == 'Q':
                    self.white_queens.append(pieces.Queen('white', row, col))
                elif piece == 'K':
                    self.white_kings.append(pieces.King('white', row, col))

                # Creates a list with empty squares
                else:
                    self.empty_squares.append(pieces.EmptySquare(row, col))

    def get_board_id(self):
        return self.board_id

    def get_color(self):
        return self.color

    def get_black_pieces(self):
        return self.black_pawns, self.black_horses, self.black_bishops, self.black_rooks, self.black_queens, self.black_kings

    def get_white_pieces(self):
        return self.white_pawns, self.white_horses, self.white_bishops, self.white_rooks, self.white_queens, self.white_kings

    def get_empty_squeares(self):
        return self.empty_squares

    def double_move(self):
        n = 2
        valid_move = moves.check_constrains(self.p1, n, self.direction)
        if valid_move:
            moves.n_square_line(self.p1, n, direction)
        else:
            print("Invaid move")
        return self.p

    def set_color(self, color):
        self.color = color

    def simple_move(self):
        n = 1
        valid_move = moves.check_constrains(self.p1, n, self.direction)
        if valid_move:
            moves.n_square_line(self.p1, n, direction)
        else:
            print("Invaid move")

def split_pieces(board):
    n = 16
    board_split_rows = [board[i:i+n] for i in range(0, len(board), n)]

    return board_split_rows