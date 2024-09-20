from game.piece import Piece

class StraightMovingPiece(Piece):
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

        return self.check_straight_path_clear(board, from_pos, to_pos)

    def check_straight_path_clear(self, board, from_pos, to_pos):
        """Determina si el camino es claro verificando en la dirección correcta."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos  

        if from_row == to_row:  #Movimiento horizontal
            return self.check_horizontal_path_clear(board, from_row, from_col, to_col)
        else:  # Movimiento vertical
            return self.check_vertical_path_clear(board, from_col, from_row, to_row)

    def check_horizontal_path_clear(self, board, row, start_col, end_col):
        """Verificar si el camino horizontal está despejado."""
        for col in range(min(start_col, end_col) + 1, max(start_col, end_col)):
            if board.get_piece(row, col) is not None:
                return False
        return True

    def check_vertical_path_clear(self, board, col, start_row, end_row):
        """Verificar si el camino vertical está despejado."""
        for row in range(min(start_row, end_row) + 1, max(start_row, end_row)):
            if board.get_piece(row, col) is not None:
                return False
        return True

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para las piezas que se mueven en línea recta."""
        return self.is_valid_straight_move(from_pos, to_pos) and \
               self.is_path_clear(board, from_pos, to_pos) and \
               super().is_valid_piece_move(board, from_pos, to_pos)
