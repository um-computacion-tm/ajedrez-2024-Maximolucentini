from game.piece import Piece

class Queen(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'Q' if self.get_color() == "WHITE" else 'q'    
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
     """Verificar condiciones generales"""
     if not super().is_valid_move(board, from_row, from_col, to_row, to_col):
        return False
     """La Reina se mueve en cualquier dirección (horizontal, vertical o diagonal) cualquier número de casillas."""
    
     """Movimiento horizontal y vertical"""
     if from_row == to_row:
        step = 1 if to_col > from_col else -1
        for col in range(from_col + step, to_col + step, step):
            if board.get_piece(from_row, col) is not None:
                return False
        return True
    
        
     elif from_col == to_col:
        step = 1 if to_row > from_row else -1
        for row in range(from_row + step, to_row + step, step):
            if board.get_piece(row, from_col) is not None:
                return False
        return True
       
    
     
     elif abs(to_row - from_row) == abs(to_col - from_col):
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        for i in range(1, abs(to_row - from_row) + 1):
            row = from_row + i * row_step
            col = from_col + i * col_step
            if board.get_piece(row, col) is not None:
                return False
        return True
     """Movimiento diagonal"""
    
     """Si no se mueve en línea recta o diagonal, el movimiento no es válido."""
     return False
 
    
