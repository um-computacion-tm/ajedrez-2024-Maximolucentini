from game.diagonalmovingpiece import DiagonalMovingPiece

class Bishop(DiagonalMovingPiece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'B' if self.get_color() == "WHITE" else 'b'

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es válido para el alfil."""
        """El alfil se mueve en diagonal."""
        """Llama a la validacion de la clase base"""
        return super().is_valid_piece_move(board, from_row, from_col, to_row, to_col)

    
    