from game.piece import Piece

class King(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return '♔' if self.get_color() == "WHITE" else '♚'
    
    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para el rey."""
        """Verificar si el destino es válido (no captura piezas propias)"""
        if not self.is_valid_destination(board, to_pos):
            return False
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1
   