from game.straightmovingpiece import StraightMovingPiece

class Rook(StraightMovingPiece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'R' if self.get_color() == "WHITE" else 'r'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para la torre."""
        """La torre puede moverse vertical o horizontalmente."""
        """Llama a la validación de la clase base"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return super().is_valid_piece_move(board, from_row, from_col, to_row, to_col)
