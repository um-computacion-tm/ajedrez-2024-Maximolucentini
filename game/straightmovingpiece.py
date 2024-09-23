from game.piece import Piece

from game.piece import Piece

class StraightMovingPiece(Piece):
    def is_valid_straight_move(self, from_pos, to_pos):
        """Verificar si el movimiento es en línea recta (horizontal o vertical)."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return from_row == to_row or from_col == to_col

    def is_path_clear(self, board, from_pos, to_pos):
        """Verificar si el camino está despejado para el movimiento de la pieza en línea recta."""
        if not self.is_valid_straight_move(from_pos, to_pos):
            return False

        return self.check_path_clear(board, from_pos, to_pos)

    def check_path_clear(self, board, from_pos, to_pos):
        """Verificar si el camino en línea recta (horizontal o vertical) está despejado."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        """Movimiento horizontal"""
        if from_row == to_row:
            return self.check_clear_range(board, from_row, from_col, to_col, horizontal=True)

        """Movimiento vertical"""
        return self.check_clear_range(board, from_col, from_row, to_row, horizontal=False)

    def check_clear_range(self, board, fixed_pos, start_pos, end_pos, horizontal):
        """Verificar si el rango de movimiento está despejado (horizontal o vertical)."""
        for pos in range(min(start_pos, end_pos) + 1, max(start_pos, end_pos)):
            if horizontal:
                if board.get_piece(fixed_pos, pos) is not None:
                    return False
            else:
                if board.get_piece(pos, fixed_pos) is not None:
                    return False
        return True

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para las piezas que se mueven en línea recta."""
        return self.is_valid_straight_move(from_pos, to_pos) and \
               self.is_path_clear(board, from_pos, to_pos) and \
               super().is_valid_piece_move(board, from_pos, to_pos)
