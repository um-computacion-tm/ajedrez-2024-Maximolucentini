from game.piece import Piece
from game.board import *

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.__initial_position__ = position
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
     """Movimiento hacia adelante: para peones que no están en la fila inicial"""
     direction = 1 if self.__color__ == "WHITE" else -1

     """Movimiento inicial: dos pasos hacia adelante"""
     if from_row == 1 and self.__color__ == "BLACK" or from_row == 6 and self.__color__ == "WHITE":
        if (to_row == from_row + 2 * direction and from_col == to_col and
            board.get_piece(to_row, to_col) is None and 
            board.get_piece(from_row + direction, from_col) is None and
            board.get_piece(to_row, to_col) is None):
            return True

     """Movimiento normal: un paso hacia adelante"""
     if to_row == from_row + direction and from_col == to_col:
        if board.get_piece(to_row, to_col) is None:
            return True

     """Captura: un paso en diagonal hacia adelante"""
     if (to_row == from_row + direction and 
        abs(to_col - from_col) == 1 and 
        board.get_piece(to_row, to_col) is not None and 
        board.get_piece(to_row, to_col).get_color() != self.__color__):
        return True    

     return False
 
    