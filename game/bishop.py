from game.piece import Piece

class Bishop(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        """
        Los alfiles se mueven en diagonal.
        """
        """Verificar que el movimiento sea diagonal"""
        if abs(to_row - from_row) != abs(to_col - from_col):
            return False

        """Calcular la dirección del movimiento"""
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1

        """Verificar que no haya piezas en el camino"""
        for i in range(1, abs(to_row - from_row)):
            row = from_row + i * row_step
            col = from_col + i * col_step
            if board.get_piece(row, col) is not None:
                return False

        """Verificar que la casilla de destino esté vacía o ocupada por una pieza del color contrario"""
        if board.get_piece(to_row, to_col) is not None and board.get_piece(to_row, to_col).get_color() == self.get_color():
            return False

        return True    