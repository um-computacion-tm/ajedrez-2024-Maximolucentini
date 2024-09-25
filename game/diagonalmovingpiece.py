from game.piece import Piece

class DiagonalMovingPiece(Piece):
    def is_valid_diagonal_move(self, from_pos, to_pos):
        """Verificar si el movimiento es diagonal."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return abs(from_row - to_row) == abs(from_col - to_col)

    def is_path_clear(self, board, from_pos, to_pos):
        """Verificar si el camino está despejado para el movimiento de la pieza en diagonal."""
        if not self.is_valid_diagonal_move(from_pos, to_pos):
            return False
        
        row_step, col_step = self.get_diagonal_steps(from_pos, to_pos)
        return self.check_clear_path(board, from_pos, to_pos, row_step, col_step)

    def get_diagonal_steps(self, from_pos, to_pos):
        """Obtener los pasos para el movimiento diagonal."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        return (row_step, col_step)

    def check_clear_path(self, board, from_pos, to_pos, steps):
        """Verificar si el camino diagonal está despejado."""
        row_step, col_step = steps
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row, col = from_row + row_step, from_col + col_step
        
        while row != to_row and col != to_col:
            if board.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        
        return True


    def is_valid_piece_move(self, board, from_pos, to_pos):
     """Verificar si el movimiento es válido para las piezas que se mueven en diagonal."""
     if not self.is_valid_diagonal_move(from_pos, to_pos):
        return False

     if not self.is_path_clear(board, from_pos, to_pos):
        return False

     return super().is_valid_piece_move(board, from_pos, to_pos)
