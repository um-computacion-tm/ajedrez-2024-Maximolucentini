from game.piece import Piece
from game.board import *

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.initial_position = True  
        """El peón empieza en su posición inicial"""

    def symbol(self):
        return '♙' if self.get_color() == "WHITE" else '♟'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verifica si el movimiento es válido para el peón."""
        direction = -1 if self.color == 'WHITE' else 1

        """Verificar movimiento hacia adelante sin captura"""
        if self._valid_move_forward(board, from_pos, to_pos, direction):
            return True

        """Verificar captura en diagonal"""
        if self._valid_diagonal_capture(board, from_pos, to_pos, direction):
            return True

        return False

    def _valid_move_forward(self, board, from_pos, to_pos, direction):
        """Verificar si el movimiento hacia adelante es válido (sin captura)."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        """Movimiento en la misma columna"""
        if from_col == to_col:
            """Verificar si es un paso adelante"""
            if self._is_one_step_forward(board, from_pos, to_pos, direction):
                return True
            """Verificar si es un paso doble desde la posición inicial"""
            if self._is_two_steps_forward(board, from_pos, to_pos, direction):
                return True
        return False

    def _is_one_step_forward(self, board, from_pos, to_pos, direction):
        """Verificar si es un paso adelante y la casilla está libre."""
        from_row, _ = from_pos
        to_row, _ = to_pos
        return from_row + direction == to_row and board.get_piece(to_pos[0], to_pos[1]) is None

    def _is_two_steps_forward(self, board, from_pos, to_pos, direction):
        """Verificar si el peón puede avanzar dos pasos desde la posición inicial."""
        from_row, from_col = from_pos
        to_row, _ = to_pos
        return self.initial_position and from_row + 2 * direction == to_row and \
               board.get_piece(from_row + direction, from_col) is None and \
               board.get_piece(to_pos[0], to_pos[1]) is None

    def _valid_diagonal_capture(self, board, from_pos, to_pos, direction):
        """Verificar si la captura en diagonal es válida."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if abs(from_col - to_col) == 1 and from_row + direction == to_row:
            target_piece = board.get_piece(to_row, to_col)
            return self._is_enemy_piece(target_piece)
        return False

    def _is_enemy_piece(self, target_piece):
        """Verificar si la pieza objetivo es enemiga."""
        return target_piece is not None and target_piece.get_color() != self.color
