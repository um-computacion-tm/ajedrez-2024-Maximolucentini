from game.piece import Piece

class Knight(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'N' if self.get_color() == "WHITE" else 'n'    
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        """Verificar condiciones generales"""
        if not super().is_valid_move(board, from_row, from_col, to_row, to_col):
         return False
        """
        Los caballos se mueven en L (dos casillas en una dirección y una casilla en otra dirección perpendicular).
        """
        """ Verificar que el movimiento sea en L"""
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            """Verificar que la casilla de destino esté vacía o ocupada por una pieza del color contrario"""
            if board.get_piece(to_row, to_col) is not None and board.get_piece(to_row, to_col).get_color() == self.get_color():
                return False
            return True
        return False
    
    
