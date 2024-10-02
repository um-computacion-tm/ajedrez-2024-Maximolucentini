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
        
        valid_move = True  # Asumimos que el movimiento es válido

        # Validar que la pieza no se mueve a la misma casilla
        if from_pos == to_pos:
            valid_move = False

        # Validar que la posición de destino esté dentro de los límites del tablero
        elif not (0 <= to_pos[0] < 8 and 0 <= to_pos[1] < 8):
            valid_move = False

        # Validar que el movimiento sea en línea recta
        elif not self.is_valid_straight_move(from_pos, to_pos):
            valid_move = False

        # Validar que el camino esté despejado
        elif not self.is_path_clear(board, from_pos, to_pos):
            valid_move = False

        # Verificar si hay una pieza en la casilla destino del mismo color
        else:
            final_piece = board.get_piece(to_pos[0], to_pos[1])
            if final_piece is not None and final_piece.get_color() == self.get_color():
                valid_move = False  # No puede capturar una pieza propia

        return valid_move






