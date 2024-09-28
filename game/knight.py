from game.piece import Piece

class Knight(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'N' if self.get_color() == "WHITE" else 'n'    
        
    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para el caballo."""
        return self._is_knight_move(from_pos, to_pos)
    
    def _is_knight_move(self, from_pos, to_pos):
        """Verificar si el movimiento sigue la forma de 'L' (movimiento válido del caballo)."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
    
    
