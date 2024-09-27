from game.piece import Piece
from game.board import *

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.initial_position = True  
        """El peón empieza en su posición inicial"""

    def symbol(self):
        return 'P' if self.get_color() == "WHITE" else 'p'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verifica si el movimiento es válido para el peón."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        direction = -1 if self.color == 'WHITE' else 1

        """Verificar movimiento hacia adelante sin captura"""
        if self._valid_move_forward(board, from_row, from_col, to_row, to_col, direction):
            return True

        """Verificar captura en diagonal"""
        if self._valid_diagonal_capture(board, from_row, from_col, to_row, to_col, direction):
            return True

        return False

    def _valid_move_forward(self, board, from_row, from_col, to_row, to_col, direction):
        """Verificar si el movimiento hacia adelante es válido (sin captura)."""
        if from_col == to_col:  
            """Movimiento en la misma columna"""
            """Movimiento de un paso adelante"""
            if from_row + direction == to_row and board.get_piece(to_row, to_col) is None:
                return True
            """Movimiento de dos pasos desde la posición inicial"""
            if self.initial_position and from_row + 2 * direction == to_row and \
               board.get_piece(from_row + direction, from_col) is None and \
               board.get_piece(to_row, to_col) is None:
                return True
        return False

    def _valid_diagonal_capture(self, board, from_row, from_col, to_row, to_col, direction):
        """Verificar si la captura en diagonal es válida."""
        if abs(from_col - to_col) == 1 and from_row + direction == to_row:
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.get_color() != self.color:
                return True
        return False
