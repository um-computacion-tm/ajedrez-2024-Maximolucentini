from game.piece import Piece
from game.board import *

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.initial_position = True  
        """El peón empieza en su posición inicial"""
        
    def symbol(self):
        return 'P' if self.get_color() == "WHITE" else 'p'

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido para el peón."""
        direction = -1 if self.color == 'WHITE' else 1

        """Movimiento hacia adelante sin capturar"""
        if from_col == to_col:
            if from_row + direction == to_row and board.get_piece(to_row, to_col) is None:
                return True
            if self.initial_position and from_row + 2 * direction == to_row and \
               board.get_piece(from_row + direction, from_col) is None and \
               board.get_piece(to_row, to_col) is None:
                return True

        """Captura en diagonal"""
        if abs(from_col - to_col) == 1 and from_row + direction == to_row:
            if board.get_piece(to_row, to_col) is not None and \
               board.get_piece(to_row, to_col).get_color() != self.color:
                return True

        return False
