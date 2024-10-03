from game.piece import Piece

class Knight(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'N' if self.get_color() == "WHITE" else 'n'    
        
    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para el caballo."""
        """Descomponer las posiciones"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        """Verificar que las posiciones están dentro del tablero"""
        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            return False  
        """Movimiento fuera del tablero"""

        """Obtener la pieza en la posición de destino"""
        destination_piece = board.get_piece(to_row, to_col)

        """Verificar si la pieza en el destino es del mismo color"""
        if destination_piece is not None and destination_piece.get_color() == self.get_color():
            return False  
        """No puede capturar piezas propias"""

        """Verificar el movimiento en forma de L del caballo"""
        return self._is_knight_move(from_pos, to_pos)
    
    def _is_knight_move(self, from_pos, to_pos):
        """Verificar si el movimiento sigue la forma de 'L' (movimiento válido del caballo)."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
    
    
