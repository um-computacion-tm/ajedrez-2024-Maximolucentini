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

        is_horizontal = from_pos[0] == to_pos[0]
        return self._verify_path_clear(board, from_pos, to_pos, is_horizontal)

    def _verify_path_clear(self, board, from_pos, to_pos, is_horizontal):
        """Verificar si el rango (horizontal o vertical) está despejado."""
        start_pos, end_pos, fixed_pos = self._get_positions(from_pos, to_pos, is_horizontal)

        check_position = (lambda pos: board.get_piece(fixed_pos, pos)) if is_horizontal else \
                         (lambda pos: board.get_piece(pos, fixed_pos))

        for pos in range(min(start_pos, end_pos) + 1, max(start_pos, end_pos)):
            if check_position(pos) is not None:
                return False
        return True

    def _get_positions(self, from_pos, to_pos, is_horizontal):
        """Obtener las posiciones de inicio, fin y fijo según el tipo de movimiento."""
        if is_horizontal:
            return from_pos[1], to_pos[1], from_pos[0]
        else:
            return from_pos[0], to_pos[0], from_pos[1]

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para las piezas que se mueven en línea recta."""
        return (self._is_within_board(to_pos) 
                and not self._is_same_position(from_pos, to_pos)
                and self.is_valid_straight_move(from_pos, to_pos)
                and self.is_path_clear(board, from_pos, to_pos)
                and self.is_valid_destination(board, to_pos))

    def _is_within_board(self, pos):
        """Validar si una posición está dentro de los límites del tablero."""
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

    def _is_same_position(self, from_pos, to_pos):
        """Validar si el origen y destino son la misma posición."""
        return from_pos == to_pos







