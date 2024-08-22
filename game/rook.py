from game.piece import *

class Rook(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        # Las torres se mueven en línea recta, ya sea horizontal o verticalmente.
        
        # Movimiento horizontal
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) is not None:
                    return False
            return True
        

    