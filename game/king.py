from game.piece import Piece

class King(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'K' if self.get_color() == "WHITE" else 'k'
    
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        """Verificar condiciones generales"""
        if not super().is_valid_move(board, from_row, from_col, to_row, to_col):
            return False

        """Verificar si el movimiento es horizontal, vertical o diagonal de 1 casilla"""
        if abs(to_row - from_row) <= 1 and abs(to_col - from_col) <= 1:
            return True

        """Si no es un movimiento válido, devuelve False"""
        return False
    
   