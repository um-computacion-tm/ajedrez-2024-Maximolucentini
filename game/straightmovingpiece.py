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

        """Identificar si es un movimiento horizontal o vertical"""
        is_horizontal = from_pos[0] == to_pos[0]
        
        """Llamar a la función con las posiciones y tipo de movimiento"""
        return self._verify_path_clear(board, from_pos, to_pos, is_horizontal)

    def _verify_path_clear(self, board, from_pos, to_pos, is_horizontal):
        """Verificar si el rango (horizontal o vertical) está despejado."""
        start_pos, end_pos = (from_pos[1], to_pos[1]) if is_horizontal else (from_pos[0], to_pos[0])
        fixed_pos = from_pos[0] if is_horizontal else from_pos[1]

        for pos in range(min(start_pos, end_pos) + 1, max(start_pos, end_pos)):
            
            if (board.get_piece(fixed_pos, pos) if is_horizontal else board.get_piece(pos, fixed_pos)) is not None:
                return False
        return True

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para las piezas que se mueven en línea recta."""
        return self.is_valid_straight_move(from_pos, to_pos) and \
               self.is_path_clear(board, from_pos, to_pos) and \
               super().is_valid_piece_move(board, from_pos, to_pos)

