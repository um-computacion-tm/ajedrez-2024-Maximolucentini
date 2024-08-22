from game.piece import *

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.__initial_position__ = position
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        # Movimiento hacia adelante: para peones que no están en la fila inicial
        direction = 1 if self.__color__ == "WHITE" else -1
        
        # Movimiento inicial: dos pasos hacia adelante
        if (from_row == self.__initial_position__[0] and 
            from_col == self.__initial_position__[1]):
            if (to_row == from_row + 2 * direction and from_col == to_col and
                board.get_piece(to_row, to_col) is None and 
                board.get_piece(from_row + direction, from_col) is None):
                return True

        # Movimiento normal: un paso hacia adelante
        if to_row == from_row + direction and from_col == to_col:
            if board.get_piece(to_row, to_col) is None:
                return True