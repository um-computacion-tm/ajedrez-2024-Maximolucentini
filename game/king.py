from game.piece import Piece

class King(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
    
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        "Verificar si el movimiento es horizontal, vertical o diagonal de 1 casilla"
        if abs(to_row - from_row) <= 1 and abs(to_col - from_col) <= 1:
            return True

        "Si no es un movimiento válido, devuelve False"
        return False
    
    def symbol(self):
        return 'K' if self.get_color() == "WHITE" else 'k'