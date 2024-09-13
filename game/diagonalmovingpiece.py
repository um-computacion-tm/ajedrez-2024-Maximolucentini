from game.piece import Piece

class DiagonalMovingPiece(Piece):
    def is_valid_diagonal_move(self, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es diagonal."""
        return abs(from_row - to_row) == abs(from_col - to_col)

    def is_path_clear(self, board, from_row, from_col, to_row, to_col):
        """Verificar si el camino está despejado para el movimiento de la pieza en diagonal."""
        if not self.is_valid_diagonal_move(from_row, from_col, to_row, to_col):
            return False
        
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        row, col = from_row + row_step, from_col + col_step
        
        while row != to_row and col != to_col:
            if board.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        
        return True

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es válido para las piezas que se mueven en diagonal."""
        return self.is_valid_diagonal_move(from_row, from_col, to_row, to_col) and \
               self.is_path_clear(board, from_row, from_col, to_row, to_col) and \
               super().is_valid_piece_move(board, from_row, from_col, to_row, to_col)
