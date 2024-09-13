from game.piece import Piece

class StraightMovingPiece(Piece):
    def is_valid_horizontal_move(self, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es horizontal."""
        return from_row == to_row

    def is_valid_vertical_move(self, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es vertical."""
        return from_col == to_col

    def is_path_clear(self, board, from_row, from_col, to_row, to_col):
        """Verificar si el camino está despejado para el movimiento de la pieza en línea recta."""
        if not (self.is_valid_horizontal_move(from_row, from_col, to_row, to_col) or 
                self.is_valid_vertical_move(from_row, from_col, to_row, to_col)):
            return False
        
        if self.is_valid_horizontal_move(from_row, from_col, to_row, to_col):
            """Movimiento horizontal"""
            for col in range(min(from_col, to_col) + 1, max(from_col, to_col)):
                if board.get_piece(from_row, col) is not None:
                    return False
        elif self.is_valid_vertical_move(from_row, from_col, to_row, to_col):
            """Movimiento vertical"""
            for row in range(min(from_row, to_row) + 1, max(from_row, to_row)):
                if board.get_piece(row, from_col) is not None:
                    return False
        
        return True

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es válido para las piezas que se mueven en línea recta."""
        return ((self.is_valid_horizontal_move(from_row, from_col, to_row, to_col) or 
                 self.is_valid_vertical_move(from_row, from_col, to_row, to_col)) and 
                self.is_path_clear(board, from_row, from_col, to_row, to_col)) and \
               super().is_valid_piece_move(board, from_row, from_col, to_row, to_col)
