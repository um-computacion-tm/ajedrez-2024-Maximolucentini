from game.piece import Piece

class Knight(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return '♘' if self.get_color() == "WHITE" else '♞'
        
    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para el caballo."""
        """Usar is_valid_destination de la clase base para validar destino"""
        if not self.is_valid_destination(board, to_pos):
            return False  
        """Movimiento inválido si la posición está ocupada por una pieza propia o fuera del tablero"""

        """Verificar el movimiento en forma de L del caballo"""
        return self._is_knight_move(from_pos, to_pos)
    
    def _is_knight_move(self, from_pos, to_pos):
        """Verificar si el movimiento sigue la forma de 'L' (movimiento válido del caballo)."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
    
