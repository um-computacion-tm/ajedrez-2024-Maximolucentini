from game.piece import Piece

class Rook(Piece):
  def __init__(self, color, position=None):
    super().__init__(color, position)
        
  def symbol(self):
        return 'R' if self.get_color() == "WHITE" else 'r'    

  def is_valid_move(self, board, from_row, from_col, to_row, to_col):
      """Verificar condiciones generales"""
      if not super().is_valid_move(board, from_row, from_col, to_row, to_col):
        return False
      """Las torres se mueven en línea recta, ya sea horizontal o verticalmente."""
    
      """Movimiento horizontal"""
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
      """Movimiento vertical"""
    
      """Si no se mueve en línea recta, el movimiento no es válido."""
      return False



        
    