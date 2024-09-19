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
        """Verificar si el camino en línea recta está despejado."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if from_row == to_row:  
            """Movimiento horizontal"""
            for col in range(min(from_col, to_col) + 1, max(from_col, to_col)):
                if board.get_piece(from_row, col) is not None:
                    return False
        else:  
            """Movimiento vertical"""
            for row in range(min(from_row, to_row) + 1, max(from_row, to_row)):
                if board.get_piece(row, from_col) is not None:
                    return False

        return True

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para las piezas que se mueven en línea recta."""
        return ((self.is_valid_horizontal_move(from_pos, to_pos) or 
                 self.is_valid_vertical_move(from_pos, to_pos)) and 
                self.is_path_clear(board, from_pos, to_pos)) and \
               super().is_valid_piece_move(board, from_pos, to_pos)
