from game.piece import Piece
from game.board import *

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.__initial_position__ = position
        
    def symbol(self):
        return 'P' if self.get_color() == "WHITE" else 'p'    
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
     """Verificar condiciones generales"""
     if not super().is_valid_move(board, from_row, from_col, to_row, to_col):
        return False

     """Establecer la dirección correcta"""
     direction = -1 if self.get_color() == "WHITE" else 1
    
     """Movimiento inicial: dos pasos hacia adelante"""
     if (self.get_color() == "BLACK" and from_row == 1) or (self.get_color() == "WHITE" and from_row == 6):
        if (to_row == from_row + 2 * direction and from_col == to_col and
            board.get_piece(to_row, to_col) is None and 
            board.get_piece(from_row + direction, from_col) is None):
            return True
    
     """Movimiento normal: un paso hacia adelante"""
     if to_row == from_row + direction and from_col == to_col:
        if board.get_piece(to_row, to_col) is None:
            return True
    
     """Captura: un paso en diagonal hacia adelante"""
     if to_row == from_row + direction and abs(to_col - from_col) == 1:
        if board.get_piece(to_row, to_col) is not None and board.get_piece(to_row, to_col).get_color() != self.get_color():
            return True

     return False
 
    

 
    